# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import copy

# import numpy as np
from ..core.analysis import Analysis


class ResultHandler:
    "Handler for Result Data"

    def __init__(self):
        self.R = []
        self.step_lpf_end = []

    def add_increment(self):
        "add single Result to ResultManager"
        self.R.append(Analysis())

    def copy_increment(self):
        "add single Result to ResultManager"
        self.R.append(copy.deepcopy(self.R[-1]))

    def remove_last_increment(self):
        "remove last Result from ResultManager"
        self.R.pop()

    def duplicate_first_increment(self):
        "duplicate first Result in ResultManager"
        self.R = [self.R[0]] + self.R

    def build_result(self, nnodes, nelems, ndim, DOF0, DOF1, nstatev):
        self.R[-1].build(nnodes, nelems, ndim, DOF0, DOF1, nstatev)

    def get_result(self, i):
        "get i-th result"
        return self.R[i]
