# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:35:19 2018

@author: adutz
"""

import numpy as np
from numpy.linalg import norm,solve,inv
#from scipy.optimize import fsolve
    
def newton_rhapson(f,dfdx,x, nfev=50, tol=8, tolcomp=-1, verbose=1):
    try:
        len(x)
        ndim = True
    except:
        ndim = False
        
    # init success flag
    success = False
        
    if ndim:
        for i in range(nfev):
            dx = solve(dfdx(x),-f(x))
            #dx = -inv(dfdx(x))@f(x)
            x = x+dx
            if verbose > 2: 
                print(('  Iteration {:2d}, |dumax|: {:+2.4e}, dlpf: {:+2.4e}, norm: {:+2.4e}').format(i, max(abs(dx[:tolcomp])), dx[tolcomp], norm(f(x)[:tolcomp])))
            #x = inv(dfdx(x))@f(x)
            if norm(f(x)[:tolcomp]) < 10**-tol:
            #if max(abs(f(x)[:tolcomp])) < 10**-tol:
                success = True
                if verbose > 2: 
                    print('Tol. reached. NR-Iterations stopped.')
                break
            if i == nfev-1: print('Warning: Convergence not reached.')
    else:
        for i in range(nfev):
            dx = -f(x)/dfdx(x)
            x = x+dx
            if norm(f(x)) < 10**-tol:
                success = True
                break

    return x,success