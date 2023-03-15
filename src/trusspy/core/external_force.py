# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


class ExternalForce:
    """External Force class.

    Attributes
    ----------
    node : int
        The node ID number,
    force : ndarray
        Array containing force components ``array([F1, F2, F3])``.

    """

    def __init__(self, node, force):
        """External Force class.

        Parameters
        ----------
        node : int
            The node ID number.
        force : array_like
            List of Force components ``[F1, F2, F3]``.

        """

        self.node = node
        self.force = np.array(force, dtype=float)
