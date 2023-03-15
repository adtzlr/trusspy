# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np


def truss(
    e,
    nodes,
    Xnodes,
    Unodes,
    U0nodes,
    rnodes,
    nodelist,
    elementlist,
    stage,
    state_v,
    mat_prop,
    geo_prop,
    umat,
    analysis,
):

    NA, NE = nodes
    XA, XE = Xnodes
    UA, UE = Unodes
    rA, rE = rnodes

    dU = UE - UA
    dX = XE - XA
    dx = dX + dU

    U0A, U0E = U0nodes
    dU0 = U0E - U0A
    dx0 = dX + dU0

    # elemental normal vector in deformed configuration
    n = dx / np.linalg.norm(dx)

    # elemental length in undeformed and deformed configuration
    L = np.sqrt(np.dot(dX, dX))
    l = np.sqrt(np.dot(dx, dx))
    l0 = np.sqrt(np.dot(dx0, dx0))

    # stretch and nominal strain
    lam0 = l0 / L
    lam = l / L
    E11 = lam - 1
    dE11 = lam - lam0
    # dE11 = 0.0 # TODO:

    # state variable
    if state_v is not None:
        state_ve = state_v[np.where(elementlist == e)][0]
    else:
        state_ve = None

    # normal force
    stress, dsde, dsdt, state_ve = umat(E11, dE11, mat_prop, state_ve)

    A = geo_prop[0]
    N = stress * A

    # Transformation Matrix
    # local --> global coordinate system
    T = np.array([[*n, *np.zeros(3)], [*np.zeros(3), *n]])

    B = 1 / L * np.array([[-1, 1]])
    B_global = B @ T
    KT = dsde * B_global.T @ B_global * A * L
    KTEE = KT[:3, :3]

    if stage == "G":
        # Equilibrium
        rA += N * -n
        rE += N * n

        analysis.stretch[np.where(elementlist == e)] = [lam]
        analysis.element_stress[np.where(elementlist == e)] = [stress]
        analysis.element_force[np.where(elementlist == e)] = [N]

        if state_v is not None:
            state_v[np.where(elementlist == e)] = [state_ve]

        analysis.r[np.where(nodelist == NA)] = [rA]
        analysis.r[np.where(nodelist == NE)] = [rE]

    if stage == "K":
        # Tangent Stiffness
        J = np.eye(3)
        KTEE = dsde * A / L * np.outer(n, n) + N / l * (J - np.outer(n, n))

        # Transformation Matrix
        # local --> global coordinate system
        # T = np.array([[          *n, *np.zeros(3)],
        #              [*np.zeros(3),          *n]])

        # B  = 1/L * np.array([[-1, 1]])
        # B_global = B@T
        # KT = dsde*B_global.T@B_global * A*L
        # KTEE = KT[:3,:3] + N/l*(J-np.outer(n,n))

        analysis.K[
            np.where(nodelist == NA)[0][0], np.where(nodelist == NA)[0][0]
        ] += KTEE  # KT[ :3, :3]# KTEE
        analysis.K[
            np.where(nodelist == NA)[0][0], np.where(nodelist == NE)[0][0]
        ] += -KTEE  # KT[3:6, :3]# -KTEE
        analysis.K[
            np.where(nodelist == NE)[0][0], np.where(nodelist == NA)[0][0]
        ] += -KTEE  # KT[ :3,3:6]#-KTEE
        analysis.K[
            np.where(nodelist == NE)[0][0], np.where(nodelist == NE)[0][0]
        ] += KTEE  # KT[ :3, :3]# KTEE

    return analysis, state_v
