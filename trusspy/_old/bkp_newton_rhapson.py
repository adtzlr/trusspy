# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:35:19 2018

@author: adutz
"""

import numpy as np
from numpy.linalg import norm,solve#,inv
#from scipy.optimize import fsolve

def nr_solve(df,f,x,*args,**kwargs):
    # Multi-Dimensional Newton-Rhapson solver

    # options
    op = {'tol':  12,
          'maxfev': 6,
          'log':  2}
    for key, value in kwargs:
        op[key] = value
        
    # initialize array of incremental variables
    dx = np.zeros_like(x)
    
    for i in range(op['maxfev']):
        dx = solve(df(x),f(x))
        x = x + dx
        
        if norm(f(x)) < 10**-op['tol']:
            break
        
    # set result informations
    message = None
    infodict = {'nfev': i}
    
    # print final results: converged or failed last increment
    if norm(f(x)) <= 10**-op['tol'] and i <= op['maxfev']:
        valid_solution = 1
        if op['log'] > 2: print('\n NR Solution:', i, valid_solution, 
                                norm(dx), norm(f(x)))
    else:
        valid_solution = 0
        if op['log'] > 2: print('\n NR Solution failed:', i, valid_solution, 
                                norm(dx), norm(f(x)))
    
    if op['log'] > 2: 
        return x, infodict, valid_solution, message
    else:
        return x
    
def newton_rhapson(f,dfdx,x, nfev=50, tol=8, tolcomp=-1):
    try:
        len(x)
        ndim = True
    except:
        ndim = False
        
    if ndim:
        for i in range(nfev):
            dx = solve(dfdx(x),-f(x)) # sign???
            x = x+dx
            print(('  Iteration {:2d}, dumax: {:+2.4e}, dlpf: {:+2.4e}, norm: {:+2.4e}').format(i, x[-1], max(abs(x)), norm(f(x)[:tolcomp])))
            #x = inv(dfdx(x))@f(x)
            if norm(f(x)[:tolcomp]) < 10**-tol:
                print('Tol. reached. NR-Iterations stopped.')
                break
    else:
        for i in range(nfev):
            dx = -f(x)/dfdx(x)
            x = x+dx
            if norm(f(x)) < 10**-tol:
                break

    return x

def NRArcLengthsolve(f,x0,jac,dl,f0,log=2,tol=1.e-12,i_max=6):
    
    # initialize array of incremental variables
    dx = np.ones_like(x0)
    
    # check if all values of start solution are zero
    # --> overwrite with small values
    # --> this avoids error "singular matrix" during 1st newton increment
    #if np.allclose(x0[:-1],0):
    #    x0[:-1].fill(tol)
    x = x0
    
    # pre-solution to identify maximum displacement component
    # with fixed delta_lpf = 0.0
    dxpre = solve(jac(x,0,1)[:-1][:,:-1], f(x)[:-1]+dl*f0)
    
    # DOF-index which contains maximum displacement and sign of that component
    j = np.argmax(max(abs(dxpre))) 
    sgn = np.sign(dxpre[j])
    
    if sgn == 0:
        sgn = 1.0
        print("WARNING: sign zero! Arbitrary Displacements possible. Set to '1.0'")
    
    
    
    # print header for results
    if log > 2: print('\n NR Iteration: \n   i |   norm(dx)   norm(f(x)) |   u,dlpf')
    

    # loop until tol is reached
    #   norm(dx)   < tol --> minimize step size
    #   norm(f(x)) < tol --> minimize residuals
    #   i <= i_max       --> iteration counter lower than max. allowed iterations
    i = 0
    #while (norm(dx[:-1]) > tol and (norm(f(x)[:-1]) > tol or i < 2)) and i <= i_max:
    while norm(f(x)[:-1] > tol) and i <= i_max:
        
        # print result table
        if log > 2: print((' {:3d} | {:+2.4e} {:+2.4e} | '+len(x)*'{:+2.4e} ').format(i, norm(dx[:-1]), norm(f(x)[:-1]), *x))
        
        # solve linearized system with nDOF+1
        dx = solve(jac(x0,j,sgn),f(x0))
        
        # update solution
        x = x0 + dx
        
        # set intermediate solution as start vector for next iteration
        x0 = x

        # increase iteration counter
        i = i+1
        
    # set result informations
    mesg = None
    ier = 0
    infodict = {'nfev': i, 'DOFmax': j, 'DOFmax value': x[j]}
    
    # print final results: converged or failed last increment
    if norm(dx[:-1]) <= tol or norm(f(x)[:-1]) <= tol and i <= i_max:
        ier = 1
        if log > 2: print('\n NR Solution:', i, ier, norm(dx[:-1]), norm(f(x)[:-1]))
    else:
        if log > 2: print('\n NR Solution failed:', i, ier, norm(dx[:-1]), norm(f(x)[:-1]))
    
    return x,infodict,ier,mesg

def NRsolve(f,x0,jac,dl,f0,log=2,tol=1.e-12,i_max=50):
    
    # initialize array of incremental variables
    dx = np.ones_like(x0)
    
    
    # check if all values of start solution are zero
    # --> overwrite with small values
    # --> this avoids error "singular matrix" during 1st newton increment
    if np.allclose(x0,0):
        x0.fill(1.e-8)
    x = x0
    
    # print header for results
    if log > 2: print('\n NR Iteration: \n   i |   norm(dx)   norm(f(x)) |   u')
    
    
    # loop until tol is reached
    #   norm(dx)   < tol --> minimize step size
    #   norm(f(x)) < tol --> minimize residuals
    #   i <= i_max       --> iteration counter lower than max. allowed iterations
    i = 0
    while (norm(dx) > tol or norm(f(x)) > tol) and i <= i_max:
        
        # print result table
        if log > 2: print((' {:3d} | {:+2.4e} {:+2.4e} | '+len(x)*'{:+2.4e} ').format(i, norm(dx), norm(f(x)), *x))

        # solve linearized system with nDOF
        dx = solve(jac(x0),dl*f0+f(x0))
        
        # update solution
        x = x0+dx
        x0 = x

        # increase iteration counter
        i = i+1
        
    # set result informations
    mesg = None
    ier = 0
    infodict = {'nfev': i}
    
    # print final results: converged or failed last increment
    if norm(dx) <= tol and norm(f(x)) <= tol and i <= i_max:
        ier = 1
        if log > 2: print('\n NR Solution:', i, ier, norm(dx), norm(f(x)))
    else:
        if log > 2: print('\n NR Solution failed:', i, ier, norm(dx), norm(f(x)))
    
    return x,infodict,ier,mesg