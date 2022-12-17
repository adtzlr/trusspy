# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:20:27 2018

@author: adutz
"""

import numpy as np


class Result:
    """Result class.

    Attributes
    ----------
    U : ndarray
        2d-array with total displacement vector
        `U.shape = (nnodes, ndim)`. To get Ux,Uy,Uz of node i type: `U[i]`

    r : ndarray
        2d-array with internal force vector
        `r.shape = (nnodes, ndim)`. To get rx,ry,rz of node i type: `r[i]`

    g : ndarray
        2d-array with equilibrium vector
        `g.shape = (nnodes, ndim)`. To get gx,gy,gz of node i type: `g[i]`

    stretch : ndarray
        2d-array with stretch vector
        `stretch.shape = (nelems, 1)`. To get stretch of element i
        type: `stretch[i]`

    element_force : ndarray
        2d-array with element force vector
        `element_force.shape = (nelems, 1)`. To get element_force of element i
        type: `element_force[i]`

    K : ndarray
        4d-array with stiffness matrix
        `K.shape = (nnodes,nnodes,ndim,ndim)`. To get K with shape (ndim,ndim)
        between node i and node j type K[i,j].

    state_v : ndarray
        state variable vector



    Todo
    ----
    * simplify reduced set with DOF1 read/write options
    """

    def __init__(self):
        self.U = None
        self.r = None
        self.g = None
        self.stretch = None
        self.element_force = None
        self.K = None
        self.state_v = None

    def build(self, nnodes, nelems, ndim, DOF0, DOF1, nstatev=0):
        """Build/initialize result class with given dimensions.

        Parameter
        ---------
        nnodes : int
            Number of nodes
        nelems : int
            Number of elements
        ndim : int
            Dimension of analysis
        DOF0 : int
            indices of inactive degree of freedoms
            (generated with flattened degree of freedoms)
        DOF1 : int
            indices of active degree of freedoms
            (generated with flattened degree of freedoms)

        Raises
        ----------
        ValueError : Result is not empty and can't be built.
            Dimensions already set.

        Todo
        ----
        * simplify reduced slice read/write operations
        """
        if self.U is None:
            self.U = np.zeros((nnodes, ndim))
            self.U0 = np.zeros((nnodes, ndim))
            self.r = np.zeros((nnodes, ndim))
            self.g = np.zeros((nnodes, ndim))
            self.K = np.zeros((nnodes, nnodes, ndim, ndim))
            # self.dlamdU = np.zeros((nnodes,ndim))
            self.stretch = np.zeros((nelems, 1))
            self.element_force = np.zeros((nelems, 1))
            self.element_stress0 = np.zeros((nelems, 1))
            self.element_stress = np.zeros((nelems, 1))
            self.DOF0 = DOF0
            self.DOF1 = DOF1
            self.Ured = self.get_U(flat=True)[DOF1]
            self.rred = self.get_r(flat=True)[DOF1]
            if nstatev > 0:
                self.state_v = np.zeros((nelems, nstatev))

        else:
            raise ValueError("Displacements or Residuals already loaded.")

    def get_U(self, flat=False, red=False):
        if flat:
            return self.U.flatten()
        elif red:
            return self.Ured
        else:
            return self.U

    def get_r(self, flat=False, red=False):
        if flat:
            return self.r.flatten()
        elif red:
            return self.rred
        else:
            return self.r
