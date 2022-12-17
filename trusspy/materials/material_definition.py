# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:24:42 2018

@author: adutz
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

    # eps_el_0 = stress/E
    eps_pl_0 = state_v[1]
    # eps_el_0 = e-de-eps_pl_0
    # eps_0 = eps_el_0 + eps_pl_0

    # total strain at time t=t_n+1
    eps_1 = e  # eps_0+de

    # yield stress at time t=t_n
    if state_v[0] == 0:
        stress_yield_0 = Sy
    else:
        stress_yield_0 = state_v[0]

    # algorithm: isotropic hardening

    # trial state
    stress_trial = E * (eps_1 - eps_pl_0)
    eps_pl_trial = eps_pl_0
    # alpha_0 = (stateolde(1)-1)/kmod;
    # alpha_trial = alpha_0;
    f_trial = abs(stress_trial) - stress_yield_0

    if f_trial <= 0:
        # print('elastic step')
        # elastic strain increment
        stress_1 = stress_trial
        eps_pl_1 = eps_pl_trial  # eps_pl_1 = eps_pl_0
        # alpha_1 = alpha_trial; % alpha_1 = alpha_0
        dsde = E
        # elastic tangent
        delta_gamma = 0.0
    else:
        # print('plastic step')
        # plastic strain increment
        delta_gamma = f_trial / (E + K)
        stress_1 = (1 - (delta_gamma * E) / abs(stress_trial)) * stress_trial
        eps_pl_1 = eps_pl_0 + delta_gamma * np.sign(stress_trial)
        # alpha_1 = alpha_0 + delta_gamma
        dsde = E * K / (E + K)  # elastoplastic tangent

    # output (update) stress
    s = stress_1

    # output (update) state variables
    stress_yield_1 = stress_yield_0 + K * delta_gamma
    state_v[0] = stress_yield_1
    state_v[1] = eps_pl_1

    dsdt = 0.0

    return s, dsde, dsdt, state_v
