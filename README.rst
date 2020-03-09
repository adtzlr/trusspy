**TrussPy** is a 3D **Truss**-Solver written in **Py**-thon which is capable of material and geometric nonlinearities. It uses an object-oriented approach to structure the code in meaningful classes, attributes and methods. TrussPy contains both multistep functionality (multiple loadcase analysis with sequenced external forces) and an adaptive method to control incremental stepwidths. Input files may be written in Excel or directly in Python. A simple post-processing inside TrussPy is directly available via Matplotlib. Model Plots whether in undeformed or deformed configuration with optional contour plots on element forces are easy to show. They may also be generated for a series of increments and saved as a GIF Movie. Last but not least History (a.k.a. x-y) Plots for a series of increments or Path Plots along a given node path may be generated for nodal properties (displacements, forces) or global quantities like the Load-Proportionality-Factor (LPF).

Official Documentation: https://adtzlr.github.io/trusspy/


Installation
============

`pip install trusspy`

Example
=======

.. code:: python

    import trusspy as tp

    M = tp.Model(logfile=False)

    with M.Nodes as MN:
        MN.add_node( 1, coord=( 0, 0, 0))
        MN.add_node( 2, coord=( 1, 0, 1))
        MN.add_node( 3, coord=( 2, 0, 0))

    with M.Elements as ME:
        ME.add_element( 1, conn=(1,2), gprop=[1] )
        ME.add_element( 2 ,conn=(2,3), gprop=[1] )

        E = 1     # elastic modulus
        ME.assign_material( 'all', [E])

    with M.Boundaries as MB:
        MB.add_bound_U( 1, (0,0,0) )
        MB.add_bound_U( 2, (0,0,1) )
        MB.add_bound_U( 3, (0,0,0) )

    with M.ExtForces as MF:
        MF.add_force( 2, ( 0, 0,-1) )
    
    M.build()
    M.run()

    M.plot_model(config=['undeformed','deformed'], 
                 inc=20, 
                 force_scale=2,
                 contour='force'
                 )
    M.plot_history(nodes=[2,2], X='Displacement Z', Y='LPF')
