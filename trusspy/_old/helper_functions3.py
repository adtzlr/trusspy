# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:11:23 2018

@author: adutz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from mpl_toolkits.mplot3d import Axes3D
#from numpy.linalg import norm

# projection : [‘aitoff’ | ‘hammer’ | ‘lambert’ | ‘mollweide’ | ‘polar’ | ‘rectilinear’], optional

def plot_nodes(X,view='xz',color='C0'):
    if view=='xz':
        i,j = 0,2
    if view=='xy':
        i,j = 0,1
    if view=='yz':
        i,j = 1,2
        
    fig = plt.figure(0)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:,0],X[:,1],X[:,2],marker='o',color=color)
    #plt.axes().set_aspect('equal');
    ax.set_aspect('equal')
    ax.set_proj_type('ortho') #'persp'
    plt.show()
    #ax.view_init(0, 0)
    
def plot_force(f0,X,view='xz',color='C3'):
    if view=='xz':
        i,j = 0,2
    if view=='xy':
        i,j = 0,1
    if view=='yz':
        i,j = 1,2
    for f0i,Xi in zip(f0,X):
        a = 0.5
        #print((f0i==np.zeros(3)).all())
        if ~(f0i==np.zeros(3)).all():
            xx = Xi[i]
            yy = Xi[j]
            if f0i[i] < 0:
                xx += -a*f0i[i]
            if f0i[j] < 0:
                yy += -a*f0i[j]
            plt.arrow(xx,yy,a*f0i[i],a*f0i[j],color=color,linewidth=4)
    plt.axes().set_aspect('equal');
    
def plot_elems(E,X,view='xz',color='C0',contour=None):
    if view=='xz':
        i,j = 0,2
    if view=='xy':
        i,j = 0,1
    if view=='yz':
        i,j = 1,2
        
    for k,e in enumerate(E):
        NA = int(e[-2])
        NE = int(e[-1])
        
        if contour is not None:
            # build up colormap and normalizer
            colormap = plt.get_cmap('viridis')
            norm = mpl.colors.Normalize(vmin=0.8, vmax=1.2)
            color = colormap(norm(contour[k]))
            print(norm(contour[k]),contour[k])
            
        plt.plot([X[NA-1][i],X[NE-1][i]],[X[NA-1][j],X[NE-1][j]],color=color)
    #plt.colorbar()