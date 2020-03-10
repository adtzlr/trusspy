**TrussPy** is a 3D **Truss**-Solver written in **Py**-thon which is capable of material and geometric nonlinearities. It uses an object-oriented approach to structure the code in meaningful classes, attributes and methods. TrussPy contains both multistep functionality (multiple loadcase analysis with sequenced external forces) and an adaptive method to control incremental stepwidths. Input files may be written in Excel or directly in Python. A simple post-processing inside TrussPy is directly available via Matplotlib. Model Plots whether in undeformed or deformed configuration with optional contour plots on element forces are easy to show. They may also be generated for a series of increments and saved as a GIF Movie. Last but not least History (a.k.a. x-y) Plots for a series of increments or Path Plots along a given node path may be generated for nodal properties (displacements, forces) or global quantities like the Load-Proportionality-Factor (LPF).
   
Official Documentation: https://adtzlr.github.io/trusspy/

Installation
============

Use `pip` to install TrussPy

.. code:: bash

   pip install trusspy

Example
=======

.. code:: python

    import trusspy as tp

    M = tp.Model()

    # create nodes
    with M.Nodes as MN:
        MN.add_node( 1, (0,0,0) )
        MN.add_node( 2, (1,0,0) )

    # create element
    with M.Elements as ME:
        ME.add_element( 1, [1,2] )
        ME.assign_material('all', [1])
        ME.assign_geometry('all', [1])

    # create displacement (U) boundary conditions
    with M.Boundaries as MB:
        MB.add_bound_U( 1, (0,0,0) )
        MB.add_bound_U( 2, (1,0,0) )

    # create external forces
    with M.ExternalForces as MF:
        MF.add_force( 2, (1,0,0) )

    # build model, run, show results
    M.build()
    M.run()

    # plot results
    M.plot_model()
    M.plot_show()
	
Online Notebook
===============

Try TrussPy without installation in an `Interactive Online Notebook`_.

.. _`Interactive Online Notebook`: https://mybinder.org/v2/gh/adtzlr/trusspy/master?filepath=tests%2Fe101%2Fe101_nb_interactive.ipynb