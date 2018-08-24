# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

import numpy as np

# import TrussPy
import trusspy as tp
import matplotlib.pyplot as plt
            
M = tp.Model('tests/Input_NTA_X.xlsx', logfile=True)

M.Settings.dlpf = 0.005
M.Settings.du = 0.05

M.Settings.incs = (180,10)
M.Settings.xlimit = ((0,1),(0,1))
#M.Settings.cycl = 10

M.Settings.stepcontrol = True
M.Settings.maxfac = 1

M.Settings.ftol = 8
M.Settings.xtol = 8
M.Settings.nfev = 8

M.Settings.dxtol = 1.25

#M.Settings.nstatev = 2
M.Settings.nsteps = 1

#M.Settings.j0 = 2
#M.Settings.j_fixed = True

# Create Model, Run, show Results
M.build()
#M.Results.R[0].Ured = np.array([1.0, -0.25, -0.375, 0.5, -0.125, -0.75])
M.run()

# lim_scale < 1: fixed value for all axis (good for videos)
# lim_scale > 1: scale factor for min/max values
# forces:        1 N = "force_scale" L

#M.plot_model(config=['undeformed'],
#             view='3d',
#             contour='stretch',
#             lim_scale=1.0,
#             force_scale=10.0,
#             inc=0)


#M.plot_model(config=['undeformed','deformed'],
#             view='xz',
#             contour='force',
#             lim_scale=100.0,
#             force_scale=50.0,
#             inc=-1)
    
#M.plot_movie(config=['undeformed','deformed'],
#             view='xz',
#             contour='stretch',
#             lim_scale=-1.5,
#             force_scale=10.0,
#             incs='all')


# Model.Result.PlotNode(2, X="Displacement U", Y="Force X")
# Model.Result.PlotContour("Force X", undeformed=True, deformed=True)

#M.plot_history(nodes=[2,2],X='Displacement X',Y='LPF')
#M.plot_history(nodes=[2,1],X='Displacement Z',Y='Force Z')
#M.plot_history(nodes=[2,2],X='Increments',Y='State Variable 2')
fig,ax = M.plot_history(nodes=[4,4],X='Displacement Z',Y='LPF')
fig,ax = M.plot_history(nodes=[5,5],X='Displacement Z',Y='LPF',fig=fig,ax=ax)
#
#fig,ax = M.plot_history(nodes=[4,4],X='Displacement Y',Y='LPF')
#fig,ax = M.plot_history(nodes=[5,5],X='Displacement Y',Y='LPF',fig=fig,ax=ax)
#
#fig,ax = M.plot_history(nodes=[4,4],X='Displacement X',Y='LPF')
#fig,ax = M.plot_history(nodes=[5,5],X='Displacement X',Y='LPF',fig=fig,ax=ax)

#plt.show()