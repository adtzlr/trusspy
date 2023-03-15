# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


class BoundaryU:
    """Mechanical (displacement) node based boundary class.

    Parameter
    ---------
    node : int
        Node ID number
    values : array_like
        List of boundary components: `[U1, U2, U3]`.
        Set 1 for active (free) DOF and 0 for inactive (locked) DOF.

    Attributes
    ----------
    node : int
        Node ID number
    values : ndarray
        Array of boundary components: `array([U1, U2, U3])`.
        Set 1 for active (free) DOF and 0 for inactive (locked) DOF.

    """

    def __init__(self, node, values):
        self.node = node
        self.values = np.array(values)


class BoundaryT:
    """Thermal element based boundary class.

    Parameter
    ---------
    element : int
        Element ID number
    value : float
        Value of thermal load

    Attributes
    ----------
    element : int
        Element ID number
    value : float
        Value of thermal load
    """

    def __init__(self, element, value):
        self.element = element
        self.value = value
