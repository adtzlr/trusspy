# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


class Analysis:
    """Analysis class containing all data for one increment.

    Attributes
    ----------
    U : None
        placeholder for 2d-array with total displacement vector at the end of the inc.
        `U.shape = (nnodes, ndim)`. To get Ux,Uy,Uz of node i type: `U[i]`
    U0 : None
        placeholder for 2d-array with total displacement vector at the beginning of the
        inc. `U0.shape = (nnodes, ndim)`. To get U0x,U0y,U0z of node i type: `U0[i]`
    r : None
        placeholder for 2d-array with internal force vector
        `r.shape = (nnodes, ndim)`. To get rx,ry,rz of node i type: `r[i]`
    g : None
        placeholder for 2d-array with equilibrium vector
        `g.shape = (nnodes, ndim)`. To get gx,gy,gz of node i type: `g[i]`
    K : None
        placeholder for 4d-array with stiffness matrix
        `K.shape = (nnodes,nnodes,ndim,ndim)`. To get K with shape (ndim,ndim)
        between force of node i w.r.t. displacement of node j type K[i,j].
    stretch : None
        placeholder for 2d-array with stretch vector
        `stretch.shape = (nelems, 1)`. To get stretch of element i
        type: `stretch[i]`
    element_force : None
        placeholder for 2d-array with element force vector
        `element_force.shape = (nelems, 1)`. To get element_force of element i
        type: `element_force[i]`
    element_stress : None
        placeholder for 2d-array with element stress vector
        `element_stress.shape = (nelems, 1)`. To get element_stress of element i
        type: `element_stress[i]`
    element_stress0 : None
        placeholder for 2d-array with element stress vector at the beginning of the
        increment ``element_stress0.shape = (nelems, 1)``. To get element_stress0 of
        element ``i`` type: ``element_stress0[i]``.
    DOF0 : None
        placeholder for indices of inactive (locked) degree of freedoms
    DOF1 : None
        placeholder for indices of active (free) degree of freedoms
    Ured : None
        placeholder for reduced dispaclement vector
        (only active components of U)
    Vred : None
        placeholder for reduced dispaclement vector
        (only active components of V)
    state_v : None
        placeholder for state variable vector

    """

    def __init__(self):
        self.U = None
        self.U0 = None
        self.r = None
        self.g = None
        self.K = None

        self.stretch = None
        self.element_force = None
        self.element_stress0 = None
        self.element_stress = None

        self.DOF0 = None
        self.DOF1 = None

        self.Ured = None
        self.rred = None

        self.state_v = None

        self.dVmax = None

    def build(self, nnodes, nelems, ndim, DOF0, DOF1, nstatev=0):
        """Build/initialize analysis class with given dimensions regarding
        nodes and dimension.

        Parameter
        ---------
        nnodes : int
            Number of nodes
        nelems : int
            Number of elements
        ndim : int
            Dimension of analysis
        DOF0 : int
            indices of inactive (locked) degree of freedoms
            (generated with flattened degree of freedoms)
        DOF1 : int
            indices of active (free) degree of freedoms
            (generated with flattened degree of freedoms)

        Raises
        ------
        ValueError : Result is not empty and can't be built.
            Dimensions already set.

        """
        if self.U is None:
            self.step = 1
            self.U = np.zeros((nnodes, ndim))
            self.U0 = np.zeros((nnodes, ndim))
            self.r = np.zeros((nnodes, ndim))
            self.g = np.zeros((nnodes, ndim))
            self.K = np.zeros((nnodes, nnodes, ndim, ndim))

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
                self.state_v = None

        else:
            raise ValueError("Displacements or Residuals already loaded.")

    def get_U(self, flat=False, red=False):
        "get flattened/reduced set of displacement vector U"
        if flat:
            return self.U.flatten()
        elif red:
            return self.Ured
        else:
            return self.U

    def get_r(self, flat=False, red=False):
        "get flattened/reduced set of interal force vector r"
        if flat:
            return self.r.flatten()
        elif red:
            return self.rred
        else:
            return self.r
