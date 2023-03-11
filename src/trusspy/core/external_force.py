# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:49:08 2018

@author: adutz
"""

import numpy as np


class ExternalForce:
    """External Force class.

    Parameter
    ---------
    node : int
        Node ID number
    force : array_like
        List of Force components: `[F1, F2, F3]`

    Attributes
    ----------
    node : int
        Node ID number
    force : ndarray
        Array containing Force components `array([F1, F2, F3])`

    TODO's
    ------
    - add steps/stages by extending `force`
    """

    def __init__(self, node, force):
        self.node = node
        self.force = np.array(force, dtype=float)
