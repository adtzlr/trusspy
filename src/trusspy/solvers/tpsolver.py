# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import copy

import numpy as np

from .zerosearch import newton


def f(Vred, V0red, j, Vmax, equilibrium, stiffness, analysis=None, statev_write=False):
    """equilibrium function, extended to (nDOF+1)"""

    analysis.j = j

    return np.append(
        -equilibrium(Vred, V0red, analysis=analysis, statev_write=statev_write),
        Vred[abs(j) - 1] - Vmax,
    )


def dfdx(
    Vred, V0red, j, Vmax, equilibrium, stiffness, analysis=None, statev_write=False
):
    """stiffness matrix, extended to (nDOF+1,nDOF+1)"""

    analysis.j = j

    # qc ... control equation
    qc = np.zeros(len(Vred))
    qc[abs(j) - 1] = 1

    # f0red ... external force vector f0 with active DOF
    #           reshaped to column-vector

    # modified stiffness
    #
    #          | KT       f0red |
    # KT_mod = | qcU  qc_lambda |

    analysis.Kmod = np.vstack(
        (np.hstack((stiffness(Vred[:-1], analysis=analysis), -analysis.f0red)), qc)
    )

    return analysis.Kmod


def dxmax_control(
    dxmax,
    dxmax0,
    j,
    j0,
    z,
    cycl,
    nr_success,
    b,
    n,
    nfev,
    minfac=1e-6,
    maxfac=10,
    reduce=8.0,
    increase=0.5,
    verbose=2,
):
    """Automatic control for incremental limit of system vector x. Based on the
    success of the nonlinear solution process the incremental limit will be
    either increased or decreased. If the newton iterations in the current inc.
    converged and the last 3 increments were successful (without any recycle)
    an increase of `dxmax` is performed. The amount of successful increments
    before the current one is read by the parameter `b`. The increase factor is
    based on a constant value `increase` and on the convergence rate of the
    current increment. The total increase factor is calculated as
    `increase_total = 1 + (nfev-n)/nfev * increase`. On the other hand,
    if the current increment did not converge, `dxmax` will be reduced by a
    given value `decrease`. Both an increase and decrease is only performed
    inside the interval `minfac*dxmax0 <= dxmax <= maxfac*dxmax0`.

    Parameters
    ----------
    dxmax : ndarray
        current incremental limit of system vector x
    dxmax0 : ndarray
        initial incremental limit of system vector x
    j : int
        current control component of x
    j0 : int
        initial control component of x (at the beginning of the inc.)
    z : int
        number of recycles in current increment
    cycl: int
        max. number of recycles
    nr_success : bool
        flag to check if nonlinear solution process converged
    b : int
        number of converged increments before this increment
    n : int
        number of newton iterations until convergence was reached
    nfev : int
        allowed number of newton iterations
    minfac : float, optional
        minimum factor of dxmax0 where a decrease of dxmax is performed
        (`minfac*dxmax0 <= dxmax <= maxfac*dxmax0`)
    maxfac : float, optional
        minimum factor of dxmax0 where a decrease of dxmax is performed
        (`minfac*dxmax0 <= dxmax <= maxfac*dxmax0`)
    reduce : flaot, optional
        factor do decrease dxmax if current increment did not converge.
        (`dxmax= dxmax/reduce`)
    increase : float, optional
        factor do increase dxmax if current increment and the 3 increments
        before did converge.
        (`dxmax = dxmax * (1 + (nfev-n)/nfev * increase)`)
    verbose : int, optional
        Level of information during iterations (default is 0):
        `verbose=0,1` ... no information,
        `verbose=2`   ... print dxmax changes

    Returns
    -------
    dxmax : ndarray
        updated incremental limit of system vector x
    z : int
        updated number of recycles in current increment
    b : int
        updated number of converged increments before this increment
    dx_changed : bool
        flag to indicate if a change in dxmax was performed

    """

    dx_changed = False

    # not converged
    if not nr_success:
        if dxmax[0] > dxmax0[0] * minfac:
            if z + 1 == cycl:
                z = 0
                final_step_reduction = True
                if verbose > 1:
                    print(
                        "* reduce NR-step although control comp. changes (max. recycles reached)."
                    )
            else:
                final_step_reduction = False
                if verbose > 1:
                    print("* reduce NR-step size by factor: (inactive) due to recycle.")

            if j0 == j or final_step_reduction:  # or True:
                if verbose > 1:
                    print(
                        "* reduce NR-step size by factor: {:10.3g}".format(1 / reduce)
                    )
                dxmax = dxmax / reduce
                dx_changed = True
                b = 0  # reset counter to increase width again

    # converged
    else:
        if dxmax[0] < dxmax0[0] * maxfac:
            if j0 == j:
                if z > 0:
                    pass
                elif b <= 3:
                    if verbose > 1:
                        print(
                            "* increase NR-step (inactive). incs since last reduction: {0:1d}/{1:1d}".format(
                                b, 3
                            )
                        )
                else:
                    # increase factor depends on convergence rate
                    #
                    # Example
                    # -------
                    #   nfev = 8, n = 4
                    #   1+(8-n)/8 = 1.5
                    #   total_increase = increase*1.5
                    dxmax = dxmax * (1 + (nfev - n) / nfev * increase)
                    dx_changed = True
                    if verbose > 1:
                        print(
                            "* increase NR-step size by factor: {:10.3g}".format(
                                1 + (nfev - n) / nfev * increase
                            )
                        )
        else:
            if j == j0:
                dxmax = dxmax0.copy() * maxfac
                dx_changed = True

    return dxmax, z, b, dx_changed


