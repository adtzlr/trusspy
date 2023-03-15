# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np

from ..core.external_force import ExternalForce


class ExternalForceHandler:
    "Handler for External Forces"

    def __init__(self):
        self.nodes = None
        self.forces = None

    def __enter__(self):
        return self

    def __exit__(self, H_type, H_value, H_traceback):
        pass

    def add_force(self, F, *args, **kwargs):

        if "ExternalForce" not in str(type(F)):
            F = ExternalForce(F, *args, **kwargs)

        if self.nodes is None:
            self.nodes = np.array([F.node])
            self.forces = np.array([F.force])
        else:
            self.nodes = np.append(self.nodes, F.node)
            self.forces = np.vstack((self.forces, F.force))

    def del_force(self, label):
        idx = np.where(self.nodes == label)[0]
        self.nodes = np.delete(self.nodes, idx, axis=0)
        self.forces = np.delete(self.forces, idx, axis=0)

    def add_forces(self, FF):

        for F in FF:
            self.add_force(F)

    def add_force_matrix(self, FM):
        if self.nodes is None:
            self.nodes = np.array(FM[:, 0])
            self.forces = np.array(FM[:, 1 : 1 + 5 * 3])
        else:
            self.nodes = np.append(self.nodes, FM[:, 0])
            self.forces = np.vstack((self.forces, FM[:, 1 : 1 + 5 * 3]))
        self.forces[np.isnan(self.forces)] = 0

    def fix_forces(self, nodelist):
        # check for missing external forces --> set them all to zero

        # are nodelist entries in force-nodes?
        mask = np.isin(nodelist, self.nodes, invert=True)
        fix_nodes = nodelist[mask]  # nodes to fix
        comp = self.forces.shape[1]
        for n in fix_nodes:
            F = ExternalForce(n, np.zeros(comp))
            self.add_force(F)
        indices = np.argsort(self.nodes)
        self.nodes = self.nodes.take(indices)
        self.forces = self.forces.take(indices, axis=0)
