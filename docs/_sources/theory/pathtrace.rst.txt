Path-Following Algorithm
========================

This section gives an overview of the algorithm for the path-following :func:`trusspy.solvers.tpsolver.pathfollow` of the equilibrium curve. The algorithm is called once for each step, which contains solutions for a number of increments. During an increment several Newton-Rhapson (NR) iterations are performed to obtain a fullfilled equilibrium.

.. figure:: pathtracing.*
   :align: center
   :width: 90%
   :alt: Curve-Following Algorithm
   
   Curve-Following Algorithm
   
Description
-----------
For the first increment the control component is unknown. Therefore it is set to the load-proportionality-factor (LPF) component, which is the last one in :math:`\boldsymbol{V}`. An Increment starts with the linearized Newton-Rhapson Iteration of the extended equilibrium equations. After finishing this Iteration a check on the control component is performed: If the control component changes, the overshoot in the highest component will be compensated by the application of a scale factor for the whole system vector :math:`\Delta\boldsymbol{V}`. Otherwise the solution will be saved and the nonlinear solution process (Newton-Rhapson Iterations) is called. If no convergence was found, the calculation stops. If the control component changes and the nonlinear solution process converged, the Increment will be recycled. Therefore the solution :math:`\Delta\boldsymbol{V}` is resetted to the value from the beginning of the increment. The recycle will be performed with the updated control component. If the nonlinear solution process did converge and all components of the incremental system vector are inside the specified tolerances :math:`|\Delta\boldsymbol{V}| \le \Delta\boldsymbol{V}_{max}`, the results are saved and the increment is successful. After that the next increment will be started.

Newton-Rhapson Iterations
=========================

.. figure:: newton.*
   :align: center
   :width: 90%
   :alt: Newton-Rhapson Iterations (nonlinear solution process) for an arbirtrary Increment.
   
   Newton-Rhapson Iterations (nonlinear solution process) for an arbirtrary converged Increment.

A Newton-Rhapson algorithm is used to obtain valid solutions of the extended system equlibrium vector with small incremental solutions :math:`\delta\boldsymbol{V}`. During an increment several Newton-Iterations (nonlinear solution process) are performed. During the nonlinear solution process the **control component remains fixed**. The figure shows an increment with :math:`f` as the control component. Several iterations are performed until convergence is reached. The final solution is inside the scope of :math:`x` and therefore the solution is accepted. The total incremental solution :math:`\Delta\boldsymbol{V}` of an Increment is obtained by a sum of the iterative incremental results.

..  math::

    \Delta \boldsymbol{V} = \sum_{n=1}^{n_{max}} \delta \boldsymbol{V}_n
    
If :math:`x(t+dt)` would be outside of it's scope the increment would be recycled. This is illustrated in the following figure. Although the solution converges, :math:`x` at time :math:`(t+dt)` violates the scope of x. Therefore the increment will be recycled.

.. figure:: newton_recycle.*
   :align: center
   :width: 90%
   :alt: Newton-Rhapson Iterations (nonlinear solution process) for an arbirtrary Increment.
   
   Newton-Rhapson Iterations (nonlinear solution process) for an arbirtrary converged Increment.