def pathfollow(
    g,
    dgdx,
    x,
    analysis,
    dxmax=[0.02, 0.02],
    j=None,
    j_fixed=False,
    j_pre=True,
    xlimit=None,
    incs=20,
    nfev=8,
    cycl=4,
    ftol=1e-8,
    xtol=1e-8,
    stepcontrol=True,
    maxfac=10,
    minfac=1e-6,
    reduce=8,
    increase=1,
    dxtol=1.25,
    verbose=0,
):
    """Path following algorithm of a curve.

    Parameters
    ----------
    f : ndarray
        1D Vectorized function to minimize which depends on vector `x`
    dfdx : array
        2D Derivative of function w.r.t. `x`
    x : ndarray
        1D Initial solution vector
    analysis : trusspy.core.analysis
        Analysis object
    dxmax: array_like, optional
        Maximum incremental step in Dx. Several input methods are possible.
        A single float value will assign dxmax to all components of Dx.
        A list of length 2 will control all values with dxmax[0] except
        for the last one, which is controlled by dxmax[1]. A list of length x
        assigns each component of dxmax to the corresponding component of x.
        (default is [0.02, 0.02])
    j : int, optional
        initial control component. Limit j-th component of Dx
        during an increment (default is None which will use last
        component of Dx --> LPF load component)
    j_fixed : bool, optional
        Lock control component to initial j (default is False). If True, a
        dedicated control component j has to be specified.
    j_pre : bool, optional
        Use linearized solution at the beginning of each increment to determine
        the control component j. The determinant of K control the sign of j.
        (default is True)
    x_limit : list, optional
        List of length 2 containing [j,max_value] to limit the
        loadcase execution. (default is None)
    incs : int, optional
        Maximum number of increments. (default is 20)
    nfev : int, optional
        Maximum number of newton iterations (default is 8)
    cycl : int, optional
        Maximum number of recycles, either due to a switch in control component
        or non-converged newton step if stepsize-control is active.
        (default is 4)
    ftol : float, optional
        Tolerance for residual of function: `norm(f)` (default is 1e-8)
    xtol : float, optional
        Tolerance for residual of `x`: `norm(x)` (default is 1e-8)
    stepcontrol : bool, optional
        Automatic adjustment of incremental stepwidth Dx. Parameters `macfac`,
        `minfac`, `reduce` and `increase` will control the adjustment. All
        components of `dxmax` will be increased or reduced by the same factor.
        (default is True)
    maxfac : float, optional
        Maximum factor compared to initial dxmax. (default is 10)
    minfac : float, optional
        Minimum factor compared to initial dxmax. (default is 1e-6)
    reduce : float, optional
        Factor to reduce dxmax. Updating dxmax follows `dxmax = dxmax/reduce`.
        (default is 8)
    increase : float, optional
        Factor to increase dxmax. To increase dxmax the total number of
        newton iterations to achieve convergence will be used. Updating dxmax
        follows `dxmax = dxmax*(1+(nfev-n)/nfev * increase)`.
        (default is 1)
    dxtol : float, optional
        Allowed vvershoot factor of control component if solution has
        converged. Will help to speed-up solution and avoid unneccessary re-
        cycles. (default is 1.25)
    verbose : int, optional
        Level of information during iterations (default is 0):
        `verbose=0` ... no information,
        `verbose=1` ... print `iteration number`, `norm(f)`, `norm(x)`

    Returns
    -------
    res_x: ndarray
        2D-array containing all valid solutions for all increments. Shape is
        `res_x.shape = (incs, len(x)+1)`. Result array `res_x[1]` contains the
        converged solution vector for the first increment. Result component
        res_x[0] contains start solution which is typically zeros.
    res_a: Analysis
        Analysis Class (trusspy.core.analysis.Analysis) with converged solution.
    """

    # extend x by one dimension
    x = np.append(x, 0)

    # init result
    res_x = x.copy()
    res_a = [copy.deepcopy(analysis)]

    # check if dxmax is a vector
    try:
        # check if dxmax has length 2: use first entry for all components of dx
        # except the last one.
        # The second value is for the last component of dx.
        if len(dxmax) == 2:  # [du,dlpf]
            dxm = np.ones_like(x)
            dxm[:-1] = np.ones(len(x) - 1) * dxmax[0]
            dxm[-1] = dxmax[-1]
            dxmax = dxm

    except:
        # if dxmax is a scalar: assign it to every component of dx
        dxmax = np.ones_like(x) * dxmax
    dxmax0 = dxmax.copy()

    # init control component to LPF
    if not j_fixed:
        j = len(x)

    # init INCREMENTS SINCE LAST REFINEMENT (stepcontrol)
    b = 4

    # init stop flag
    stop = False

    # loop over increments
    for i in range(incs):
        # print informations
        if verbose > 0:
            # print(r'\pagebreak')
            print(r"")
            print(r"### Increment", i + 1)

        if verbose > 1:
            print(
                r"|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |"
            )
        if verbose > 1:
            print(
                "|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|"
            )

        # COPY RESULT
        x0 = x.copy()

        # RECYCLE UNTIL VALID SOLUTION IS FOUND
        z = 0

        # init success flag of pre-identification of j
        nr_success_pre = False

        # -----------------------------------------------------------------
        # BEGIN PRE-IDENTIFY j
        # -----------------------------------------------------------------
        n_pre = 0
        if j_pre and not j_fixed:
            # only one nr-iteration
            nfev_pre = 1

            # j is initially set to the LPF-component
            # sign of j is identified by the sign of the stiffness matrix K
            # args = x0,len(x),0,g,dgdx,analysis,False
            # sign_pre = np.sign(np.linalg.det(dfdx(x,*args)[:-1,:-1]))
            # j_pre0 = int(len(x)*sign_pre)
            # xmax_pre = x[abs(j_pre0)-1] + dxmax[abs(j_pre0)-1] *np.sign(j_pre0)

            # get linearized solution x
            xmax_pre = x[abs(j) - 1] + dxmax[abs(j) - 1] * np.sign(j)
            args = x0, j, xmax_pre, g, dgdx, analysis, False

            x_pre, nr_success_pre, n_pre, f_norm_pre, x_norm_pre = newton(
                f, dfdx, x, nfev_pre, ftol, xtol, 0, *args
            )

            # incremental solution
            Dx_pre = x_pre - x0

            # Dx/dxmax --> get j-th component with maximum value and it's sign
            Dxi_pre = 1 + np.argsort(abs(Dx_pre / dxmax))
            Dxs_pre = np.sort(abs(Dx_pre / dxmax)) * np.sign(
                (Dx_pre / dxmax).T[Dxi_pre - 1]
            )
            i1, v1 = Dxi_pre[-1], Dxs_pre[-1]
            j_pre = int(i1 * np.sign(v1))
            if verbose > 1:
                print(
                    "| {0:2d}  |  {1:2d}  |  {2:2d}   |{3:1.3e}|{4:4d}|{5:8.1g}|    |        |    |        |".format(
                        z + 1, n_pre - 1, j, f_norm_pre, i1, v1
                    )
                )

            # set the found solution to j
            j = j_pre

            if abs(v1) > dxtol:
                nr_success_pre = False

        # -----------------------------------------------------------------
        # END PRE-IDENTIFY j
        # -----------------------------------------------------------------

        # recylce loop
        while nr_success_pre is not True:
            if verbose > 1:
                print("")
            if verbose > 1:
                print(
                    r"|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |"
                )
            if verbose > 1:
                print(
                    "|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|"
                )

            # RESET X TO START SOLUTION X0 and COPY j to j0
            x = x0.copy()
            j0 = j

            # UPDATE CONTROL PARAMETER WITH CURRENT CONTROL COMPONENT
            xmax = x[abs(j) - 1] + dxmax[abs(j) - 1] * np.sign(j)

            # NEWTON-RHAPSON ITERATIONS (nonlinear solution process)
            args = x0, j, xmax, g, dgdx, analysis, False
            if z == 0 and j_pre and not j_fixed:
                x = x0 + Dx_pre / abs(Dxs_pre[-1])

            x, nr_success, n, f_norm, x_norm = newton(
                f, dfdx, x, nfev - n_pre, ftol, xtol, verbose, *args
            )

            # TOTAL INCREMENTAL SOLUTION
            Dx = x - x0

            # GET MAXIMUM COMPONENT AND SIGN
            Dxi = 1 + np.argsort(abs(Dx / dxmax))
            Dxs = np.sort(abs(Dx / dxmax)) * np.sign((Dx / dxmax).T[Dxi - 1])

            i1, v1 = Dxi[-1], Dxs[-1]
            i2, v2 = Dxi[-2], Dxs[-2]
            i3, v3 = 0, np.nan

            if len(x) > 2:
                i3, v3 = Dxi[-3], Dxs[-3]
            # if len(x) > 3:
            #    i4, v4 = Dxi[-4], Dxs[-4]

            # PRINT INFORMATIONS ON BIGGEST INCREMENTAL COMPONENTS
            if verbose > 1:
                print(
                    "|total| sum  | used  |  final  |    | final  |    | final  |    | final  |"
                )
                print(
                    "| {0:2d}  |  {1:2d}  |  {2:2d}   |{3:1.3e}|{4:4d}|{5:8.4f}|{6:4d}|{7:8.4f}|{8:4d}|{9:8.4f}|".format(
                        z + 1, n + n_pre, j, f_norm, i1, v1, i2, v2, i3, v3
                    )
                )

            # set new control comp. if not fixed by the user
            if not j_fixed:
                j = int(i1 * np.sign(v1))

            # save current dxmax as dVmax to analysis object
            # (do this **before** an adoption of dxmax is performed by
            #  `stepcontrol`)
            analysis.dVmax = dxmax

            # CHECK IF SOLUTION IS VALID --> GO TO NEXT INCREMENT
            solution_valid = False
            if j_fixed:
                if abs(Dx[abs(j) - 1] / dxmax[abs(j) - 1]) <= dxtol:
                    solution_valid = True
            else:
                if np.all(abs(Dx / dxmax) <= dxtol):
                    solution_valid = True

            # init flag for *stepcontrol changed dxmax* (sc_changed) to False
            sc_changed = False
            # -----------------------STEP WIDTH CONTROL------------------------
            if stepcontrol:
                dxmax, z, b, sc_changed = dxmax_control(
                    dxmax,
                    dxmax0,
                    j,
                    j0,
                    z,
                    cycl,
                    nr_success,
                    b,
                    n,
                    nfev - n_pre,
                    minfac,
                    maxfac,
                    reduce,
                    increase,
                    verbose=2,
                )

            if solution_valid and nr_success:
                # UPDATE STATE VARIABLES
                args = x0, j0, xmax, g, dgdx, analysis, True
                f(x, *args)
                b = b + 1
                # print(z, np.all(abs((Dx)/dxmax) <= 1+tol))
                break

            if z + 1 == cycl:
                stop = True
                print("")
                print(
                    "* **ERROR 1**: Job stopped - NR-it. failed, max. number of recycles reached."
                )
                print("  Reduce dVmax and/or activate adaptive stepwidth-control.")
                break

            if j0 == j and nr_success is False and sc_changed is False:
                stop = True
                print("")
                print(
                    "* **ERROR 2**: Job stopped - NR-it. failed, control component does not change."
                )
                print("  Reduce dVmax and/or activate adaptive stepwidth-control.")
                break

            # reset j
            if not nr_success:
                j = j0

            z = z + 1
            n_pre = 0

            print("")
            print("* recycling increment")

        # save results to analysis object
        # if not stop:
        analysis.Vred = x
        analysis.Ured = x[:-1]
        analysis.lpf = x[-1]

        res_x = np.vstack((res_x, x))
        res_a.append(copy.deepcopy(analysis))

        if verbose > 0:
            print("")
            print("* final LPF: {0: 10.4g}".format(x[-1]))

        # Stop due to error
        if stop:
            break

        # Maximum value reached
        if xlimit is not None:
            if abs(x[xlimit[0] - 1]) > xlimit[1]:
                print("* EXIT 1: Job stopped - max value of control component reached.")
                break

    return res_x, res_a
