Global Assembly
===============

The fixing force contributions of each element `k` have to be assembled into a global system column vector of fixing forces.

.. math::
   :label: global_r
   
   \boldsymbol{r} = \bigcup_{k=1}^{n_{el}} \boldsymbol{r}_k
   
   
The same also applies for the tangent stiffness contributions `k` of each element into a global system stiffness matrix.

.. math::
   :label: global_K

   \boldsymbol{K}_{T} = \bigcup_{k=1}^{n_{el}} \boldsymbol{K}_{T,k}
   
Example
-------
The contributions of a truss `k=1` with it's connectivities `(A,E) = (1,3)` and a truss `k=2` with `(A,E) = (3,2)` to a global system with a total number of 3 nodes is assembled as follows: The system fixing force column vector :math:`\boldsymbol{r}` has a total length of `(nnodes*ndim)=(9)` (assuming `ndim=3`). The contributions of the trusses `k=1` and `k=2` are then assembled by their connectivity information `A` and `E`.

.. math::

   \boldsymbol{r} = \left[\begin{array}{c}
                            \boldsymbol{r}_1 \\
                            \boldsymbol{r}_2 \\
                            \boldsymbol{r}_3 \\
                            \end{array}\right]

.. math::

   \boldsymbol{r} &= \quad \boldsymbol{r}_{k=1} &+ \quad \boldsymbol{r}_{k=2} \\
   \boldsymbol{r} &= \left[\begin{array}{c}
                            \boldsymbol{r}_{A=1} \\
                            \boldsymbol{0}       \\
                            \boldsymbol{r}_{E=3} \\
                            \end{array}\right]              &+
                                                                \left[\begin{array}{c}
                                                                \boldsymbol{0}       \\
                                                                \boldsymbol{r}_{E=2} \\
                                                                \boldsymbol{r}_{A=3} \\
                                                                \end{array}\right]
                            
The total system fixing force column vector of all elements `k` is finally obtained with equation :eq:`global_r`. For the stiffness contribution the same method applies to `A` end `E`. For example, the submatrix `(AE)` of element `k` is assembled at system position `(13)`.

.. math::

   \boldsymbol{K}_{T~(9,9)} = \begin{bmatrix}
                              \boldsymbol{K}_{11} & \boldsymbol{K}_{12} & \boldsymbol{K}_{13}\\
                              \boldsymbol{K}_{21} & \boldsymbol{K}_{22} & \boldsymbol{K}_{23}\\
                              \boldsymbol{K}_{31} & \boldsymbol{K}_{32} & \boldsymbol{K}_{33}
                              \end{bmatrix}
                              
The total system stiffness matrix of all elements `k` is again obtained with equation :eq:`global_K`.
                                              
.. math::

   \boldsymbol{K}_T &= \quad \quad \quad \boldsymbol{K}_{T,k=1} &+ \quad \quad \quad \boldsymbol{K}_{T,k=2} \\
   \boldsymbol{K}_T &= \begin{bmatrix}
                              \boldsymbol{K}_{k=1,AA} & \boldsymbol{0} & \boldsymbol{K}_{k=1,AE}\\
                              \boldsymbol{0} & \boldsymbol{0} & \boldsymbol{0}\\
                              \boldsymbol{K}_{k=1,EA} & \boldsymbol{0} & \boldsymbol{K}_{k=1,AA}
                      \end{bmatrix} &+
                      \begin{bmatrix}
                              \boldsymbol{0} & \boldsymbol{0}          & \boldsymbol{0}\\
                              \boldsymbol{0} & \boldsymbol{K}_{k=2,EE} & \boldsymbol{K}_{k=2,EA}\\
                              \boldsymbol{0} & \boldsymbol{K}_{k=2,AE} & \boldsymbol{K}_{k=2,AA}
                      \end{bmatrix}