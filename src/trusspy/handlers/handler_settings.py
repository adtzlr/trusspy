# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


class SettingsHandler:
    def __init__(self, ndim=3, lpf=0.02, dlpf=0.02, du=0.02, log=2):
        self.ndim = ndim

        self.incs = 50

        self.stepcontrol = False
        self.maxfac = 10
        self.minfac = 1e-6
        self.increase = 0.5
        self.reduce = 8

        self.dxtol = 1.000001

        self.ftol = 8
        self.xtol = 8

        self.cycl = 4
        self.nfev = 8

        self.lpf = lpf

        self.dlpf = dlpf
        self.du = du

        # self.xlimit = (0,1.0)
        self.xlimit = (0, np.inf)

        self.log = log

        self.j0 = None
        self.j_pre = True
        self.j_fixed = False

        self.nstatev = 0

        self.nsteps = 1
