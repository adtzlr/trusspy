# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np

from ..core.boundary import BoundaryU


class BoundaryHandler:
    "Handler for Boundary Conditions"

    def __init__(self):
        # Node-based displacement boundary condition
        self.Unodes = None

        # UValue:
        # 1=active    (free)  DOF
        # 0=inactive (locked) DOF
        self.Uvalues = None

        # NOT IMPLEMENTED
        # Element based thermal boundary condition
        self.Telements = None
        self.Tvalues = None

    def __enter__(self):
        return self

    def __exit__(self, H_type, H_value, H_traceback):
        pass

    def add_bound_U(self, B, *args, **kwargs):
        """add displacement boundary"""

        if "BoundaryU" not in str(type(B)):
            B = BoundaryU(B, *args, **kwargs)

        if self.Unodes is None:
            self.Unodes = np.array([B.node])
            self.Uvalues = np.array(B.values)
        else:
            self.Unodes = np.append(self.Unodes, B.node)
            self.Uvalues = np.vstack((self.Uvalues, B.values))

    def del_bound_U(self, label):
        """delete boundary U by label"""
        idx = np.where(self.Unodes == label)[0]
        self.Unodes = np.delete(self.Unodes, idx, axis=0)
        self.Uvalues = np.delete(self.Uvalues, idx, axis=0)

    def add_bounds_U(self, BB):
        """add list of displacement boundaries"""
        for B in BB:
            self.add_bound_U(B)

    def fix_bounds_U(self, nodelist):
        # check for undefined DOF --> set them all to free

        # are nodelist entries in Unodes?
        mask = np.isin(nodelist, self.Unodes, invert=True)
        fix_nodes = nodelist[mask]  # nodes to fix
        for n in fix_nodes:
            B = BoundaryU(n, (1, 1, 1))
            self.add_bound_U(B)
        indices = np.argsort(self.Unodes)
        self.Unodes = self.Unodes.take(indices)
        self.Uvalues = self.Uvalues.take(indices, axis=0)

    def add_bound_U_matrix(self, UM):
        # add matrix of displacement boundaries from input file
        if self.Unodes is None:
            self.Unodes = np.array(UM[:, 0])
            self.Uvalues = np.array(UM[:, 1:4])
        else:
            self.Unodes = np.append(self.Unodes, UM[:, 0])
            self.Uvalues = np.vstack((self.Uvalues, UM[:, 1:4]))
        self.Uvalues[np.isnan(self.Uvalues)] = 0

    def add_bound_T(self, B):
        # add thermal boundary
        if self.Tnodes is None:
            self.Tnodes = np.array([B.node])
            self.Tvalues = np.array(B.value)
        else:
            self.Tnodes = np.append(self.Tnodes, B.node)
            self.Tvalues = np.vstack((self.Tvalues, B.value))

    def add_bounds_T(self, BB):
        # add list of thermal boundaries
        for B in BB:
            self.add_bound_T(B)
