# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:08:10 2018

@author: adutz

    TrussPy - Object Oriented Truss Solver for Python
    Copyright (C) 2018  Andreas Dutzler

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import copy

# Numpy and Pandas
import numpy as np
import pandas as pd

# Manager Classes
from trusspy.managers.manager_settings import SettingsManager
from trusspy.managers.manager_node import NodeManager
from trusspy.managers.manager_element import ElementManager
from trusspy.managers.manager_boundary import BoundaryManager  
from trusspy.managers.manager_extforce import ExternalForceManager
from trusspy.managers.manager_result import ResultManager

#from scipy.optimize import fsolve

# Material Definition
from trusspy.materials.material_definition import umat_el, umat_elplast_iso

# Element Definition
from trusspy.elements.element_definition import truss

# Solver and Tools
from trusspy.solvers.trusspy_solvers import path_tracing
from trusspy.tools.plot_utilities import (p_nodes,p_elements,p_extforces,
                                          p_model,p_movie,p_history)

class Model:
    "Create Model Class with Nodes, Elements, Boundaries, etc."
    def __init__(self,file=None,log=2,logfile=True):
        self.stdout = sys.stdout
        self.file = file
        self.logfile = logfile
        if file is None: self.logfile = False
        
        if self.file is not None:
            logfile_name = '.'.join(self.file.split('.')[:-1])
        else:
            logfile_name = 'analysis'
            self.logfile = False
        if self.logfile: sys.stdout = open(logfile_name+'.log', 'w')
            
            
        print("""
         _____                  ______      
        |_   _|                 | ___ \     
          | |_ __ _   _ ___ ___ | |_/ /   _ 
          | | '__| | | / __/ __||  __/ | | |
          | | |  | |_| \__ \__ \| |  | |_| |
          \_/_|   \__,_|___/___/\_|   \__, |
                                       __/ |
                                      |___/ 
        
        TrussPy - Object Oriented Truss Solver for Python
                  SNAPSHOT-20180802

        Author: Dutzler A.
                Graz University of Technology, 2018
                
        TrussPy  Copyright (C) 2018  Andreas Dutzler
        This program comes with ABSOLUTELY NO WARRANTY; 
        for details type `trusspy.show_w()'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `trusspy.show_c()' for details.
        """)

        if log > 1: print('')
        if log > 1: print('Initialize Model...')
        if log > 1: print('-'*88)
        if log > 1: print(' loading Managers...')
        
        self.Nodes = NodeManager()
        self.Elements = ElementManager()
        self.Boundaries = BoundaryManager()
        self.ExtForces = ExternalForceManager()
        self.Settings = SettingsManager()
        self.Results = ResultManager()
        
        if log > 1: print(' ...finished.')
        if log > 1: print('-'*88+'\n')
        
        if file is not None:
            if log > 1: print(' loading INPUT-File: "'+file+'"')
            Nodes = pd.read_excel(file,sheet_name="Nodes",skiprows=2).as_matrix()[:,:4].astype(float)
            Elements = pd.read_excel(file,sheet_name="Elements",skiprows=2).as_matrix()[:,:10].astype(float)
            Material = pd.read_excel(file,sheet_name="Material",skiprows=2).as_matrix()[:,:10].astype(float)
            Geometry = pd.read_excel(file,sheet_name="Geometry",skiprows=2).as_matrix()[:,:10].astype(float)
            ExtForces = pd.read_excel(file,sheet_name="ExternalForces",skiprows=2).as_matrix()[:,:1+5*3].astype(float)
            Boundary_U = pd.read_excel(file,sheet_name="BoundaryU",skiprows=2).as_matrix()[:,:4].astype(float)
            Boundary_T = pd.read_excel(file,sheet_name="BoundaryT",skiprows=2).as_matrix()[:,:2].astype(float)
            if log > 1: print(' ...successful.\n')
            
            if log > 1: print(' Converting Data...')
            self.Nodes.add_node_matrix(Nodes)
            self.Elements.add_element_matrix(Elements,Material,Geometry,Boundary_T)
            self.ExtForces.add_force_matrix(ExtForces)
            self.Boundaries.add_bound_U_matrix(Boundary_U)

            if log > 1: print(' ...Import finised.\n')
            if log > 1: print('-'*88)
    
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
            print('-'*88)
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
            
        # init results, add empty increment
        self.Results.add_increment()
        self.Results.build_result(self.nnodes,self.nelems,self.ndim,
                                  self.nproDOF0,self.nproDOF1,
                                  self.Settings.nstatev)
            
    def run(self):
        
        if self.Settings.log > 1: 
            print(' ')
            print('Run Simulation...')
            print('-'*88)
            
        if self.Settings.log > 1:
            print('\nSettings summary:')
            print('-----------------\n')
            print('Maximum increments                    "incs":', self.Settings.incs)
            print('Maximum increment recycles            "cycl":', self.Settings.cycl)
            print('Maximum Newton-Rhapson iterations     "nfev":', self.Settings.nfev)
            print('Maximum incremental displacement        "du":', self.Settings.du)
            print('Maximum incremental LPF               "dlpf":', self.Settings.dlpf)
            print('Initial control component               "j0":', 'LPF' if self.Settings.j0==None else self.Settings.j0)
            print('Maximum incremental overshoot        "dxtol":', self.Settings.dxtol)
            print('Tolerance for x                       "xtol":', self.Settings.xtol)
            print('Tolerance for f                       "ftol":', self.Settings.ftol)
            
            print('Adaptive control for stepwidth "stepcontrol":', self.Settings.stepcontrol)
            if self.Settings.stepcontrol:
                print('+ Minimum step size factor          "minfac":', self.Settings.minfac)
                print('+ Maximum step size factor          "maxfac":', self.Settings.maxfac)
                print('+ Reduce step size factor           "reduce":', 1/self.Settings.reduce)
                print('+ Increase step size factor       "increase":', self.Settings.increase)
            print('')

        # stiffness matrix, extended to nDOF+1
        def dgdV(Vred,V0red,j,Vmax,statev_write=False):
            
            # copy active control component to current result
            self.Results.R[-1].j = j
            
            # qc ... control equation
            qc = np.zeros(self.ndof1+1)
            qc[abs(j)-1] = 1

            # f0red ... external force vector f0 with active DOF
            #           reshaped to column-vector
            
            # modified stiffness
            #
            #          | KT       f0red |
            # KT_mod = | qcU  qc_lambda |
            
            
            self.Results.R[-1].Kmod = np.vstack((np.hstack((self.stiffness(Vred[:-1]),
                                                 -self.Results.R[-1].f0red)),qc))
            
            return self.Results.R[-1].Kmod
        
        # equilibrium function, extended to nDOF+1
        def g(Vred,V0red,j,Vmax,statev_write=False):
            # copy active control component to current result
            self.Results.R[-1].j = j
            
            # negative sign for default newton-rhapson function
            return np.append(-self.equilibrium(Vred,V0red,statev_write=statev_write),
                             Vred[abs(j)-1]-Vmax)
            
            
        
        
        # reduced modified displacement vector to active DOF and LPF
        self.Results.R[-1].Vred = np.append(self.Results.R[-1].Ured, 0)
        self.Results.R[-1].lpf = 0
        
        # init LPF
        # self.Settings.lpf = self.Settings.dlpf
        #self.Results.R[-1].lpf = self.Settings.dlpf
        
        for step in range(self.Settings.nsteps):
            if self.Settings.log > 0: print('\n--------------------- START OF STEP     ', step+1,'---------------------------------------------')
            # get reduced external force vector
            #f0red = self.ExtForces.forces[:,3*(step):3*(step+1)].flatten()[self.Results.R[-1].DOF1]
            #self.Results.R[-1].f0red = f0red.reshape(len(f0red),1)
            self.Results.R[-1].ExtForces = copy.deepcopy(self.ExtForces)
            
            f0_const = np.zeros_like(self.ExtForces.forces[:,3*(step):3*(step+1)])
            for s in range(step):
                f0_const += self.Results.step_lpf_end[s]*self.ExtForces.forces[:,3*(s):3*(s+1)]
            self.Results.R[-1].ExtForces.forces = f0_const + self.ExtForces.forces[:,3*(step):3*(step+1)]
            f0red = self.Results.R[-1].ExtForces.forces.flatten()[self.Results.R[-1].DOF1]
            self.Results.R[-1].f0red = f0red.reshape(len(f0red),1)
            
            
            res_V = path_tracing(g,dgdV, self.Results.R[-1].Vred,
                             dxmax=[self.Settings.du,self.Settings.dlpf],
                             j=self.Settings.j0,
                             incs=self.Settings.incs,
                             nfev=self.Settings.nfev,
                             cycl=self.Settings.cycl,
                             ftol=10**-self.Settings.ftol,
                             xtol=10**-self.Settings.xtol,
                             stepcontrol=self.Settings.stepcontrol,
                             maxfac=self.Settings.maxfac,
                             minfac=self.Settings.minfac,
                             reduce=self.Settings.reduce,
                             increase=self.Settings.increase,
                             dxtol=self.Settings.dxtol,
                             verbose=self.Settings.log)
            
            for i,r_V in enumerate(res_V[1:]):
                self.Results.R[-1].Vred = r_V
                self.Results.R[-1].U.reshape(len(self.Results.R[-1].U.flatten(),))[self.Results.R[-1].DOF1] = r_V[:-1]
                self.Results.R[-1].lpf = r_V[-1]
                self.Results.copy_increment()
            
            # append last lpf value
            self.Results.step_lpf_end.append(self.Results.R[-1].lpf)
            if step+1 < self.Settings.nsteps:
                self.Results.R[-1].Vred[-1] = 0.0
                self.Results.R[-1].lpf = 0.0
            else:
                self.Results.remove_last_increment()
                
            if self.Settings.log > 0: print('\n----------------------- END OF STEP     ', step+1,'---------------------------------------------')
            
        sys.stdout = self.stdout
        

    def stiffness(self,Ured):
        "Stiffness Matrix"
        
        # In a future version this function should be implemented in Stiffness class part of the Model or Results
        # self.Stiffness(reduced=True)
        
        # it re-shapes stiffness matrix to
        # K(nnodes,nnodes,ndim,ndim) --> K(nnodes*ndim,nnodes*nim)
        # and returns a view on the reduced (active part of the) matrix
        # K(nnodes*ndim,nnodes*nim)[active DOF rows][:,active DOF columns]
        
        # generate stiffness
        self.equilibrium(Ured,Ured,stage='K')
        
        # init re-shaped output stiffness matrix
        K_out = np.zeros((self.nnodes*self.ndim, self.nnodes*self.ndim))

        # loop over nodes to reshape K
        for a in range(self.nnodes):
            for b in range(self.nnodes):
                K_out[a*self.ndim:a*self.ndim+self.ndim,
                      b*self.ndim:b*self.ndim+self.ndim] = self.Results.R[-1].K[a,b]

        # select only active DOF1
        self.Results.R[-1].Kred = K_out[self.Results.R[-1].DOF1][:,self.Results.R[-1].DOF1]
        
        return self.Results.R[-1].Kred
            
        
    def equilibrium(self,Ured,U0red,stage='G',statev_write=False):

        # remove last entry in Vred to get only displacement DOFs
        if len(Ured) > self.ndof1:
            lpf   =  Ured[-1]
            lpf0  = U0red[-1]
            Ured  =  Ured[:self.ndof1]
            U0red = U0red[:self.ndof1]
        else:
            lpf = self.Results.R[-1].lpf
            
        if stage=='G':
            self.Results.R[-1].r.fill(0.0)
        else: #stage=='K'
            self.Results.R[-1].K.fill(0.0)
            
            
        # copy input Ured to appropriate positions in full U-vector
        self.Results.R[-1].U.reshape(len(self.Results.R[-1].U.flatten(),))[self.Results.R[-1].DOF1] = Ured
        self.Results.R[-1].U0.reshape(len(self.Results.R[-1].U0.flatten(),))[self.Results.R[-1].DOF1] = U0red
        
        # loop over elements
        for e in self.Elements.labels:
            nodes = self.Elements.get_nodes(e) # connected nodes
            
            mat_prop = self.Elements.get_material_properties(e)  # material parameter
            geo_prop = self.Elements.get_geometric_properties(e) # geometric parameter
            
            # undeformed coordinates of begin and end nodes
            Xnodes = np.zeros((len(nodes),3))
            for n,node in enumerate(nodes):
                Xnodes[n] = self.Nodes.coords[np.where(self.Nodes.labels == node)][0]
            
            # displacements at begin and end nodes
            Unodes = np.zeros((len(nodes),3))
            for n,node in enumerate(nodes):
                Unodes[n] = self.Results.R[-1].U[np.where(self.Nodes.labels == node)][0]
            
            # initial displacements at begin and end nodes
            U0nodes = np.zeros((len(nodes),3))
            for n,node in enumerate(nodes):
                U0nodes[n] = self.Results.R[-1].U0[np.where(self.Nodes.labels == node)][0]
                
            # RESOLVE PROBLEM IN STATEV UPDATE
            if self.Settings.nstatev > 0:
                state_v = self.Results.R[-1].state_v.copy()
            else:
                state_v = None

            # internal forces at begin and end nodes
            rnodes = np.zeros((len(nodes),3))
            for n,node in enumerate(nodes):
                rnodes[n] = self.Results.R[-1].r[np.where(self.Nodes.labels == node)][0]
                
            mat_type = self.Elements.get_material_type(e)
            #elem_type = self.Elements.get_element_type(e)
            
            if mat_type == 1:
                umat = umat_el
            elif mat_type == 2:
                umat = umat_elplast_iso
            elif mat_type == 3:
                umat = umat_elplast_kiniso
            
            self.Results.R[-1],state_v = truss(e,nodes,Xnodes,Unodes,U0nodes,rnodes,
                                       self.Nodes.labels,self.Elements.labels,stage,
                                       state_v,mat_prop,geo_prop,umat,
                                       self.Results.R[-1])
            if statev_write and self.Settings.nstatev > 0:
                #print('write state-variable for element', int(e), state_v[0])
                self.Results.R[-1].state_v = state_v

        if stage == 'G':
            self.Results.R[-1].g = -self.Results.R[-1].r.flatten() \
                                  + lpf * self.Results.R[-1].ExtForces.forces.flatten()
            return self.Results.R[-1].g[self.Results.R[-1].DOF1]
        else:
            return
    
    # Plot Utilities from "trusspy/tools/plot_utitilies.py"
    def plt_nodes(self,config='undeformed'):
        p_nodes(self,config)
        
    def plt_elements(self,config='undeformed'):
        p_elements(self,config)

    def plt_extforces(self,config='undeformed'):
        p_extforces(self,config)

    def plot_model(self,config='both',view='xz',contour=None,lim_scale=1.2,force_scale=0.5,inc=-1):
        p_model(self,config,view,contour,lim_scale,force_scale,inc)
           
    def plot_movie(self,config='both',view='xz',contour=None,lim_scale=1.2,force_scale=0.5,incs='all'):
        p_movie(self,config,view,contour,lim_scale,force_scale,incs)
        
    def plot_history(self, nodes=[1, 1], increments=None, X='Displacement X', Y='LPF', fig=None, ax=None):
        fig, ax = p_history(self,nodes,increments,X,Y,fig,ax)
        return fig, ax

        