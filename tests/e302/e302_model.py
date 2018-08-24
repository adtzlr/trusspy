# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example 302
# -----------
# - 2 Trusses with 1 DOF
# - material: linear elastic - plastic (isotropic hardening)
# - 2 steps with restart after fixed amount of increments

# import TrussPy (absolute path to local copy if trusspy not installed)
try:
    import trusspy as tp
except ImportError:
    import sys
    sys.path.append(r'../../')
    import trusspy as tp

M = tp.Model('e302_input.xlsx')

M.Settings.dlpf = 0.05
M.Settings.du = 0.05

M.Settings.incs = (170,10)
M.Settings.xlimit = ((0,1),(0,1))

M.Settings.stepcontrol = True
M.Settings.maxfac = 1

M.Settings.ftol = 8
M.Settings.xtol = 8
M.Settings.nfev = 8

M.Settings.dxtol = 1.25

#M.Settings.nstatev = 2
M.Settings.nsteps = 2

# Create Model, Run, show Results
M.build()
M.run()

# model plot: undeformed and deformed configuration for last increment
fig, ax = M.plot_model(config=['undeformed','deformed'],
             view='xz',
             contour='force',
             lim_scale=2,
             force_scale=0.2,
             inc=-1)
fig.savefig('model_contour-force_inc-last.pdf')

# history plot
fig, ax = M.plot_history(nodes=[2,2],X='Displacement Z',Y='Force Z')
fig.savefig('history_node2_DispZ-ForceZ.pdf')

# show plots
#M.plot_show()