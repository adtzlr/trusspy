# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


class Node:
    """Node class.

    Attributes
    ----------
    label : int
        Node ID number
    coord : ndarray
        List of node coordinates: ``[X, Y, Z]``

    """

    def __init__(self, label, coord):
        """Node class.

        Parameters
        ----------
        label : int
            Node ID number
        coord : array_like
            List of node coordinates: ``[X, Y, Z]``

        """

        self.label = label
        self.coord = np.array(coord)
