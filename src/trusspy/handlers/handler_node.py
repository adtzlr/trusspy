# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np

from ..core.node import Node


class NodeHandler:
    "Handler for Nodes"

    def __init__(self):
        self.labels = None
        self.coords = None

    def __enter__(self):
        return self

    def __exit__(self, H_type, H_value, H_traceback):
        pass

    def add_node(self, N, *args, **kwargs):

        # raw node
        if "Node" not in str(type(N)):
            N = Node(N, *args, **kwargs)

        if self.labels is None:
            self.labels = np.array([N.label])
            self.coords = np.array([N.coord])
        else:
            self.labels = np.append(self.labels, N.label)
            self.coords = np.vstack((self.coords, N.coord))

    def del_node(self, label):
        idx = np.where(self.labels == label)[0]
        self.labels = np.delete(self.labels, idx, axis=0)
        self.coords = np.delete(self.coords, idx, axis=0)

    def add_nodes(self, NN):
        for N in NN:
            self.add_node(N)

    def add_node_matrix(self, NM):
        if self.labels is None:
            self.labels = np.array(NM[:, 0])
            self.coords = np.array(NM[:, 1:4])
        else:
            self.labels = np.append(self.labels, NM[:, 0])
            self.coords = np.vstack((self.coords, NM[:, 1:4]))

    def fix_nodes(self):
        indices = np.argsort(self.labels)
        self.labels = self.labels.take(indices)
        self.coords = self.coords.take(indices, axis=0)
