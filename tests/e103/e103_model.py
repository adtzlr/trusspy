# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example 103
# -----------
# - 2 Trusses with 1 DOF ("Zweibock" with geometric imperfection)
# - material: linear elastic

# import TrussPy (absolute path to local copy if trusspy not installed)
try:
    import trusspy as tp
except ImportError:
    import sys
    sys.path.append(r'../../')
    import trusspy as tp

M = tp.Model('e103_input.xlsx')

M.Settings.dlpf = 0.005
M.Settings.du = 0.05

M.Settings.incs = 250

M.Settings.stepcontrol = True
M.Settings.maxfac = 1

M.Settings.ftol = 8
M.Settings.xtol = 8
M.Settings.nfev = 8

M.Settings.dxtol = 1.25

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
fig, ax = M.plot_history(nodes=[2,2],X='Displacement X',Y='Displacement Z')
fig.savefig('history_node2_DispX-DispZ.pdf')

# show plots
#M.plot_show()