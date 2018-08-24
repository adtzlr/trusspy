# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example 101
# -----------
# - 1 Truss with 1 DOF
# - material: linear elastic

# import TrussPy (absolute path to local copy if trusspy not installed)
try:
    import trusspy as tp
except ImportError:
    import sys
    sys.path.append(r'../../')
    import trusspy as tp

M = tp.Model()

M.Settings.du = 0.02
M.Settings.dlpf = 0.02
M.Settings.incs = 10

N1 = tp.Node( 1, (0,0,0) )
N2 = tp.Node( 2, (1,0,0) )

E1 = tp.Element( 1, [1,2])

B1 = tp.BoundaryU( 1, (0,0,0) )
B2 = tp.BoundaryU( 2, (1,0,0) )

#F1 = tp.ExternalForce( 1, (0,0,0) )
F2 = tp.ExternalForce( 2, (1,0,0) )

M.Nodes.add_nodes([N1,N2])
M.Elements.add_element(E1)

M.Elements.assign_material('all', mprop=[1,0.01,0.01], mtype=2)
M.Elements.assign_geometry('all', gprop=[1])

M.Boundaries.add_bounds_U([B1,B2])
M.ExtForces.add_forces([F2])

# Create Model, Run, show Results
M.build()
M.run()

# model plot: undeformed and deformed configuration for last increment
fig0, ax0 = M.plot_model(config=['undeformed'],
             view='xz',
             lim_scale=(-0.5,3.5,-2,2),
             force_scale=0.5,
             inc=0)
fig0.savefig('model_contour-force_inc-begin.pdf')
fig0.savefig('getting_started-1.png')

fig1, ax1 = M.plot_model(config=['deformed'],
             view='xz',
             contour='force',
             lim_scale=(-0.5,3.5,-2,2),
             force_scale=1.0,
             inc=-1)
fig1.savefig('model_contour-force_inc-last.pdf')
fig1.savefig('getting_started-2.png')

# history plot
fig2, ax2 = M.plot_history(nodes=[2,2],X='Displacement X',Y='Force X')
fig2.savefig('history_node2_DispX-ForceX.pdf')
fig2.savefig('getting_started-3.png')

#M.plot_movie(config=['deformed'],
#             view='xz',
#            
#            contour='force',
#             lim_scale=(-0.5,3.5,-2,2),
#             force_scale=1.0,
#             cbar_limits=[-1,1])

# show plots
# M.plot_show()