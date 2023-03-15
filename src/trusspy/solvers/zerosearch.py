# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

from numpy.linalg import norm
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


def newton(f, dfdx, x, nfev=8, ftol=1e-8, xtol=1e-8, verbose=0, *args):
    """Find the roots of a function using the Newton-Rhapson algorithm.

    Find the roots of the (non-linear) equations `f` given a starting
    estimate x. The derivative `dfdx`of `f` w.r.t. `x` has to be provided by the
    user. Iteration loop stops after maximum number of function
    evaluations is reached (default: `nfev=8`). Default tolerance is
    8 digits for vector norm of function residual and 8 digits for
    vector norm of incremental dx. If both tolerances are reached then
    the loop ends and the `success` flag becomes `True`. Return the roots of the
    (non-linear) equations defined by ``f(x) = 0`` given a starting estimate.

    Parameters
    ----------
    f : ndarray
        1D Vectorized function to minimize which depends on vector `x`
    dfdx : ndarray
        2D Derivative of function w.r.t. `x`
    x : ndarray
        1D Initial solution vector
    nfev : int, optional
        Maximum number of newton iterations (default is 8)
    ftol : float, optional
        Tolerance for residual of function: `norm(f)` (default is 1e-8)
    xtol : float, optional
        Tolerance for residual of `x`: `norm(x)` (default is 1e-8)
    verbose : int, optional
        Level of information during iterations (default is 0):
        `verbose=0` ... no information,
        `verbose=1` ... print `iteration number`, `norm(f)`, `norm(x)`
    arg s: tuple, optional
        pass arbitrary number of additional variables
        to function and derivative

    Returns
    -------
    x : ndarray
        final solution
    success : bool
        'True' if valid solution found, 'False' if not converged
    n : int
        number of function iterations
    f_norm : float
        norm(f)
    x_norm : float
        norm(x)


    Examples
    --------

    >>> import numpy as np
    >>> def f(x, a):
    ...     return np.array([a*x[0]**3-1])
    >>> def dfdx(x, a):
    ...     return np.array([a*3*x[0]**2])

    >>> x0 = np.array([1.5])
    >>> a = 2

    >>> from trusspy.solvers import newton
    >>> x,success,ntot,f_norm,x_norm = newton(f, dfdx, x0, 8, 1e-8, 1e-8, 0, a)

    >>> x
    array([0.79370053])
    >>> success
    True
    >>> ntot
    6
    >>> f_norm <= 1e-8
    True
    >>> x_norm <= 1e-8
    True
    """

    success = False

    # NEWTON-RHAPSON ITERATIONS
    for n in range(nfev):
        dx = spsolve(csr_matrix(dfdx(x, *args)), -f(x, *args))

        # UPDATE SOLUTION
        x = x + dx

        # CHECK IF EQUILIBRUM FOUND
        f_norm = norm(f(x, *args))
        x_norm = norm(dx)

        if verbose > 0:
            print(
                "|     |  {0:2d}  |       |{1:1.3e}|    |        |    |        |    |        |".format(
                    n + 1, f_norm
                )
            )

        if f_norm < ftol and x_norm < xtol:
            success = True
            break

    return x, success, n + 1, f_norm, x_norm
