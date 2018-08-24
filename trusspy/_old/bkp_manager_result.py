# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:48:42 2018

@author: adutz
"""

import numpy as np

class ResultManager:
    "Manager for Result Data"
    def __init__(self):
        self.U = None
        self.r = None
        self.K = None
        self.dlamdU = None
        self.g = None
        self.stretch = None
        #self.nresUVW = None
        #self.eresL = None
        #self.ereslam = None
        #self.eresN = None
        #self.eres = None
        
    def build(self,nnodes,nelems,ndim,DOF0,DOF1):
        if self.U is None:
            self.U = np.zeros((nnodes,ndim))
            self.r = np.zeros((nnodes,ndim))
            self.K = np.zeros((nnodes,nnodes,ndim,ndim))
            self.dlamdU = np.zeros((nnodes,ndim))
            self.stretch = np.zeros((nelems,1))
            self.DOF0 = DOF0
            self.DOF1 = DOF1
            self.Ured = self.get_U(flat=True)[DOF1]
            self.rred = self.get_U(flat=True)[DOF1]

        else:
            raise ValueError('Displacements or Residuals already loaded.')
        
    def get_U(self,flat=False,red=False):
        if flat:
            return self.U.flatten()
        elif red:
            return self.Ured
        else:
            return self.U
        
    def get_r(self,flat=False,red=False):
        if flat:
            return self.r.flatten()
        elif red:
            return self.rred
        else:
            return self.r