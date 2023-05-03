# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


def umat_el(e, de, mat_prop, state_v):
    E = mat_prop[0]

    s = E * e
    dsde = E
    dsdt = 0

    return s, dsde, dsdt, state_v


def umat_elplast_iso(e, de, mat_prop, state_v):
    E = mat_prop[0]
    K = mat_prop[1]
    Sy = mat_prop[2]

    eps_pl_0 = state_v[1]

    # total strain at time t=t_n+1
    eps_1 = e

    # yield stress at time t=t_n
    if state_v[0] == 0:
        stress_yield_0 = Sy
    else:
        stress_yield_0 = state_v[0]

    # algorithm: isotropic hardening

    # trial state
    stress_trial = E * (eps_1 - eps_pl_0)
    eps_pl_trial = eps_pl_0
    f_trial = abs(stress_trial) - stress_yield_0

    if f_trial <= 0:
        # elastic strain increment
        stress_1 = stress_trial
        eps_pl_1 = eps_pl_trial
        dsde = E
        delta_gamma = 0.0
    else:
        # plastic strain increment
        delta_gamma = f_trial / (E + K)
        stress_1 = (1 - (delta_gamma * E) / abs(stress_trial)) * stress_trial
        eps_pl_1 = eps_pl_0 + delta_gamma * np.sign(stress_trial)
        dsde = E * K / (E + K)

    # output (update) stress
    s = stress_1

    # output (update) state variables
    stress_yield_1 = stress_yield_0 + K * delta_gamma
    state_v[0] = stress_yield_1
    state_v[1] = eps_pl_1

    dsdt = 0.0

    return s, dsde, dsdt, state_v
