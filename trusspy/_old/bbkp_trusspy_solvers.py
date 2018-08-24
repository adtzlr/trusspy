# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:36:41 2018

@author: adutz
"""

import numpy as np

def nr_solve(f,dfdx,x,nfev=8,ftol=1e-8,xtol=1e-8,verbose=0,*args):
    
    success = False
    
    # NEWTON-RHAPSON ITERATIONS
    for n in range(nfev):
        #dx = -np.linalg.inv(dfdx(x,j,xmax))@f(x,j,xmax)
        dx = np.linalg.solve(dfdx(x,*args),-f(x,*args))
        
        # UPDATE SOLUTION
        x = x + dx
        
        # CHECK IF EQUILIBRUM FOUND
        f_norm = np.linalg.norm(f(x,j,xmax))
        x_norm = np.linalg.norm(dx)
        if (f_norm < ftol and x_norm < xtol):
            success = True
            break
            
    return x,success,n,f_norm,x_norm
        

def path_tracing(f,dfdx, x, dxmax=[0.02,0.02], j=None,
            incs=20,nfev=8,cycl=4,ftol=1e-8,xtol=1e-8,
            stepcontrol=True,maxfac=10,minfac=1e-6,reduce=8,increase=1,
            dxtol=1.25,
            verbose=0):
    
    # init result
    res_x = x.copy()
    
    # check if dxmax is a vector
    try:
        if len(dxmax) == 2:
            dxm = np.ones_like(x)
            dxm[:-1] = np.ones(len(x)-1) * dxmax[0]
            dxm[-1]  = dxmax[-1]
            dxmax = dxm
            
    except:
        dxmax = np.ones_like(x) * dxmax
    dxmax0 = dxmax.copy()
    
    # init control component
    if j==None:
        j = len(x)
        
    # INIT CONTROL PARAMETER
    xmax = x[abs(j)-1] + dxmax[abs(j)-1] *np.sign(j)
    if verbose > 1 and not np.allclose(x,0):
        print('\ninitial x-values:\n',x.reshape(len(x),1),'\n')
        print('\ninitial equlibrium:\n',f(x,j,xmax).reshape(len(x),1),'\n')
        
    # increments
    for i in range(incs):
        
        if verbose > 0: print('\n--------------------- START OF INCREMENT', i,'---------------------------------------------')
        if verbose > 1: print('                    |       Norm        |  sorted Dx/Dxmax (descending)')
        if verbose > 1: print('Inc  NR-Iter Control|    Eq.      dx    | i   Value | i   Value | i   Value | i   Value')
        if verbose > 1: print('-'*88)
        # COPY RESULT
        x0    =    x.copy()
        
        # RECYCLE UNTIL VALID SOLUTION IS FOUND
        z = 0
        while True:
            j0 = j
            
            # RESET X TO START SOLUTION X0
            x = x0.copy()
            
            # UPDATE CONTROL PARAMETER
            xmax = x[abs(j)-1] + dxmax[abs(j)-1] *np.sign(j)
            
            # NEWTON-RHAPSON ITERATIONS
            for n in range(nfev):
                #dx = -np.linalg.inv(dfdx(x,j,xmax))@f(x,j,xmax)
                dx = np.linalg.solve(dfdx(x,j,xmax),-f(x,j,xmax))
                
                # UPDATE SOLUTION
                x = x + dx
                
                # CHECK IF EQUILIBRUM FOUND
                eq_norm = np.linalg.norm(f(x,j,xmax))
                dx_norm = np.linalg.norm(dx)
                if (eq_norm < ftol and dx_norm < xtol):
                    break
                
                # TOTAL INCREMENTAL SOLUTION
                Dx = x-x0
                #Dx = -np.linalg.inv(dgdx(x))@g(x)
                
                Dxi = 1+np.argsort(abs(Dx/dxmax))
                Dxs = np.sort(abs(Dx/dxmax))*np.sign( (Dx/dxmax).T[Dxi-1] )
                
                i1, v1 = Dxi[-1], Dxs[-1]
                i2, v2 = Dxi[-2], Dxs[-2]
                i3, v3, i4, v4 = 0,0,0,0
                if len(x) > 2:
                    i3, v3 = Dxi[-3], Dxs[-3]
                if len(x) > 3:
                    i4, v4 = Dxi[-4], Dxs[-4]
                
                if verbose > 1: 
                    print(' {0:3d}    {1:2d}    {2:2d}    |{3:1.3e} {4:1.3e}|{5:2d} {6:8.3f}|{7:2d} {8:8.3f}|{9:2d} {10:8.3f}|{11:2d} {12:8.3f}'.format(
                          i,n,j,eq_norm,dx_norm,i1,v1,i2,v2,i3,v3,i4,v4))
            
            # UPDATE CONTROL COMPONENT
            #j = 1+np.where( abs((Dx)/dxmax) == max(abs((Dx)/dxmax)))[0][0]
            #j = int(j * np.sign(((Dx)/dxmax)[j-1]))
            
            if (eq_norm < ftol and dx_norm < xtol):
                j = int(i1*np.sign(v1))
            
            # STEP WIDTH CONTROL
            # ------------------------------------------
            if stepcontrol:
                #maxfac = 10
                #minfac = 1e-6
                #reduce   = 8
                #increase = 1
                
                if n == nfev-1:  # not converged
                    if dxmax[0] > dxmax0[0]*minfac:
                        if verbose > 1: print('\n...reducing NR-step size factor:', 1/reduce)
                        dxmax = dxmax/reduce
                else: # converged
                    if dxmax[0] < dxmax0[0]*maxfac:
                        if verbose > 1 and j==j0: print('\n...increasing NR-step size factor:', (1+(nfev-n)/nfev))
                        if j==j0: dxmax = dxmax*(1+(nfev-n)/nfev * increase)
                    else:
                        if j==j0: dxmax = dxmax0.copy()*maxfac
            # ------------------------------------------
    

            # RE-UPDATE CONTROL COMPONENT
            if stepcontrol:
                #j = 1+np.where( abs((Dx)/dxmax) == max(abs((Dx)/dxmax)))[0][0]
                #j = int(j * np.sign(((Dx)/dxmax)[j-1]))
                Dxi = 1+np.argsort(abs(Dx/dxmax))
                Dxs = np.sort(abs(Dx/dxmax))*np.sign( (Dx/dxmax).T[Dxi-1] )
                i1, v1 = Dxi[-1], Dxs[-1]
                if (eq_norm < ftol and dx_norm < xtol):
                    j = int(i1*np.sign(v1))
            
            
            # CHECK IF SOLUTION IS VALID
            if (np.all(abs((Dx)/dxmax) <= dxtol)) or z>cycl:
                #print(z, np.all(abs((Dx)/dxmax) <= 1+tol))
                break
            
            z=z+1
            print('\n')
        
        res_x = np.vstack((res_x, x))
        if verbose > 0: print('----------------------- END OF INCREMENT', i,'---------------------------------------------')
    
    return res_x