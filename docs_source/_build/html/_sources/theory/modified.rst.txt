Extended system equations
=========================

In order to solve the equilibrium equations a equation system with `n+1` DOF's will be formulated. The extra degree of freedom arises from the external load - scale parameter, also denoted as load-proportionality-factor :math:`\lambda`, which will be appended to the system vector :math:`\boldsymbol{U}`. The transformation will be shown for both the equilibrium and tangent stiffness. This extension is performed by appending the LPF factor :math:`\lambda` to the system displacement column vector :math:`\boldsymbol{U}`. This new combined system column vector is called :math:`\boldsymbol{V}`.

.. math::

   \boldsymbol{V} = \left[\begin{array}
                             ~ \\
                             \boldsymbol{U} \\
                             ~ \\ \hdashline
                             {\lambda}
                    \end{array}\right]

Extended system equilibrium
---------------------------

The extended system equilibrium is expanded by one extra equation, which is also referred to as **control equation** :math:`{g}_{C}(\boldsymbol{V})`.

.. math::

   -\boldsymbol{g}_{extended} = \left[\begin{array}
                                 ~ \\
                                 -\boldsymbol{g}(\boldsymbol{V}) \\
                                 ~ \\ \hdashline
                                 -{g}_{C}(\boldsymbol{V})
                               \end{array}\right]
                          
                          
This extra control equation is formulated as a linear constraint to limit the control component `j`.

.. math::

   -{g}_{C} = {V}_j - {V}_{j,max}
   
With this definition the modified system equilibrium becomes
   
.. math::

   -&\boldsymbol{g}_{extended}(\boldsymbol{V}) &= \left[\begin{array}
                             ~ \\
                             -\boldsymbol{g}(\boldsymbol{V}) \\
                             ~ \\ \hdashline
                             -{g}_{C}(\boldsymbol{V})
                             \end{array}\right] = \left[\begin{array}
                                               ~ \\
                                               \boldsymbol{r}(\boldsymbol{U}) - \lambda~\boldsymbol{f}_0 \\
                                               ~ \\ \hdashline
                                               {V}_j - {V}_{j,max}
                                             \end{array}\right] = \boldsymbol{0} \\
   ||(-)&\boldsymbol{g}_{extended}(\boldsymbol{V})|| &\le \varepsilon_{tol}

Extended system tangent stiffness matrix
----------------------------------------

To illustrate the components of the partial derivatives of the control equation we formulate the first order derivative of the control equation for small changes in :math:`\boldsymbol{dU}` and :math:`d\lambda` at a given state :math:`(\boldsymbol{U},\lambda)`.

.. math::

   -\boldsymbol{g}_{C}(\boldsymbol{V}+\boldsymbol{dV}) &= &-{g}_{C}(\boldsymbol{V}) &- \quad {dg}_{C}(\boldsymbol{V}) &= \\
   &= {V}_j &- {V}_{j,max} &- \frac{\partial ({V}_j - {V}_{j,max})}{\partial \boldsymbol{V}}~\boldsymbol{dV} &= 0
   
and therefore

.. math::

   \frac{\partial {V}_j}{\partial \boldsymbol{V}}~\boldsymbol{dV} = {g}_{C}(\boldsymbol{V})
   
with

.. math::

   {dV}_j &= \frac{\partial {V}_j}{\partial \boldsymbol{U}} ~ &\boldsymbol{dU} &+ \frac{\partial {V}_j}{\partial \lambda} ~ &d \lambda \\
   {dV}_j &= \boldsymbol{q}_{c,\boldsymbol{U}} ~ &\boldsymbol{dU} &+ {q}_{c,\lambda}  ~ &d \lambda
   
The modified tangent stiffness :math:`\boldsymbol{K}_{T,extended}` is now calculated w.r.t. the modified system vector :math:`\boldsymbol{V}`.
                             
.. math::
                             
   \boldsymbol{K}_{T,extended} = \left[\begin{array}{ccc:c}
                                        ~ & ~ & ~ & ~ \\
                                        ~ & \frac{\partial \boldsymbol{r}}{\partial \boldsymbol{U}} & ~ & -\boldsymbol{f}_0 \\
                                        ~ & ~ & ~ & ~ \\ \hdashline
                                        ~ & \frac{\partial {g}_{C}}{\partial \boldsymbol{U}} & ~ & \frac{\partial {g}_{C}}{\partial \lambda}
                             \end{array}\right]
                             
.. math::                           
                             
   \boldsymbol{K}_{T,extended} = \left[\begin{array}{ccc:c}
                                        ~ & ~ & ~ & ~ \\
                                        ~ & \boldsymbol{K}_{T} & ~ & -\boldsymbol{f}_0 \\
                                        ~ & ~ & ~ & ~ \\ \hdashline
                                        ~ & \boldsymbol{q}_{C,\boldsymbol{U}} & ~ & {q}_{C,\lambda}
                             \end{array}\right]
                             
with the partial derivatives of the control equation:

.. math::

   \boldsymbol{q}_{C,\boldsymbol{U}} &= \frac{\partial {g}_{C}(\boldsymbol{U},\lambda)}{\partial \boldsymbol{U}} \\
   \boldsymbol{q}_{C,\lambda}        &= \frac{\partial {g}_{C}(\boldsymbol{U},\lambda)}{\partial \lambda}
   
The combined partial derivate of the control equation may be expressed as:

.. math::

   \boldsymbol{q}_{C} = \begin{bmatrix}
                          \boldsymbol{q}_{C,\boldsymbol{U}} & {q}_{C,\lambda}
                        \end{bmatrix}
                        
and is a system row vector with a length of `nDOF+1` entries filled with zeros, except for the `j`-th entry (control component), which is one. Let's assume we have a system of 6 DOF and the control component is identified to `j=4` then :math:`\boldsymbol{q}_{C}` looks like

.. math::

   \boldsymbol{q}_{C} = \begin{bmatrix}
                          0 & 0 & 0 & 1 & 0 & 0 & 0
                        \end{bmatrix}
                        
Summary
-------

The final equation system for the :doc:`pathtrace` may now be formulated as

.. math::

     \boldsymbol{K}_{T,extended} ~ \boldsymbol{dV} = \boldsymbol{g}_{extended}(\boldsymbol{V})
     
and in detail

.. math::
                             
   \begin{bmatrix}
     \boldsymbol{K}_{T}                & -\boldsymbol{f}_0 \\
     \boldsymbol{q}_{c,\boldsymbol{U}} &  \boldsymbol{q}_{c,\lambda}
   \end{bmatrix} \begin{bmatrix}
                                               \boldsymbol{dU} \\
                                               d{\lambda}
                                           \end{bmatrix} = \begin{bmatrix}
                                                              \boldsymbol{g} \\
                                                              {g}_{C}
                                                           \end{bmatrix}
                                                           
The control component :math:`j` is defined as the **signed index of the biggest component** of the incremental system vector :math:`\boldsymbol{dV}`. This component remains fixed during all newton-iterations inside an increment. To initialize the control component :math:`j` the linear equation system is solved with an incremental load proportionality factor :math:`d\lambda`.

.. math::
                             
     \boldsymbol{K}_{T} ~ \boldsymbol{dU} &= d \lambda \boldsymbol{f}_0 \\
     \rightarrow \boldsymbol{dU} &= \dots
     
.. math:: 
     
     j = \text{index} [\max (|\boldsymbol{dU}|)] \cdot \text{sign} [\max (|\boldsymbol{dU}|)]
