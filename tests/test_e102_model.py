# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example 102
# -----------
# - 2 Trusses with 1 DOF
# - material: linear elastic

# import TrussPy (absolute path to local copy if trusspy not installed)
try:
    import trusspy as tp
except ImportError:
    import sys

    sys.path.append(r"../../")
    import trusspy as tp

M = tp.Model("e102_input.xlsx")

M.Settings.incs = 100

# Create Model, Run, show Results
M.build()
M.run()

# model plot: undeformed and deformed configuration for last increment
fig, ax = M.plot_model(
    config=["undeformed", "deformed"],
    view="xz",
    contour="force",
    lim_scale=2,
    force_scale=0.2,
    inc=-1,
)
fig.savefig("model_contour-force_inc-last.pdf")

# history plot
fig, ax = M.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF")
fig.savefig("history_node2_DispZ-LPF.pdf")

# show plots
# M.plot_show()
