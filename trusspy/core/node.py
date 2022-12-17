# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:45:21 2018

@author: adutz
"""

import numpy as np


class Node:
    """Node class.

    Parameter
    ---------
    label : int
        Node ID number
    coord : array_like
        List of node coordinates: `[X, Y, Z]`

    Attributes
    ----------
    label : int
        Node ID number
    coord : ndarray
        List of node coordinates: `[X, Y, Z]`

    Todo
    ----
    - add undeformed/deformed coordinates (useful?)
    - copy deformed coordinates to result class at the end of each increment
    """

    def __init__(self, label, coord):
        self.label = label
        self.coord = np.array(coord)
