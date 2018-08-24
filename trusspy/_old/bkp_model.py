# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:08:10 2018

@author: adutz
"""

import numpy as np
import pandas as pd

from trusspy.tools.helper_functions2 import plot_nodes, plot_elems, plot_force

# Manager Classes
from trusspy.managers.manager_settings import SettingsManager
from trusspy.managers.manager_node import NodeManager
from trusspy.managers.manager_element import ElementManager
from trusspy.managers.manager_boundary import BoundaryManager  
from trusspy.managers.manager_extforce import ExternalForceManager
from trusspy.managers.manager_result import ResultManager

from scipy.optimize import fsolve,root
from trusspy.solvers.newton_rhapson import NRsolve,NRArcLengthsolve,nr_solve,newton_rhapson
#from scipy.optimize import root,minimize

class Model:
    "Create Model Class with Nodes, Elements, Boundaries, etc."
    def __init__(self,file=None,log=2):
        if log > 1: print('')
        if log > 1: print('Initialize Model...')
        if log > 1: print('---------------------------------------')
        if log > 1: print(' loading Managers...')
        
        self.Nodes = NodeManager()
        if log > 1: print(' NodeManager ... OK')
        
        self.Elements = ElementManager()
        if log > 1: print(' ElementManager ... OK')
        
        self.Boundaries = BoundaryManager()
        if log > 1: print(' BoundaryManager ... OK')
        
        self.ExtForces = ExternalForceManager()
        if log > 1: print(' ExternalForceManager ... OK')
        
        self.Settings = SettingsManager()
        if log > 1: print(' SettingsManager ... OK')
        
        self.Results = ResultManager()
        if log > 1: print(' ResultManager ... OK')
        
        if log > 1: print(' ...finished.')
        if log > 1: print('---------------------------------------\n')
        
        if file is not None:
            if log > 1: print(' loading INPUT-File: "'+file+'"')
            if log > 1: print(' loading Nodes...')
            Nodes = pd.read_excel(file,sheet_name="Nodes",skiprows=2).as_matrix()[:,:4].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' loading Elements...')
            Elements = pd.read_excel(file,sheet_name="Elements",skiprows=2).as_matrix()[:,:6].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' loading External Forces...')
            ExtForces = pd.read_excel(file,sheet_name="ExternalForces",skiprows=2).as_matrix()[:,:4].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' loading Boundaries in U...')
            Boundary_U = pd.read_excel(file,sheet_name="BoundaryU",skiprows=2).as_matrix()[:,:4].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' loading Boundaries in T...')
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
        
        # node properties: active=free=1/inactive=fixed=0 DOF
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
        
        # initialize results
        self.Results.build(self.nnodes,self.nelems,self.ndim,
                           self.nproDOF0,self.nproDOF1)
        
        self.Settings.dVmax = np.ones(self.ndof1)*self.Settings.du
        self.Settings.dVmax = np.append(self.Settings.dVmax, self.Settings.dlpf)
        
        f0red = self.ExtForces.forces.flatten()[self.Results.DOF1]
        self.Results.f0red = f0red.reshape(len(f0red),1)
        
        self.Results.j = 1
        
        # jacobian, extended to nDOF+1
        def dgdV(Vred):
            # K"c"ontrol "v"ertical extension, "h"orizontal extension
            
            # qc ... control equation
            qc = np.zeros(self.ndof1+1)
            qc[abs(self.Results.j)-1] = np.sign(self.Results.j)
            
            # f0red ... external force vector f0 with active DOF
            # reshaped to column-vector
            
            # modified stiffness
            return np.vstack((np.hstack((self.jacobian(Vred[:-1]),-self.Results.f0red)),qc))
        
        # equilibrium function, extended to nDOF+1
        def g(Vred):
            self.Settings.lpf = Vred[-1]
            return np.append(self.equilibrium(Vred), self.Settings.dVmax[abs(self.Results.j)-1])
        
        # reduced displacement vector to active DOF
        self.Results.Vred = np.append(self.Results.Ured, self.Settings.dlpf)
        
        # init LPF
        self.Settings.lpf = self.Settings.dlpf
        
        for i in range(self.Settings.nmax):
            print('Increment', i)
            # pre solve --> identify max. displacement component and direction
            dVpre = np.linalg.solve(self.jacobian(self.Results.Ured),self.Results.Vred[-1]*f0red+g(self.Results.Vred)[:-1])
            dVpre_norm = dVpre/self.Settings.dVmax[:-1]
            
            j = np.argmax(abs(dVpre_norm))+1
            self.Results.j = int(np.sign(dVpre_norm[j-1])*j)
            
            # Newton-Rhapson
            (self.Results.Vredi,
            self.Results.infodict, 
            self.Results.ier,
            self.Results.mesg) = newton_rhapson(g,dgdV,self.Results.Vred, nfev=8,tol=12)
            
            self.Results.Vred = self.Results.Vred + self.Results.Vredi
            
        
    def run_bkp(self):
        if self.Settings.log > 1: 
            print(' ')
            print('Run Simulation...')
            print('---------------------------------------')
        #r = np.zeros((self.nnodes,self.ndim)).flatten()
        #u = np.zeros((self.nnodes,self.ndim)).flatten()
        
        #ured = u[np.where(self.nproBC.flatten() == 1)]
        
        self.Results.build(self.nnodes,self.nelems,self.ndim,
                           self.nproDOF0,self.nproDOF1)

        Ured = self.Results.Ured
        
        #----------------------------------------------------------------------
        # Arc Length Method
        if self.Settings.arc_length:
            def jac(Ured,j):
                # K"c"ontrol "v"ertical extension, "h"orizontal extension
                qc = np.zeros(self.ndof1+1)
                qc[abs(j)] = np.sign(j)
                
                Kch = -self.ExtForces.forces.flatten()[self.Results.DOF1]
                Kch = Kch.reshape(len(Kch),1)
                
                return np.vstack((np.hstack((self.jacobian(Ured),Kch)),qc))
            
            def equ(Ured):
                self.Settings.lpf = Ured[-1]
                return np.append(self.equilibrium(Ured), self.Settings.du)

            Vred = np.append(Ured, 0.0)
            f0 = self.ExtForces.forces.flatten()[self.Results.DOF1]
            
            i = 0
            self.Settings.lpf0 = self.Settings.dlpf
            lpfi = self.Settings.lpf0

            while i < 10 :#and lpfi < self.Settings.lpf:
                
                if self.Settings.solver == 'SciPy':
                    Vred,self.Results.infodict,self.Results.ier,self.Results.mesg = fsolve(equ,Vred,fprime=None,full_output=True)
                else: #'NewtonRhapson'
                    Vred,self.Results.infodict,self.Results.ier,self.Results.mesg = NRArcLengthsolve(equ,Vred,
                                                                                        jac,
                                                                                        lpfi,
                                                                                        f0,
                                                                                        log=self.Settings.log)
        
                Ured = Vred[:-1]
                self.Settings.lpf = Vred[-1]
                
                if self.Settings.log > 1: print(' Run incremenet:', i+1)
                
                self.Results.U.reshape(len(self.Results.U.flatten(),))[self.Results.DOF1] = Ured
                
                #lpfi = self.Settings.lpf0 + self.Settings.dlpf
                lpfi = self.Settings.lpf
            
                if self.Settings.log > 2: 
                    print('\n Increment:', i+1)
                    print(' n Function Evaluations: ', self.Results.infodict['nfev'])
                    if self.Settings.solver != 'SciPy': print(' n DOFmax: ', self.Results.infodict['DOFmax'], self.Results.infodict['DOFmax value'])
                    print(' Message: ', self.Results.mesg)
                    print(' LPF: ', lpfi)
                    print(' Converged: ',self.Results.ier)
                    print(' final Displacements: \n', self.Results.U, '\n')
                    
                    #print(' jacobian', self.jacobian(Ured))
                if self.Results.ier != 1:
                    break
                i=i+1
            
        else:
        #----------------------------------------------------------------------
        # Newton Method with fixed load increments
        
            # loop over increments
            if self.Settings.dlpf == 0:
                lpf_list = np.linspace(0,self.Settings.lpf,self.Settings.inc+1)[1:]
            else:
                lpf_list = np.append(np.arange(0,self.Settings.lpf,self.Settings.dlpf)[1:],self.Settings.lpf)
            
            for i,lpfi in enumerate(lpf_list):
                
                self.Settings.lpf = lpfi
                if i==0:
                    self.Settings.lpf0 = lpfi
                self.Settings.dlpf = lpfi-self.Settings.lpf0
                
                self.Settings.dlpf = 0.0

                #Ured = Ured
                jac = self.jacobian
                equ = self.equilibrium
                Vred = Ured
                f0 = self.ExtForces.forces.flatten()[self.Results.DOF1]
                
                if self.Settings.solver == 'SciPy':
                    Vred,self.Results.infodict,self.Results.ier,self.Results.mesg = fsolve(equ,Vred,fprime=None,full_output=True)
                else: #'NewtonRhapson'
                    Vred,self.Results.infodict,self.Results.ier,self.Results.mesg = NRsolve(equ,Vred,
                                                                                        jac,
                                                                                        self.Settings.dlpf,
                                                                                        f0,
                                                                                        log=self.Settings.log)
    
                if self.Settings.log > 1: print(' Run incremenet:', i+1)
                
                Ured = Vred
                    
                self.Results.U.reshape(len(self.Results.U.flatten(),))[self.Results.DOF1] = Ured
                
                self.Settings.lpf0 = lpfi
            
                if self.Settings.log > 2: 
                    print('\n Increment:', i+1)
                    print(' n Function Evaluations: ', self.Results.infodict['nfev'])
                    print(' Message: ', self.Results.mesg)
                    print(' LPF: ', lpfi)
                    print(' Converged: ',self.Results.ier)
                    print(' final Displacements: \n', self.Results.U, '\n')
                    
                    #print(' jacobian', self.jacobian(Ured))
                if self.Results.ier != 1:
                    break
            
    def jacobian(self,Ured):
        "Stiffness Matrix"
        
        # In a future version this function should be implemented in Stiffness class part of the Model or Results
        # self.Stiffness(reduced=True)
        
        # it re-shapes stiffness matrix to
        # K(nnodes,nnodes,ndim,ndim) --> K(nnodes*ndim,nnodes*nim)
        # and returns a view on the reduced (active part of the) matrix
        # K(nnodes*ndim,nnodes*nim)[active DOF rows][:,active DOF columns]
        
        #if np.allclose(Ured,0):
        #    Ured = 1.e-8
        
        self.equilibrium(Ured,stage='K')

        for i in range(self.nnodes):
            for j in range(self.nnodes):
                if j==0:
                    Kj = self.Results.K[i,j]
                else:
                    Kj  = np.hstack((Kj,self.Results.K[i,j]))
            if i == 0:
                K_out = Kj
            else:
                K_out = np.vstack((K_out,Kj))
        #print('jac',K_out)
        self.Results.Kred = K_out[self.Results.DOF1][:,self.Results.DOF1]
        #print('jac',K_out[self.Results.DOF1][:,self.Results.DOF1])
        return K_out[self.Results.DOF1][:,self.Results.DOF1]
                
        #return self.Results.K.reshape(self.nnodes*self.ndim,
        #                               self.nnodes*self.ndim)\
        #                              [self.Results.DOF1][:,self.Results.DOF1]#\
               #+ np.outer(self.ExtForces.forces.flatten()[self.Results.DOF1],
               #           self.Results.dlamdU.flatten()[self.Results.DOF1])
            
        
    def equilibrium(self,Ured,stage='G'):
        
        #if self.Settings.arc_length:
        #    Ured = Ured[:-1]
        if len(Ured) > self.ndof1:
            Ured = Ured[:self.ndof1]
        #print('nDOF1',self.ndof1,'Ured',Ured,'stage',stage)
            
        self.Results.U.reshape(len(self.Results.U.flatten(),))[self.Results.DOF1] = Ured
        if stage == 'G':
            self.Results.r.fill(0.0)
        if stage == 'K':
            self.Results.K.fill(0.0)
            self.Results.dlamdU.fill(0.0)
        
        for e in self.Elements.labels:
            NA = self.Elements.NA(e)
            NE = self.Elements.NE(e)
            E = self.Elements.get_material(e)
            A = self.Elements.get_area(e)
            #D = self.Elements.get_D(e)
            
            #Ured = self.Results.get_U(red=True)
            UA = self.Results.U[np.where(self.Nodes.labels == NA)][0]
            UE = self.Results.U[np.where(self.Nodes.labels == NE)][0]
            dU = UE-UA
            
            XA = self.Nodes.coords[np.where(self.Nodes.labels == NA)][0]
            XE = self.Nodes.coords[np.where(self.Nodes.labels == NE)][0]
            
            dX = XE-XA
            dx = dX + dU
            
            n = dx/np.linalg.norm(dx)
            
            L = np.sqrt(np.dot(dX,dX))
            l = np.sqrt(np.dot(dx,dx))
            
            lam = l/L
            E11 = lam-1
            
            N = E*A*E11
            if stage == 'G':
                # Equilibrium
                rA = self.Results.r[np.where(self.Nodes.labels == NA)]
                rE = self.Results.r[np.where(self.Nodes.labels == NE)]
    
                rA += [N*-n]
                rE += [N* n]
                self.Results.stretch[np.where(self.Elements.labels == e)] = [lam]
                self.Results.r[np.where(self.Nodes.labels == NA)] = rA
                self.Results.r[np.where(self.Nodes.labels == NE)] = rE
            
            if stage == 'K':
                # Tangent Stiffness
                J = np.eye(3)
                KTEE = (E*A/L*np.outer(n,n) + N/l*(J-np.outer(n,n)))
                #print('e', e, np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NE)[0][0])
                self.Results.K[np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NA)[0][0]] +=  KTEE
                self.Results.K[np.where(self.Nodes.labels == NA)[0][0],np.where(self.Nodes.labels == NE)[0][0]] += -KTEE
                self.Results.K[np.where(self.Nodes.labels == NE)[0][0],np.where(self.Nodes.labels == NA)[0][0]] += -KTEE
                self.Results.K[np.where(self.Nodes.labels == NE)[0][0],np.where(self.Nodes.labels == NE)[0][0]] +=  KTEE
                
                # dlam/dU
                dlamdUE = n/L
                self.Results.dlamdU[np.where(self.Nodes.labels == NA)[0][0]] += -dlamdUE
                self.Results.dlamdU[np.where(self.Nodes.labels == NE)[0][0]] +=  dlamdUE
        
        if stage == 'G':
            lpf = self.Settings.lpf
            self.Results.g = -self.Results.r.flatten() + lpf * self.ExtForces.forces.flatten()
        #print(' displ:', Ured, 'g:', self.Results.g[self.Results.DOF1])
        #print(Ured,self.Results.K,'\n')
        
        if stage == 'G':
            return self.Results.g[self.Results.DOF1]
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
            
    def plot_model(self,config='both',view='xz',contour=None,lim_scale=1.2,force_scale=0.5):
        con = None
        if contour == 'stretch':
            con = contour, self.Results.stretch[:,0]
        if 'undeformed' in config:
            plot_nodes(self.Nodes.coords,color='C7',view=view)
            plot_elems(self.Elements.conns,self.Nodes.coords,
                       color='C7',view=view,lim_scale=lim_scale)
        if 'deformed' in config:
            plot_nodes(self.Nodes.coords+self.Results.U,color='C0',view=view)
            plot_elems(self.Elements.conns,self.Nodes.coords+self.Results.U,
                       color='C0',view=view,contour=con,lim_scale=lim_scale)
            plot_force(self.ExtForces.forces,self.Nodes.coords+self.Results.U,view=view,scale=force_scale)
        if 'both' in config:
            plot_nodes(self.Nodes.coords,color='C7',view=view)
            plot_elems(self.Elements.conns,self.Nodes.coords,color='C7',view=view)
            plot_nodes(self.Nodes.coords+self.Results.U,color='C0',view=view)
            plot_elems(self.Elements.conns,self.Nodes.coords+self.Results.U,
                       color='C0',view=view,contour=con,lim_scale=lim_scale)
            plot_force(self.ExtForces.forces,self.Nodes.coords+self.Results.U,view=view,scale=force_scale)

           #plot_force(self.ExtForces.forces,self.Nodes.coords)
        