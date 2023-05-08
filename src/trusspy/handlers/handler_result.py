# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import copy

import numpy as np
from ..core.analysis import Analysis


class ResultHandler:
    "Handler for Result Data"

    def __init__(self):
        self.R = []
        self.step_lpf_end = []

    def add_increment(self, analysis=None, extforces=None, lpf=None):
        "add single Result to ResultManager"

        if analysis is None:
            result = Analysis()
        else:
            result = copy.deepcopy(analysis)

            if extforces is not None:
                result.ExtForces = copy.deepcopy(extforces)
                result.ExtForces.forces_const = np.zeros_like(result.U)

        result.lpf = lpf

        # add the increment
        self.R.append(result)

    def copy_increment(self):
        "add single Result to ResultManager"
        self.R.append(copy.deepcopy(self.R[-1]))

    def remove_last_increment(self):
        "remove last Result from ResultManager"
        self.R.pop()

    def duplicate_first_increment(self):
        "duplicate first Result in ResultManager"
        self.R = [copy.deepcopy(self.R[0])] + self.R

    def build_result(self, nnodes, nelems, ndim, DOF0, DOF1, nstatev):
        self.R[-1].build(nnodes, nelems, ndim, DOF0, DOF1, nstatev)

    def get_result(self, i):
        "get i-th result"
        return self.R[i]
