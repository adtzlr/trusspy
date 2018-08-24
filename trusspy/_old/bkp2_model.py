# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:08:10 2018

@author: adutz
"""

import numpy as np
import pandas as pd

from trusspy.tools.helper_functions2 import plot_nodes, plot_elems, plot_force, plot_hist

# Manager Classes
from trusspy.managers.manager_settings import SettingsManager
from trusspy.managers.manager_node import NodeManager
from trusspy.managers.manager_element import ElementManager
from trusspy.managers.manager_boundary import BoundaryManager  
from trusspy.managers.manager_extforce import ExternalForceManager
from trusspy.managers.manager_result import ResultManager

from scipy.optimize import fsolve
from trusspy.solvers.newton_rhapson import newton_rhapson

import matplotlib.pyplot as plt

class Model:
    "Create Model Class with Nodes, Elements, Boundaries, etc."
    def __init__(self,file=None,log=2):
        if log > 1: print('')
        if log > 1: print('Initialize Model...')
        if log > 1: print('---------------------------------------')
        if log > 1: print(' loading Managers...')
        
        self.Nodes = NodeManager()
        self.Elements = ElementManager()
        self.Boundaries = BoundaryManager()
        self.ExtForces = ExternalForceManager()
        self.Settings = SettingsManager()
        self.Results = ResultManager()
        
        if log > 1: print(' ...finished.')
        if log > 1: print('---------------------------------------\n')
        
        if file is not None:
            if log > 1: print(' loading INPUT-File: "'+file+'"')
            Nodes = pd.read_excel(file,sheet_name="Nodes",skiprows=2).as_matrix()[:,:4].astype(float)
            Elements = pd.read_excel(file,sheet_name="Elements",skiprows=2).as_matrix()[:,:6].astype(float)
            ExtForces = pd.read_excel(file,sheet_name="ExternalForces",skiprows=2).as_matrix()[:,:4].astype(float)
            Boundary_U = pd.read_excel(file,sheet_name="BoundaryU",skiprows=2).as_matrix()[:,:4].astype(float)
            Boundary_T = pd.read_excel(file,sheet_name="BoundaryT",skiprows=2).as_matrix()[:,:2].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' Converting Data...')
            self.Nodes.add_node_matrix(Nodes)
            self.Elements.add_element_matrix(Elements,Boundary_T)
            self.ExtForces.add_force_matrix(ExtForces)
            self.Boundaries.add_bound_U_matrix(Boundary_U)

            if log > 1: print(' ...Import finised.\n')
            if log > 1: print('---------------------------------------')
            
            if log > 2:
                print(' ...Imported Data:')
                print(self.Nodes.coords)
                print(self.Elements.conns)
                print(self.Elements.material)
                print(self.Elements.alpha)
                print(self.ExtForces.forces)
                print(self.Boundaries.Uvalues)
    
    def build(self):
        
        # initialize numbers: #nodes, #elements, #dof
        self.nnodes = len(self.Nodes.labels)
        self.nelems = len(self.Elements.labels)
        self.ndim = self.Settings.ndim
        self.ndof = self.nnodes * self.ndim
        
        # node properties
        # n----pro-------
        #
        #      active = free  = 1
        #    inactive = fixed = 0
        
        self.nproBC = self.Boundaries.Uvalues
        self.nproDOF = np.arange(self.ndof).reshape(self.nnodes,self.ndim)
        self.nproDOF0 = self.nproDOF.flatten()[np.where(self.nproBC.flatten() == 0)]
        self.nproDOF1 = self.nproDOF.flatten()[np.where(self.nproBC.flatten() == 1)]
        self.ndof0 = len(self.nproDOF0)
        self.ndof1 = len(self.nproDOF1)
        
        if self.Settings.log > 1: 
            print('')
            print('Build Model...')
            print('---------------------------------------')
            print(' Analysis Dimension ...', self.Settings.ndim)
            print(' Number of Nodes    ...', self.nnodes)
            print(' Number of Elements ...', self.nelems)
            print(' ')
            print(' System DOF ...', self.ndof)
            print(' active DOF ...', self.ndof1)
            print(' locked DOF ...', self.ndof0)
            print(' ')
            print(' active DOF ...', self.nproDOF1)
            print(' fixed  DOF ...', self.nproDOF0)
            
    def run(self):
        if self.Settings.log > 1: 
            print(' ')
            print('Run Simulation...')
            print('---------------------------------------')
        
        # init results, add empty increment
        self.Results.add_increment()
        self.Results.build_result(self.nnodes,self.nelems,self.ndim,
                                  self.nproDOF0,self.nproDOF1)
        
        # init max. allowed step sizes
        self.Settings.dVmax = np.ones(self.ndof1)*self.Settings.du
        self.Settings.dVmax = np.append(self.Settings.dVmax, self.Settings.dlpf)
        self.Settings.dVmax0 = np.copy(self.Settings.dVmax)
        
        # get reduced external force vector
        f0red = self.ExtForces.forces.flatten()[self.Results.R[-1].DOF1]
        self.Results.R[-1].f0red = f0red.reshape(len(f0red),1)
        
        # init value for active component "j" in control equation qc
        self.Results.R[-1].j = 1
        
        # jacobian, extended to nDOF+1
        def dgdV(Vred):
            # K"c"ontrol "v"ertical extension, "h"orizontal extension
            
            # qc ... control equation
            qc = np.zeros(self.ndof1+1)
            qc[abs(self.Results.R[-1].j)-1] = np.sign(self.Results.R[-1].j)

            # f0red ... external force vector f0 with active DOF
            # reshaped to column-vector
            
            # modified stiffness
            #
            #          | KT       f0red |
            # KT_mod = | qcU  qc_lambda |
            
            
            self.Results.R[-1].Kmod = np.vstack((np.hstack((self.jacobian(Vred[:-1]),
                                                 -self.Results.R[-1].f0red)),qc))
            
            return self.Results.R[-1].Kmod
        
        # equilibrium function, extended to nDOF+1
        def g(Vred):
            #self.Settings.lpf = Vred[-1]
            # negative sign for default newton-rhapson function
            return np.append(-self.equilibrium(Vred), -self.Settings.dVmax[abs(self.Results.R[-1].j)-1])
        
        # reduced modified displacement vector to active DOF and LPF
        self.Results.R[-1].Vred = np.append(self.Results.R[-1].Ured, self.Settings.dlpf)
        self.Results.R[-1].Vred0 = np.copy(self.Results.R[-1].Vred)
        self.Results.R[-1].lpf = 0
        
        # init LPF
        # self.Settings.lpf = self.Settings.dlpf
        self.Results.R[-1].lpf = self.Settings.dlpf
        
        stop = False
        
        for i in range(self.Settings.nmax):
            if stop: break
            if self.Settings.log > 1: print('\nstart of Increment', i+1)
            
            # pre solve --> identify max. displacement component and direction
            if i == 0:
                dVpre = np.linalg.solve(self.jacobian(self.Results.R[-1].Ured),
                                        self.Results.R[-1].Vred[-1]*f0red-g(self.Results.R[-1].Vred)[:-1])
                dVpre_norm = dVpre/self.Settings.dVmax[:-1]
            else:
                self.Results.copy_increment()
            
            # extra loop, check if all components are valid!
            # satisfied if initial control component is equal to final control component
            j2check = 0
            success = False
            
            while self.Results.R[-1].j != j2check or success == False:
                j = np.argmax(abs(dVpre_norm))+1
                self.Results.R[-1].j = int(np.sign(dVpre_norm[j-1])*j)
                        
                if self.Settings.log > 2: print('  Component containing dV_max:', self.Results.R[-1].j)
                
                # Newton-Rhapson Iterations
                self.Results.R[-1].Vred, success = newton_rhapson(g,dgdV,
                                                         self.Results.R[-1].Vred,
                                                         nfev=self.Settings.nfev,
                                                         tol=self.Settings.tol,
                                                         verbose=self.Settings.log)
                #self.Results.R[-1].Vred = fsolve(g,self.Results.R[-1].Vred)
                #self.Results.R[-1].Vred[:-1] = self.Results.R[-1].Vred[:-1] + self.Results.R[-1].dVred[:-1]
    
                self.Results.R[-1].lpf = self.Results.R[-1].Vred[-1]
                
                # step-width control
                if success == False:
                    if self.Settings.log > 1: print("...recycling increment, NR-iterations failed.")
                    self.Settings.dVmax = self.Settings.dVmax/10

                    if self.Settings.log > 1: print('...current lpf fraction:', min(abs(self.Settings.dVmax/self.Settings.dVmax0)))
                    if min(abs(self.Settings.dVmax/self.Settings.dVmax0)) < self.Settings.mindV:
                        stop = True
                        if self.Settings.log > 1: print('------STOP------: Mininum fraction reached.')
                        break
                else:
                    if np.all(self.Settings.dVmax < self.Settings.dVmax0):
                        self.Settings.dVmax = self.Settings.dVmax*2
                
                # identify maximum displacement component
                if i > 0:
                    dVpre = self.Results.R[-1].Vred - self.Results.R[-2].Vred
                    dVpre_norm = dVpre/self.Settings.dVmax
                    j2 = np.argmax(abs(dVpre_norm))+1
                    j2check = int(np.sign(dVpre_norm[j2-1])*j2)
                    #if self.Results.R[-1].j == j2check:
                    #    break
                else:
                    j2check = self.Results.R[-1].j
                    
                # check if max. component changed or no NR-success
                # reset displacements to last converged ones
                if (self.Results.R[-1].j != j2check or success != True):
                    if i>1:
                        self.Results.R[-1].Vred = self.Results.R[-2].Vred
                    else:
                        self.Results.R[-1].Vred = self.Results.R[-1].Vred0
                    if self.Results.R[-1].j != j2check and self.Settings.log > 1: print("...recycling increment, switch control component: %d to %d" % (self.Results.R[-1].j, j2check))
                    
                #if i>0: print('Vred',self.Results.R[-1].Vred-self.Results.R[-2].Vred,self.Results.R[-1].Vred)


    def jacobian(self,Ured):
        "Stiffness Matrix"
        
        # In a future version this function should be implemented in Stiffness class part of the Model or Results
        # self.Stiffness(reduced=True)
        
        # it re-shapes stiffness matrix to
        # K(nnodes,nnodes,ndim,ndim) --> K(nnodes*ndim,nnodes*nim)
        # and returns a view on the reduced (active part of the) matrix
        # K(nnodes*ndim,nnodes*nim)[active DOF rows][:,active DOF columns]
        
        self.equilibrium(Ured,stage='K')

        # loop over nodes
#        for i in range(self.nnodes):
#            for j in range(self.nnodes):
#                if j==0:
#                    Kj = self.Results.R[-1].K[i,j]
#                else:
#                    Kj  = np.hstack((Kj,self.Results.R[-1].K[i,j]))
#            if i == 0:
#                K_out = Kj
#            else:
#                K_out = np.vstack((K_out,Kj))
                
        K_out = np.zeros((self.nnodes*self.ndim, self.nnodes*self.ndim))
        for a in range(self.nnodes):
            for b in range(self.nnodes):
                K_out[a*self.ndim:a*self.ndim+self.ndim,
                      b*self.ndim:b*self.ndim+self.ndim] = self.Results.R[-1].K[a,b]

        self.Results.R[-1].Kred = K_out[self.Results.R[-1].DOF1][:,self.Results.R[-1].DOF1]

        return self.Results.R[-1].Kred
            
        
    def equilibrium(self,Ured,stage='G'):

        # remove last entry in Vred to get only displacement DOFs
        if len(Ured) > self.ndof1:
            lpf = Ured[-1]
            Ured = Ured[:self.ndof1]
        else:
            lpf = self.Results.R[-1].lpf
            
        # copy input Ured to appropriate positions in full U-vector
        self.Results.R[-1].U.reshape(len(self.Results.R[-1].U.flatten(),))[self.Results.R[-1].DOF1] = Ured
        
        # loop over elements
        for e in self.Elements.labels:
            NA = self.Elements.NA(e) # begin node
            NE = self.Elements.NE(e) # end   node
            E = self.Elements.get_material(e) # young's modulus
            A = self.Elements.get_area(e) # section area
            #D = self.Elements.get_D(e)
            
            #Ured = self.Results.get_U(red=True)
            # displacements at begin and end nodes
            UA = self.Results.R[-1].U[np.where(self.Nodes.labels == NA)][0]
            UE = self.Results.R[-1].U[np.where(self.Nodes.labels == NE)][0]
            dU = UE-UA

            
            # undeformed coordinates of begin and end nodes
            XA = self.Nodes.coords[np.where(self.Nodes.labels == NA)][0]
            XE = self.Nodes.coords[np.where(self.Nodes.labels == NE)][0]
            
            dX = XE-XA
            dx = dX + dU
            
            # elemental normal vector in deformed configuration
            n = dx/np.linalg.norm(dx)
            
            # elemental length in undeformed and deformed configuration
            L = np.sqrt(np.dot(dX,dX))
            l = np.sqrt(np.dot(dx,dx))
            
            # stretch and nominal strain
            lam = l/L
            E11 = lam-1
            
            # normal force
            N = E*A*E11
            if stage == 'G':
                self.Results.R[-1].r.fill(0.0)
                # Equilibrium
                rA = self.Results.R[-1].r[np.where(self.Nodes.labels == NA)]
                rE = self.Results.R[-1].r[np.where(self.Nodes.labels == NE)]

                rA += [N*-n]
                rE += [N* n]

                self.Results.R[-1].stretch[np.where(self.Elements.labels == e)] = [lam]
                self.Results.R[-1].r[np.where(self.Nodes.labels == NA)] = rA
                self.Results.R[-1].r[np.where(self.Nodes.labels == NE)] = rE
            
            if stage == 'K':
                self.Results.R[-1].K.fill(0.0)
                #self.Results.R[-1].dlamdU.fill(0.0)
                # Tangent Stiffness
                J = np.eye(3)
                KTEE = E*A/L*np.outer(n,n) + N/l*(J-np.outer(n,n))
                #print('e', e, np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NE)[0][0])
                self.Results.R[-1].K[np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NA)[0][0]] +=  KTEE
                self.Results.R[-1].K[np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NE)[0][0]] += -KTEE
                self.Results.R[-1].K[np.where(self.Nodes.labels == NE)[0][0],np.where(self.Nodes.labels == NA)[0][0]] += -KTEE
                self.Results.R[-1].K[np.where(self.Nodes.labels == NE)[0][0],np.where(self.Nodes.labels == NE)[0][0]] +=  KTEE
                
                # dlam/dU
                #dlamdUE = n/L
                #self.Results.R[-1].dlamdU[np.where(self.Nodes.labels == NA)[0][0]] += -dlamdUE
                #self.Results.R[-1].dlamdU[np.where(self.Nodes.labels == NE)[0][0]] +=  dlamdUE
        
        if stage == 'G':
            self.Results.R[-1].g = -self.Results.R[-1].r.flatten() \
                                  + lpf * self.ExtForces.forces.flatten()
            return self.Results.R[-1].g[self.Results.R[-1].DOF1]
        else:
            return
    
    def plt_nodes(self,config='undeformed'):
        if config == 'undeformed':
            plot_nodes(self.Nodes.coords,color='C7')
        else:
            plot_nodes(self.Nodes.coords+self.Results.U,color='C0')
        
    def plt_elements(self,config='undeformed'):
        if config == 'undeformed':
            plot_elems(self.Elements.conns,self.Nodes.coords,color='C7')
        else:
            plot_elems(self.Elements.conns,self.Nodes.coords+self.Results.U,color='C0')
        
    def plt_extforces(self,config='undeformed'):
        if config == 'undeformed':
            plot_force(self.ExtForces.forces,self.Nodes.coords)
        else:
            plot_force(self.ExtForces.forces,self.Nodes.coords+self.Results.U)
            
    def plot_model(self,config='both',view='xz',contour=None,lim_scale=1.2,force_scale=0.5,inc=-1):
        con = None
        plt.figure()
        if contour == 'stretch':
            con = contour, self.Results.R[inc].stretch[:,0], [0.8,1.2]
        if 'undeformed' in config:
            fig,ax = plot_nodes(self.Nodes.coords,color='C7',view=view)
            fig,ax = plot_elems(self.Elements.conns,self.Nodes.coords,fig,ax,
                       color='C7',view=view,lim_scale=lim_scale)
        if 'deformed' in config:
            fig,ax = plot_nodes(self.Nodes.coords+self.Results.R[inc].U,fig,ax,color='C0',view=view)
            fig,ax = plot_elems(self.Elements.conns,self.Nodes.coords+self.Results.R[inc].U,
                       fig,ax,color='C0',view=view,contour=con,lim_scale=lim_scale)
            fig,ax = plot_force(self.Results.R[inc].lpf*self.ExtForces.forces,
                       self.Nodes.coords+self.Results.R[inc].U,
                       fig,ax,view=view,
                       scale=force_scale)
        if 'both' in config:
            fig,ax = plot_nodes(self.Nodes.coords,color='C7',view=view)
            fig,ax = plot_elems(self.Elements.conns,self.Nodes.coords,fig,ax,color='C7',view=view)
            fig,ax = plot_nodes(self.Nodes.coords+self.Results.R[inc].U,fig,ax,color='C0',view=view)
            fig,ax = plot_elems(self.Elements.conns,self.Nodes.coords+self.Results.R[inc].U,
                       fig,ax,color='C0',view=view,contour=con,lim_scale=lim_scale)
            fig,ax = plot_force(self.Results.R[inc].lpf*self.ExtForces.forces,
                       self.Nodes.coords+self.Results.R[inc].U,
                       fig,ax,view=view,
                       scale=force_scale)
        
        if view=='3d':
            ax.set_title('INCREMENT: '+str(inc)+', '+plt.gca().yaxis.get_label().get_text())
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
        else:
            plt.title('INCREMENT: '+str(inc)+', '+plt.gca().yaxis.get_label().get_text())
            plt.xlabel(view[0])
            plt.ylabel(view[1])

           #plot_force(self.ExtForces.forces,self.Nodes.coords)
           
    def plot_history(self, nodes=[1, 1], increments=None, X='Displacement X', Y='LPF'):
        # loop over increments
        xx = [0]
        yy = [0]
        dir_dict = {'X': 0, 'Y': 1, 'Z': 2}
        
        for R in self.Results.R:
            if 'Displacement' in X:
                x = R.U[np.where(self.Nodes.labels == nodes[0])][0][dir_dict[X[-1]]]
            elif 'LPF' in X:
                x = R.lpf
            else:
                x = R.r[np.where(self.Nodes.labels == nodes[0])][0][dir_dict[X[-1]]]
                
            if 'Displacement' in Y:
                y = R.U[np.where(self.Nodes.labels == nodes[1])][0][dir_dict[Y[-1]]]
            elif 'LPF' in Y:
                y = R.lpf
            else:
                y = R.r[np.where(self.Nodes.labels == nodes[1])][0][dir_dict[Y[-1]]]
            xx.append(x)
            yy.append(y)
        
        plt.figure()
        plot_hist(xx,yy,nodes[0],X,Y)
        #print(np.array(xx),np.array(yy))
        return
        