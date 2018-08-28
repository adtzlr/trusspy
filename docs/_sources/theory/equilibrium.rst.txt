Equilibrium
===========

This section covers the description of global system equilibrium equations and their linearization. For local (element-based) contributions see refer to :doc:`truss`.

System Equilibrium
------------------

The system vector of nodal equilibrium equations is formulated as the component-wise difference for each DOF of nodal element fixing forces :math:`\boldsymbol{r}(\boldsymbol{U})` and prescribed nodal external forces :math:`\boldsymbol{f} = \lambda~\boldsymbol{f}_0`. Given to the fact that we enforce the stiffness matrix to contain a positive sign for the partial derivative of the system fixing force column vector w.r.t to the nodal displacement system column vector the sign of the system equilibrium :math:`\boldsymbol{g}` in equation :eq:`equilibrium_1` is shifted.

.. math::
   :label: equilibrium_1

   -&\boldsymbol{g}(\boldsymbol{U},\lambda) &= \boldsymbol{r}(\boldsymbol{U}) - \lambda~\boldsymbol{f}_0  = \boldsymbol{0}\\
   ||(-)&\boldsymbol{g}(\boldsymbol{U},\lambda)|| &\le \varepsilon_{tol}
   
with

.. tabularcolumns:: |c|l|

.. table:: Overview of system parameters

   ====================================== =============================================================================
         Symbol                             Description
   ====================================== =============================================================================
   :math:`\boldsymbol{g}`                   system column vector of (nonlinear) nodal equilibrium equations
   :math:`\boldsymbol{r}`                   system column vector of nodal element fixing forces
   :math:`\boldsymbol{U}`                   system column vector of nodal displacements
   :math:`\lambda`                          load-proportionality-factor (LPF)
   :math:`\boldsymbol{f}_0`                 prescribed external nodal load vector (reference loadcase)
   :math:`\boldsymbol{\varepsilon}_{tol}`   tolerance vector for allowable numerical violation of the equilibrum state
   ====================================== =============================================================================
   
Linearized System Equlibrium
----------------------------

The linearized equilibrium equations for a given equlibrium state :math:`\boldsymbol{g}(\boldsymbol{U},\lambda)` are approximated with the help of a 1st order taylor - expansion:

.. math::

   -\boldsymbol{g}(\boldsymbol{U}+\boldsymbol{dU}, \lambda+d\lambda) &= \boldsymbol{r}(\boldsymbol{U}+\boldsymbol{dU}) &- (\lambda + d\lambda)\boldsymbol{f}_0 &&\\
                                                                    &\approx \left(\boldsymbol{r}(\boldsymbol{U}) + \frac{\partial \boldsymbol{r}}{\partial \boldsymbol{U}} \boldsymbol{dU} \right) &- (\lambda + d\lambda)\boldsymbol{f}_0 & &= \boldsymbol{0}\\
                                                                    &\approx \quad \phantom{-}\boldsymbol{r}(\boldsymbol{U}) - \lambda \boldsymbol{f}_0 &+ \frac{\partial \boldsymbol{r}}{\partial \boldsymbol{U}} \boldsymbol{dU} &- d\lambda~\boldsymbol{f}_0 &= \boldsymbol{0} \\
                                                                    &\approx \quad-\boldsymbol{g}(\boldsymbol{U}, \lambda) &+ \boldsymbol{K}_T(\boldsymbol{U})~\boldsymbol{dU} &- d\lambda~\boldsymbol{f}_0 &= \boldsymbol{0}
                                                                    
The linearized equilibrium equations may also be expressed as a simple linear equation system. The right hand side of this equation enforces a self-correction over incremental updates of the displacement vector.

.. math::

   \quad\boldsymbol{K}_T(\boldsymbol{U})~\boldsymbol{dU} - d\lambda~\boldsymbol{f}_0 = \boldsymbol{g}(\boldsymbol{U}, \lambda)
                                                                    
Newton-Rhapson Iteration and Update of Displacements
----------------------------------------------------
                                                                    
The linearized equilibrium equations may also be expressed as a simple linear equation system. The right hand side of this equation enforces a self-correction over incremental updates of the displacement vector.

.. math::

   \quad\boldsymbol{K}_T(\boldsymbol{U})~\boldsymbol{dU} - d\lambda~\boldsymbol{f}_0 = \boldsymbol{g}(\boldsymbol{U}, \lambda)
   
with 

.. math::

   \boldsymbol{U} &\leftarrow (\boldsymbol{U} + d\boldsymbol{U}) \\
   \lambda        &\leftarrow (\lambda        + d\lambda)