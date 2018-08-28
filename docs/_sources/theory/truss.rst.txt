Truss Element
=============

This section describes the **Kinematics** and **Constitution** of a Truss element :class:`trusspy.elements.element_definition.truss`. A Truss `k` is connected to a system by it's begin (`A`) and end (`E`) nodes. The cross section remains constant over the element length. It has three coordinates and three degrees of freedom.

.. figure:: truss.*
   :align: center
   :width: 90%
   :alt: Arbitrary deformed (stretched and rotated) truss `k` and it's contribution to the equilibrium on nodes A and E.
   
   Arbitrary deformed (stretched and rotated) truss k and it's contribution to the equilibrium on nodes A and E.

Kinematics
----------

For a truss element the stretch may be calculated as

.. math::

   \Lambda = \frac{l}{L} = \sqrt{1 + 2 \left(\frac{\boldsymbol{\Delta X}}{L}\right)^T \left(\frac{\boldsymbol{\Delta U}}{L}\right) + \left(\frac{\boldsymbol{\Delta U}}{L}\right)^T \left(\frac{\boldsymbol{\Delta U}}{L}\right)}

which follows from

.. math::

   l^2 &= \boldsymbol{\Delta x}^T \boldsymbol{\Delta x} \\
   L^2 &= \boldsymbol{\Delta X}^T \boldsymbol{\Delta X}
   
and enables the Biot strain measure:

.. math::

   E_{11} = \Lambda - 1
   

Constitution
------------

The normal force of a truss depends directly on the geometric exactly defined strain measure :math:`E_{11}`. For the general case of a nonlinear material behaviour the normal force is defined as

.. math::

   N = S_{11}(E_{11})~A + N_0
   
and the derivative

.. math::

   \frac{\partial N}{\partial E_{11}} = \frac{\partial S_{11}(E_{11})}{\partial E_{11}}~A
   
For the case of a linear elastic material this reduces to

.. math::

   S_{11}(E_{11}) &= E~E_{11} \\
   N              &= EA~E_{11} + N_0 \\
   \frac{\partial N}{\partial E_{11}} &= EA
   
Kinetics
--------

The (nonlinear) fixing force column vector with dimension `(ndim)` may be expressed as a function of the elemental force :math:`N_k` and the deformed unit vector :math:`\boldsymbol{n}_k`.

.. math::

   \boldsymbol{r}_k = \begin{bmatrix}
                       \boldsymbol{r}_A \\
                       \boldsymbol{r}_E
                    \end{bmatrix}            = N_k  \begin{pmatrix}
                                                    -\boldsymbol{n}_k \\
                                                    \phantom{-}\boldsymbol{n}_k
                                                    \end{pmatrix}
                                                 
Stiffness Matrix
----------------

The elemental stiffness matrix of a truss has dimensions `(2*ndim,2*ndim)` and contains partial derivatives of the element fixing forces w.r.t to the displacements. The matrix components for the case of `ndim=3` results in

.. math::

   \boldsymbol{K}_{k~(6,6)} = \left[\begin{array}{ccc:ccc}
                                \frac{\partial r_{A,x}}{\partial U_{A,x}} & \frac{\partial r_{A,y}}{\partial U_{A,x}} & \frac{\partial r_{A,z}}{\partial U_{A,x}} & \frac{\partial r_{E,x}}{\partial U_{A,x}} & \frac{\partial r_{E,y}}{\partial U_{A,x}} & \frac{\partial r_{E,z}}{\partial U_{A,x}}\\
                                \frac{\partial r_{A,x}}{\partial U_{A,y}} & \frac{\partial r_{A,y}}{\partial U_{A,y}} & \frac{\partial r_{A,z}}{\partial U_{A,y}} & \frac{\partial r_{E,x}}{\partial U_{A,y}} & \frac{\partial r_{E,y}}{\partial U_{A,y}} & \frac{\partial r_{E,z}}{\partial U_{A,y}}\\
                                \frac{\partial r_{A,x}}{\partial U_{A,z}} & \frac{\partial r_{A,z}}{\partial U_{A,z}} & \frac{\partial r_{A,z}}{\partial U_{A,z}} & \frac{\partial r_{E,x}}{\partial U_{A,z}} & \frac{\partial r_{E,y}}{\partial U_{A,z}} & \frac{\partial r_{E,z}}{\partial U_{A,z}}\\ \hdashline
                                \frac{\partial r_{A,x}}{\partial U_{E,x}} & \frac{\partial r_{A,y}}{\partial U_{E,x}} & \frac{\partial r_{A,z}}{\partial U_{E,x}} & \frac{\partial r_{E,x}}{\partial U_{E,x}} & \frac{\partial r_{E,y}}{\partial U_{E,x}} & \frac{\partial r_{E,z}}{\partial U_{E,x}}\\
                                \frac{\partial r_{A,x}}{\partial U_{E,y}} & \frac{\partial r_{A,y}}{\partial U_{E,y}} & \frac{\partial r_{A,z}}{\partial U_{E,y}} & \frac{\partial r_{E,x}}{\partial U_{E,y}} & \frac{\partial r_{E,y}}{\partial U_{E,y}} & \frac{\partial r_{E,z}}{\partial U_{E,y}}\\
                                \frac{\partial r_{A,x}}{\partial U_{E,z}} & \frac{\partial r_{A,z}}{\partial U_{E,z}} & \frac{\partial r_{A,z}}{\partial U_{E,z}} & \frac{\partial r_{E,x}}{\partial U_{E,z}} & \frac{\partial r_{E,y}}{\partial U_{E,z}} & \frac{\partial r_{E,z}}{\partial U_{E,z}}
                              \end{array}\right]

For a truss the stiffness matrix may be divided into four block matrices of the same components but with different signs.

.. math::

   \boldsymbol{K}_{k~(6,6)} = \begin{bmatrix}
                             \boldsymbol{K}_{AA} & \boldsymbol{K}_{AE}\\
                             \boldsymbol{K}_{EA} & \boldsymbol{K}_{EE}
                          \end{bmatrix}                                 =  \begin{pmatrix}
                                                                              \phantom{-}\boldsymbol{K}_{EE} & -\boldsymbol{K}_{EE}\\
                                                                             -\boldsymbol{K}_{EE} &  \phantom{-}\boldsymbol{K}_{EE}
                                                                          \end{pmatrix}
                                                                          
Whereas a change in the fixing force vector at the end node `E` w.r.t. a small change of the displacements at node `E` is defined as the tangent stiffnes `EE`. 

.. math::

   \boldsymbol{K}_{EE} &= \frac{\partial \boldsymbol{r}_E}{\partial \boldsymbol{U}_E} \\
   \boldsymbol{K}_{EE} &= \frac{A}{L} ~ \frac{\partial S_{11}(E_{11})}{\partial E_{11}} \boldsymbol{n} \otimes \boldsymbol{n} + \frac{N}{l} \left( \boldsymbol{1} - \boldsymbol{n} \otimes \boldsymbol{n} \right)
   
with the identity matrix :math:`\boldsymbol{1}`

.. math::

   \begin{bmatrix}
   1 & 0 & 0\\
   0 & 1 & 0\\
   0 & 0 & 1\\
   \end{bmatrix}
   

   
Continue to :doc:`assembly`.