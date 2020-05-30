<script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>

         _____                  ______      
        |_   _|                 | ___ \     
          | |_ __ _   _ ___ ___ | |_/ /   _ 
          | | '__| | | / __/ __||  __/ | | |
          | | |  | |_| \__ \__ \| |  | |_| |
          \_/_|   \__,_|___/___/\_|   \__, |
                                       __/ |
                                      |___/ 
        
        TrussPy - Object Oriented Truss Solver for Python
                  Version 2018.08 (Build 20180829)

        Author: Dutzler A.
                Graz University of Technology, 2018
                
        TrussPy  Copyright (C) 2018  Andreas Dutzler
        This program comes with ABSOLUTELY NO WARRANTY; 
        for details type `trusspy.show_w()'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `trusspy.show_c()' for details.
        

# Initialize Model
* loading Managers

    - finished.


# Model Summary
    Analysis Dimension      "ndim": 3
    Number of Nodes       "nnodes": 9
    Number of Elements    "nelems": 12
 
    System DOF              "ndof": 27
    active DOF             "ndof1": 9
    locked DOF             "ndof2": 18
 
    active DOF          "nproDOF1": [18 19 20 21 22 23 24 25 26]
    fixed  DOF          "nproDOF0": [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17]
\pagebreak
 
# Run Simulation

## Summary of Analysis Parameters
|Description                          |Parameter|Value|
|:------------------------------------|:--------|:--|
|Maximum increments                   |   `incs`| 132 |
|Maximum increment recycles           |   `cycl`| 4 |
|Maximum Newton-Rhapson iterations    |   `nfev`| 8 |
|Maximum incremental displacement     |     `du`| 0.05 |
|Maximum incremental LPF              |   `dlpf`| 0.05 |
|Initial control component            |     `j0`| LPF|
|Locked control component             |`j_fixed`| False |
|Maximum incremental overshoot        |  `dxtol`| 1.000001 |
|Tolerance for x                      |   `xtol`| 8 |
|Tolerance for f                      |   `ftol`| 8 |


## Step 1
* i(1) is index with 1st-biggest component in abs(Dx/Dx,max).
* i(2) is index with 2nd-biggest component in abs(Dx/Dx,max).
* i(3) is index with 3rd-biggest component in abs(Dx/Dx,max).
* i(4) is index with 4th-biggest component in abs(Dx/Dx,max).
* Value(i) is value of i-th component in abs(Dx/Dx,max).
$$\text{Value}_i = \left|\frac{D_x}{D_{x,max}}\right|_i$$

### Increment 1
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  10   |1.469e-02|   9|      -2|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.221e-06|    |        |    |        |    |        |
|     |   2  |       |4.834e-14|    |        |    |        |    |        |
|     |   3  |       |3.658e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.658e-16|   9| -1.0000|   3| -1.0000|  10|  0.3890|

* final LPF:    0.01945

### Increment 2
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.695e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.030e-06|    |        |    |        |    |        |
|     |   2  |       |1.679e-13|    |        |    |        |    |        |
|     |   3  |       |3.262e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |3.262e-16|   3| -1.0000|   9| -1.0000|  10|  0.3365|

* final LPF:    0.03628

### Increment 3
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.957e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.489e-06|    |        |    |        |    |        |
|     |   2  |       |8.534e-13|    |        |    |        |    |        |
|     |   3  |       |3.683e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |3.683e-16|   3| -1.0000|   9| -1.0000|   1|  0.3601|

* final LPF:    0.05013

### Increment 4
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |3.254e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.992e-06|    |        |    |        |    |        |
|     |   2  |       |5.121e-12|    |        |    |        |    |        |
|     |   3  |       |2.989e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.989e-16|   9| -1.0000|   3| -1.0000|   7| -0.4249|

* final LPF:    0.06059

### Increment 5
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.580e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.892e-06|    |        |    |        |    |        |
|     |   2  |       |1.887e-11|    |        |    |        |    |        |
|     |   3  |       |2.966e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.966e-16|   9| -1.0000|   3| -1.0000|   7| -0.5087|

* final LPF:     0.0671

### Increment 6
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.899e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.497e-05|    |        |    |        |    |        |
|     |   2  |       |4.391e-11|    |        |    |        |    |        |
|     |   3  |       |1.692e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |1.692e-16|   3| -1.0000|   9| -1.0000|   1|  0.6186|

* final LPF:    0.06898

### Increment 7
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |4.131e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.934e-05|    |        |    |        |    |        |
|     |   2  |       |6.039e-11|    |        |    |        |    |        |
|     |   3  |       |2.950e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.950e-16|   9| -1.0000|   3| -1.0000|   7| -0.7612|

* final LPF:    0.06544

### Increment 8
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |4.133e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.854e-05|    |        |    |        |    |        |
|     |   2  |       |3.862e-11|    |        |    |        |    |        |
|     |   3  |       |4.421e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.421e-16|   9| -1.0000|   3| -1.0000|   7| -0.9354|

* final LPF:    0.05584

### Increment 9
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.820e-03|   1|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.811e-06|    |        |    |        |    |        |
|     |   2  |       |2.959e-12|    |        |    |        |    |        |
|     |   3  |       |1.274e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   1   |1.274e-16|   1|  1.0000|   7| -1.0000|   3| -0.9012|

* final LPF:    0.04211

### Increment 10
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   1   |2.596e-03|   1|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.208e-06|    |        |    |        |    |        |
|     |   2  |       |1.208e-11|    |        |    |        |    |        |
|     |   3  |       |1.402e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   1   |1.402e-16|   7| -1.0000|   1|  1.0000|   9| -0.8094|

* final LPF:     0.0267

### Increment 11
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -7   |2.486e-03|   1|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.503e-06|    |        |    |        |    |        |
|     |   2  |       |1.353e-11|    |        |    |        |    |        |
|     |   3  |       |2.456e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   1   |2.456e-16|   1|  1.0000|   7| -1.0000|   9| -0.7750|

* final LPF:    0.01083

### Increment 12
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   1   |2.880e-03|   7|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.731e-06|    |        |    |        |    |        |
|     |   2  |       |1.165e-11|    |        |    |        |    |        |
|     |   3  |       |3.423e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -7   |3.423e-16|   1|  1.0000|   7| -1.0000|   9| -0.7853|

* final LPF:  -0.004609

### Increment 13
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   1   |3.484e-03|   7|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.954e-06|    |        |    |        |    |        |
|     |   2  |       |1.311e-11|    |        |    |        |    |        |
|     |   3  |       |1.763e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -7   |1.763e-16|   7| -1.0000|   1|  1.0000|   3| -0.8364|

* final LPF:   -0.01888

### Increment 14
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -7   |4.213e-03|   7|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.603e-06|    |        |    |        |    |        |
|     |   2  |       |3.434e-11|    |        |    |        |    |        |
|     |   3  |       |5.280e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -7   |5.280e-16|   1|  1.0000|   7| -1.0000|   3| -0.9319|

* final LPF:   -0.03127

### Increment 15
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   1   |5.104e-03|   1|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.796e-05|    |        |    |        |    |        |
|     |   2  |       |1.844e-10|    |        |    |        |    |        |
|     |   3  |       |3.735e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   1   |3.735e-16|   9| -1.0857|   3| -1.0857|   7| -1.0000|

* recycling increment

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.134e-03|    |        |    |        |    |        |
|     |   2  |       |3.647e-05|    |        |    |        |    |        |
|     |   3  |       |1.470e-09|    |        |    |        |    |        |
|     |   4  |       |3.244e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  2  |   4  |  -9   |3.244e-16|   9| -1.0000|   3| -1.0000|   1|  0.9274|

* final LPF:   -0.04038

### Increment 16
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |4.493e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.619e-05|    |        |    |        |    |        |
|     |   2  |       |7.015e-10|    |        |    |        |    |        |
|     |   3  |       |2.864e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.864e-16|   3| -1.0000|   9| -1.0000|   7| -0.7837|

* final LPF:   -0.04566

### Increment 17
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |3.868e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.803e-05|    |        |    |        |    |        |
|     |   2  |       |3.080e-10|    |        |    |        |    |        |
|     |   3  |       |7.444e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |7.444e-16|   3| -1.0000|   9| -1.0000|   1|  0.6548|

* final LPF:   -0.04777

### Increment 18
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |3.337e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.244e-05|    |        |    |        |    |        |
|     |   2  |       |1.367e-10|    |        |    |        |    |        |
|     |   3  |       |6.384e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |6.384e-16|   3| -1.0000|   9| -1.0000|   1|  0.5414|

* final LPF:   -0.04734

### Increment 19
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.910e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.786e-06|    |        |    |        |    |        |
|     |   2  |       |6.417e-11|    |        |    |        |    |        |
|     |   3  |       |1.538e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |1.538e-16|   9| -1.0000|   3| -1.0000|   7| -0.4417|

* final LPF:    -0.0449

### Increment 20
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.577e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.421e-06|    |        |    |        |    |        |
|     |   2  |       |3.252e-11|    |        |    |        |    |        |
|     |   3  |       |2.869e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.869e-16|   9| -1.0000|   3| -1.0000|   1|  0.3534|

* final LPF:   -0.04086

### Increment 21
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.319e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.878e-06|    |        |    |        |    |        |
|     |   2  |       |1.796e-11|    |        |    |        |    |        |
|     |   3  |       |7.148e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |7.148e-16|   9| -1.0000|   3| -1.0000|   6| -0.3873|

* final LPF:   -0.03555

### Increment 22
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.122e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.862e-06|    |        |    |        |    |        |
|     |   2  |       |1.086e-11|    |        |    |        |    |        |
|     |   3  |       |3.306e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |3.306e-16|   9| -1.0000|   3| -1.0000|   6| -0.4347|

* final LPF:   -0.02923

### Increment 23
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.972e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.188e-06|    |        |    |        |    |        |
|     |   2  |       |7.195e-12|    |        |    |        |    |        |
|     |   3  |       |1.934e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |1.934e-16|   3| -1.0000|   9| -1.0000|   6| -0.4769|

* final LPF:    -0.0221

### Increment 24
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.863e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.747e-06|    |        |    |        |    |        |
|     |   2  |       |5.229e-12|    |        |    |        |    |        |
|     |   3  |       |1.925e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |1.925e-16|   9| -1.0000|   3| -1.0000|   6| -0.5156|

* final LPF:   -0.01433

### Increment 25
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.788e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.470e-06|    |        |    |        |    |        |
|     |   2  |       |4.169e-12|    |        |    |        |    |        |
|     |   3  |       |3.409e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.409e-16|   3| -1.0000|   9| -1.0000|   6| -0.5521|

* final LPF:  -0.006048

### Increment 26
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.744e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.320e-06|    |        |    |        |    |        |
|     |   2  |       |3.651e-12|    |        |    |        |    |        |
|     |   3  |       |5.211e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |5.211e-16|   9| -1.0000|   3| -1.0000|   6| -0.5876|

* final LPF:   0.002648

### Increment 27
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.732e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.279e-06|    |        |    |        |    |        |
|     |   2  |       |3.521e-12|    |        |    |        |    |        |
|     |   3  |       |6.747e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |6.747e-16|   9| -1.0000|   3| -1.0000|   6| -0.6233|

* final LPF:    0.01166

### Increment 28
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.753e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.345e-06|    |        |    |        |    |        |
|     |   2  |       |3.758e-12|    |        |    |        |    |        |
|     |   3  |       |2.514e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.514e-16|   9| -1.0000|   3| -1.0000|   6| -0.6602|

* final LPF:    0.02092

### Increment 29
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.810e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.535e-06|    |        |    |        |    |        |
|     |   2  |       |4.468e-12|    |        |    |        |    |        |
|     |   3  |       |5.671e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |5.671e-16|   9| -1.0000|   3| -1.0000|   6| -0.6993|

* final LPF:    0.03035

### Increment 30
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.910e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.889e-06|    |        |    |        |    |        |
|     |   2  |       |5.983e-12|    |        |    |        |    |        |
|     |   3  |       |3.798e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.798e-16|   3| -1.0000|   9| -1.0000|   6| -0.7421|

* final LPF:    0.03987

### Increment 31
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.062e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.492e-06|    |        |    |        |    |        |
|     |   2  |       |9.144e-12|    |        |    |        |    |        |
|     |   3  |       |2.492e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.492e-16|   3| -1.0000|   9| -1.0000|   6| -0.7901|

* final LPF:    0.04939

### Increment 32
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.281e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.504e-06|    |        |    |        |    |        |
|     |   2  |       |1.626e-11|    |        |    |        |    |        |
|     |   3  |       |1.718e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |1.718e-16|   9| -1.0000|   3| -1.0000|   6| -0.8457|

* final LPF:     0.0588

### Increment 33
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.589e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.260e-06|    |        |    |        |    |        |
|     |   2  |       |3.451e-11|    |        |    |        |    |        |
|     |   3  |       |7.858e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |7.858e-16|   3| -1.0000|   9| -1.0000|   6| -0.9119|

* final LPF:    0.06797

### Increment 34
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |3.022e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.509e-06|    |        |    |        |    |        |
|     |   2  |       |9.086e-11|    |        |    |        |    |        |
|     |   3  |       |3.881e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.881e-16|   9| -1.0000|   3| -1.0000|   6| -0.9940|

* final LPF:    0.07666

### Increment 35
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.647e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.836e-06|    |        |    |        |    |        |
|     |   2  |       |1.284e-11|    |        |    |        |    |        |
|     |   3  |       |4.951e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.951e-16|   6| -1.0000|   9| -0.9131|   3| -0.9131|

* final LPF:    0.08389

### Increment 36
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.376e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.506e-06|    |        |    |        |    |        |
|     |   2  |       |1.067e-11|    |        |    |        |    |        |
|     |   3  |       |3.484e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.484e-16|   6| -1.0000|   3| -0.8210|   9| -0.8210|

* final LPF:    0.08946

### Increment 37
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.398e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.349e-06|    |        |    |        |    |        |
|     |   2  |       |9.610e-12|    |        |    |        |    |        |
|     |   3  |       |4.872e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.872e-16|   6| -1.0000|   9| -0.7295|   3| -0.7295|

* final LPF:    0.09319

### Increment 38
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.414e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.327e-06|    |        |    |        |    |        |
|     |   2  |       |9.322e-12|    |        |    |        |    |        |
|     |   3  |       |5.908e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.908e-16|   6| -1.0000|   9| -0.6380|   3| -0.6380|

* final LPF:    0.09496

### Increment 39
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.416e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.419e-06|    |        |    |        |    |        |
|     |   2  |       |9.699e-12|    |        |    |        |    |        |
|     |   3  |       |3.826e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.826e-16|   6| -1.0000|   3| -0.5463|   9| -0.5463|

* final LPF:    0.09463

### Increment 40
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.402e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.619e-06|    |        |    |        |    |        |
|     |   2  |       |1.078e-11|    |        |    |        |    |        |
|     |   3  |       |3.776e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.776e-16|   6| -1.0000|   7|  0.4782|   1| -0.4782|

* final LPF:     0.0921

### Increment 41
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.368e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.931e-06|    |        |    |        |    |        |
|     |   2  |       |1.277e-11|    |        |    |        |    |        |
|     |   3  |       |3.159e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.159e-16|   6| -1.0000|   1| -0.4798|   7|  0.4798|

* final LPF:    0.08728

### Increment 42
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.317e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.378e-06|    |        |    |        |    |        |
|     |   2  |       |1.607e-11|    |        |    |        |    |        |
|     |   3  |       |5.086e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.086e-16|   6| -1.0000|   1| -0.4826|   7|  0.4826|

* final LPF:    0.08014

### Increment 43
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.255e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.001e-06|    |        |    |        |    |        |
|     |   2  |       |2.155e-11|    |        |    |        |    |        |
|     |   3  |       |2.545e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |2.545e-16|   6| -1.0000|   1| -0.4872|   7|  0.4872|

* final LPF:    0.07067

### Increment 44
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.195e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.879e-06|    |        |    |        |    |        |
|     |   2  |       |3.097e-11|    |        |    |        |    |        |
|     |   3  |       |3.673e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.673e-16|   6| -1.0000|   7|  0.4935|   1| -0.4935|

* final LPF:     0.0589

### Increment 45
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.156e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.158e-06|    |        |    |        |    |        |
|     |   2  |       |4.841e-11|    |        |    |        |    |        |
|     |   3  |       |4.961e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.961e-16|   6| -1.0000|   7|  0.5012|   1| -0.5012|

* final LPF:    0.04491

### Increment 46
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.171e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.113e-05|    |        |    |        |    |        |
|     |   2  |       |8.456e-11|    |        |    |        |    |        |
|     |   3  |       |2.640e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |2.640e-16|   6| -1.0000|   1| -0.5094|   7|  0.5094|

* final LPF:    0.02882

### Increment 47
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.283e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.440e-05|    |        |    |        |    |        |
|     |   2  |       |1.728e-10|    |        |    |        |    |        |
|     |   3  |       |6.674e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |6.674e-16|   6| -1.0000|   7|  0.5165|   1| -0.5165|

* final LPF:    0.01077

### Increment 48
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.562e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.048e-05|    |        |    |        |    |        |
|     |   2  |       |4.469e-10|    |        |    |        |    |        |
|     |   3  |       |3.527e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.527e-16|   6| -1.0000|   1| -0.5198|   7|  0.5198|

* final LPF:   -0.00907

### Increment 49
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |4.125e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.380e-05|    |        |    |        |    |        |
|     |   2  |       |1.683e-09|    |        |    |        |    |        |
|     |   3  |       |1.550e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |1.550e-16|   6| -1.0000|   9|  0.6207|   3|  0.6207|

* final LPF:   -0.03049

### Increment 50
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |5.225e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.221e-05|    |        |    |        |    |        |
|     |   2  |       |1.225e-08|    |        |    |        |    |        |
|     |   3  |       |7.314e-16|    |        |    |        |    |        |
|     |   4  |       |4.660e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   5  |  -6   |4.660e-16|   6| -1.0000|   9|  0.8726|   3|  0.8726|

* final LPF:   -0.05329

### Increment 51
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |7.619e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.435e-05|    |        |    |        |    |        |
|     |   2  |       |8.325e-10|    |        |    |        |    |        |
|     |   3  |       |2.398e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |2.398e-16|   3|  1.0000|   9|  1.0000|   6| -0.8039|

* final LPF:   -0.07256

### Increment 52
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |5.697e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.437e-05|    |        |    |        |    |        |
|     |   2  |       |5.445e-10|    |        |    |        |    |        |
|     |   3  |       |2.698e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.698e-16|   9|  1.0000|   3|  1.0000|   6| -0.5495|

* final LPF:   -0.08633

### Increment 53
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |4.935e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.953e-05|    |        |    |        |    |        |
|     |   2  |       |3.790e-10|    |        |    |        |    |        |
|     |   3  |       |2.459e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |2.459e-16|   9|  1.0000|   3|  1.0000|   6| -0.3466|

* final LPF:   -0.09556

### Increment 54
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |4.395e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.571e-05|    |        |    |        |    |        |
|     |   2  |       |2.381e-10|    |        |    |        |    |        |
|     |   3  |       |2.063e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.063e-16|   3|  1.0000|   9|  1.0000|   6| -0.1732|

* final LPF:    -0.1009

### Increment 55
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |3.943e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.193e-05|    |        |    |        |    |        |
|     |   2  |       |1.212e-10|    |        |    |        |    |        |
|     |   3  |       |3.798e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.798e-16|   9|  1.0000|   3|  1.0000|   7| -0.1047|

* final LPF:    -0.1027

### Increment 56
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |3.525e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.268e-06|    |        |    |        |    |        |
|     |   2  |       |4.760e-11|    |        |    |        |    |        |
|     |   3  |       |2.132e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.132e-16|   3|  1.0000|   9|  1.0000|   7| -0.1573|

* final LPF:    -0.1016

### Increment 57
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |3.129e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.156e-06|    |        |    |        |    |        |
|     |   2  |       |1.534e-11|    |        |    |        |    |        |
|     |   3  |       |4.443e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |4.443e-16|   9|  1.0000|   3|  1.0000|   6|  0.2158|

* final LPF:   -0.09768

### Increment 58
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |2.757e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.884e-06|    |        |    |        |    |        |
|     |   2  |       |4.939e-12|    |        |    |        |    |        |
|     |   3  |       |2.114e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.114e-16|   9|  1.0000|   3|  1.0000|   6|  0.3044|

* final LPF:   -0.09149

### Increment 59
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |2.414e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.504e-06|    |        |    |        |    |        |
|     |   2  |       |1.441e-12|    |        |    |        |    |        |
|     |   3  |       |8.442e-17|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |8.442e-17|   3|  1.0000|   9|  1.0000|   6|  0.3750|

* final LPF:   -0.08329

### Increment 60
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |2.103e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.308e-07|    |        |    |        |    |        |
|     |   2  |       |5.275e-13|    |        |    |        |    |        |
|     |   3  |       |3.342e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.342e-16|   9|  1.0000|   3|  1.0000|   6|  0.4300|

* final LPF:    -0.0734

### Increment 61
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.825e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.756e-07|    |        |    |        |    |        |
|     |   2  |       |3.519e-13|    |        |    |        |    |        |
|     |   3  |       |1.923e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |1.923e-16|   9|  1.0000|   3|  1.0000|   6|  0.4721|

* final LPF:   -0.06211

### Increment 62
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.581e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.443e-07|    |        |    |        |    |        |
|     |   2  |       |4.377e-13|    |        |    |        |    |        |
|     |   3  |       |3.131e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |3.131e-16|   3|  1.0000|   9|  1.0000|   6|  0.5036|

* final LPF:   -0.04969

### Increment 63
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |1.373e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.004e-06|    |        |    |        |    |        |
|     |   2  |       |7.436e-13|    |        |    |        |    |        |
|     |   3  |       |1.204e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |1.204e-16|   9|  1.0000|   3|  1.0000|   6|  0.5263|

* final LPF:    -0.0364

### Increment 64
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.206e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.046e-06|    |        |    |        |    |        |
|     |   2  |       |9.777e-13|    |        |    |        |    |        |
|     |   3  |       |3.441e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.441e-16|   9|  1.0000|   3|  1.0000|   6|  0.5416|

* final LPF:    -0.0225

### Increment 65
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.093e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.071e-06|    |        |    |        |    |        |
|     |   2  |       |1.112e-12|    |        |    |        |    |        |
|     |   3  |       |3.394e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.394e-16|   9|  1.0000|   3|  1.0000|   6|  0.5506|

* final LPF:  -0.008218

### Increment 66
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.045e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.081e-06|    |        |    |        |    |        |
|     |   2  |       |1.162e-12|    |        |    |        |    |        |
|     |   3  |       |5.333e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |5.333e-16|   9|  1.0000|   3|  1.0000|   6|  0.5538|

* final LPF:   0.006194

### Increment 67
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.068e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.073e-06|    |        |    |        |    |        |
|     |   2  |       |1.136e-12|    |        |    |        |    |        |
|     |   3  |       |6.948e-17|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |6.948e-17|   9|  1.0000|   3|  1.0000|   6|  0.5514|

* final LPF:     0.0205

### Increment 68
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.158e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.047e-06|    |        |    |        |    |        |
|     |   2  |       |1.030e-12|    |        |    |        |    |        |
|     |   3  |       |2.944e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.944e-16|   9|  1.0000|   3|  1.0000|   6|  0.5432|

* final LPF:    0.03448

### Increment 69
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.301e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.003e-06|    |        |    |        |    |        |
|     |   2  |       |8.322e-13|    |        |    |        |    |        |
|     |   3  |       |2.755e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.755e-16|   9|  1.0000|   3|  1.0000|   6|  0.5289|

* final LPF:    0.04786

### Increment 70
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.485e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.408e-07|    |        |    |        |    |        |
|     |   2  |       |5.448e-13|    |        |    |        |    |        |
|     |   3  |       |3.975e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.975e-16|   9|  1.0000|   3|  1.0000|   6|  0.5073|

* final LPF:    0.06042

### Increment 71
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.701e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.619e-07|    |        |    |        |    |        |
|     |   2  |       |3.118e-13|    |        |    |        |    |        |
|     |   3  |       |3.005e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.005e-16|   9|  1.0000|   3|  1.0000|   6|  0.4772|

* final LPF:    0.07189

### Increment 72
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |1.943e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.332e-07|    |        |    |        |    |        |
|     |   2  |       |3.755e-13|    |        |    |        |    |        |
|     |   3  |       |3.788e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.788e-16|   9|  1.0000|   3|  1.0000|   6|  0.4367|

* final LPF:    0.08199

### Increment 73
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |2.211e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.140e-06|    |        |    |        |    |        |
|     |   2  |       |6.246e-13|    |        |    |        |    |        |
|     |   3  |       |3.275e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |3.275e-16|   9|  1.0000|   3|  1.0000|   6|  0.3836|

* final LPF:    0.09045

### Increment 74
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |2.505e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.103e-06|    |        |    |        |    |        |
|     |   2  |       |2.418e-12|    |        |    |        |    |        |
|     |   3  |       |3.168e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |3.168e-16|   3|  1.0000|   9|  1.0000|   6|  0.3153|

* final LPF:    0.09694

### Increment 75
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |2.827e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.806e-06|    |        |    |        |    |        |
|     |   2  |       |8.132e-12|    |        |    |        |    |        |
|     |   3  |       |2.924e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |2.924e-16|   3|  1.0000|   9|  1.0000|   6|  0.2294|

* final LPF:     0.1012

### Increment 76
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |3.177e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.207e-06|    |        |    |        |    |        |
|     |   2  |       |2.637e-11|    |        |    |        |    |        |
|     |   3  |       |3.436e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |3.436e-16|   9|  1.0000|   3|  1.0000|   1| -0.1630|

* final LPF:     0.1027

### Increment 77
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |3.551e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.035e-06|    |        |    |        |    |        |
|     |   2  |       |6.749e-11|    |        |    |        |    |        |
|     |   3  |       |4.112e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |4.112e-16|   3|  1.0000|   9|  1.0000|   1| -0.1134|

* final LPF:     0.1013

### Increment 78
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |3.952e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.179e-05|    |        |    |        |    |        |
|     |   2  |       |1.258e-10|    |        |    |        |    |        |
|     |   3  |       |4.074e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |4.074e-16|   9|  1.0000|   3|  1.0000|   6| -0.1507|

* final LPF:    0.09653

### Increment 79
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |4.398e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.400e-05|    |        |    |        |    |        |
|     |   2  |       |1.732e-10|    |        |    |        |    |        |
|     |   3  |       |4.445e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |4.445e-16|   3|  1.0000|   9|  1.0000|   6| -0.3207|

* final LPF:    0.08788

### Increment 80
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   3   |4.943e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.570e-05|    |        |    |        |    |        |
|     |   2  |       |1.820e-10|    |        |    |        |    |        |
|     |   3  |       |1.750e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |1.750e-16|   9|  1.0000|   3|  1.0000|   6| -0.5186|

* final LPF:     0.0748

### Increment 81
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |5.724e-03|   3|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.882e-05|    |        |    |        |    |        |
|     |   2  |       |1.154e-10|    |        |    |        |    |        |
|     |   3  |       |5.119e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   3   |5.119e-16|   9|  1.0000|   3|  1.0000|   6| -0.7633|

* final LPF:    0.05639

### Increment 82
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   9   |7.109e-03|   9|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.340e-05|    |        |    |        |    |        |
|     |   2  |       |3.856e-10|    |        |    |        |    |        |
|     |   3  |       |3.264e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   9   |3.264e-16|   6| -1.1136|   3|  1.0000|   9|  1.0000|

* recycling increment

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.562e-03|    |        |    |        |    |        |
|     |   2  |       |1.133e-04|    |        |    |        |    |        |
|     |   3  |       |2.002e-08|    |        |    |        |    |        |
|     |   4  |       |7.657e-16|    |        |    |        |    |        |
|     |   5  |       |8.555e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  2  |   5  |  -6   |8.555e-16|   6| -1.0000|   3|  0.9149|   9|  0.9149|

* final LPF:    0.03342

### Increment 83
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |5.776e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.360e-05|    |        |    |        |    |        |
|     |   2  |       |2.090e-09|    |        |    |        |    |        |
|     |   3  |       |3.124e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.124e-16|   6| -1.0000|   3|  0.6487|   9|  0.6487|

* final LPF:     0.0118

### Increment 84
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |4.540e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.397e-05|    |        |    |        |    |        |
|     |   2  |       |4.870e-10|    |        |    |        |    |        |
|     |   3  |       |4.132e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.132e-16|   6| -1.0000|   7| -0.5198|   1|  0.5198|

* final LPF:  -0.008252

### Increment 85
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.911e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.593e-05|    |        |    |        |    |        |
|     |   2  |       |1.757e-10|    |        |    |        |    |        |
|     |   3  |       |2.498e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |2.498e-16|   6| -1.0000|   1|  0.5172|   7| -0.5172|

* final LPF:   -0.02655

### Increment 86
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.591e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.188e-05|    |        |    |        |    |        |
|     |   2  |       |8.281e-11|    |        |    |        |    |        |
|     |   3  |       |1.223e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |1.223e-16|   6| -1.0000|   7| -0.5104|   1|  0.5104|

* final LPF:   -0.04291

### Increment 87
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.446e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.556e-06|    |        |    |        |    |        |
|     |   2  |       |4.649e-11|    |        |    |        |    |        |
|     |   3  |       |5.033e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.033e-16|   6| -1.0000|   7| -0.5023|   1|  0.5023|

* final LPF:   -0.05718

### Increment 88
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.400e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |8.096e-06|    |        |    |        |    |        |
|     |   2  |       |2.951e-11|    |        |    |        |    |        |
|     |   3  |       |5.158e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.158e-16|   6| -1.0000|   1|  0.4944|   7| -0.4944|

* final LPF:   -0.06925

### Increment 89
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.407e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.120e-06|    |        |    |        |    |        |
|     |   2  |       |2.053e-11|    |        |    |        |    |        |
|     |   3  |       |2.510e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |2.510e-16|   6| -1.0000|   7| -0.4879|   1|  0.4879|

* final LPF:   -0.07902

### Increment 90
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.434e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.442e-06|    |        |    |        |    |        |
|     |   2  |       |1.538e-11|    |        |    |        |    |        |
|     |   3  |       |3.159e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.159e-16|   6| -1.0000|   1|  0.4831|   7| -0.4831|

* final LPF:   -0.08647

### Increment 91
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.464e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.960e-06|    |        |    |        |    |        |
|     |   2  |       |1.231e-11|    |        |    |        |    |        |
|     |   3  |       |4.011e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.011e-16|   6| -1.0000|   1|  0.4800|   7| -0.4800|

* final LPF:   -0.09159

### Increment 92
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.483e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.621e-06|    |        |    |        |    |        |
|     |   2  |       |1.049e-11|    |        |    |        |    |        |
|     |   3  |       |3.035e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.035e-16|   6| -1.0000|   7| -0.4783|   1|  0.4783|

* final LPF:   -0.09443

### Increment 93
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.486e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.397e-06|    |        |    |        |    |        |
|     |   2  |       |9.518e-12|    |        |    |        |    |        |
|     |   3  |       |5.206e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.206e-16|   6| -1.0000|   9| -0.5341|   3| -0.5341|

* final LPF:   -0.09504

### Increment 94
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.473e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.277e-06|    |        |    |        |    |        |
|     |   2  |       |9.212e-12|    |        |    |        |    |        |
|     |   3  |       |5.448e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |5.448e-16|   6| -1.0000|   3| -0.6260|   9| -0.6260|

* final LPF:   -0.09354

### Increment 95
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.444e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.266e-06|    |        |    |        |    |        |
|     |   2  |       |9.538e-12|    |        |    |        |    |        |
|     |   3  |       |4.180e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.180e-16|   6| -1.0000|   9| -0.7174|   3| -0.7174|

* final LPF:   -0.09005

### Increment 96
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.406e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.378e-06|    |        |    |        |    |        |
|     |   2  |       |1.060e-11|    |        |    |        |    |        |
|     |   3  |       |3.056e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |3.056e-16|   6| -1.0000|   3| -0.8089|   9| -0.8089|

* final LPF:   -0.08473

### Increment 97
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.362e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.648e-06|    |        |    |        |    |        |
|     |   2  |       |1.272e-11|    |        |    |        |    |        |
|     |   3  |       |6.016e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |6.016e-16|   6| -1.0000|   9| -0.9009|   3| -0.9009|

* final LPF:    -0.0777

### Increment 98
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.322e-03|   6|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |6.128e-06|    |        |    |        |    |        |
|     |   2  |       |1.658e-11|    |        |    |        |    |        |
|     |   3  |       |4.340e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -6   |4.340e-16|   6| -1.0000|   3| -0.9939|   9| -0.9939|

* final LPF:   -0.06915

### Increment 99
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -6   |3.297e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.456e-06|    |        |    |        |    |        |
|     |   2  |       |4.350e-11|    |        |    |        |    |        |
|     |   3  |       |2.360e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.360e-16|   9| -1.0000|   3| -1.0000|   6| -0.9217|

* final LPF:   -0.06003

### Increment 100
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.591e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.171e-06|    |        |    |        |    |        |
|     |   2  |       |1.947e-11|    |        |    |        |    |        |
|     |   3  |       |4.521e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.521e-16|   3| -1.0000|   9| -1.0000|   6| -0.8537|

* final LPF:   -0.05063

### Increment 101
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.272e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.889e-06|    |        |    |        |    |        |
|     |   2  |       |1.049e-11|    |        |    |        |    |        |
|     |   3  |       |3.324e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.324e-16|   9| -1.0000|   3| -1.0000|   6| -0.7970|

* final LPF:   -0.04112

### Increment 102
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.047e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.134e-06|    |        |    |        |    |        |
|     |   2  |       |6.617e-12|    |        |    |        |    |        |
|     |   3  |       |4.667e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |4.667e-16|   3| -1.0000|   9| -1.0000|   6| -0.7481|

* final LPF:    -0.0316

### Increment 103
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.891e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.683e-06|    |        |    |        |    |        |
|     |   2  |       |4.779e-12|    |        |    |        |    |        |
|     |   3  |       |3.829e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |3.829e-16|   3| -1.0000|   9| -1.0000|   6| -0.7047|

* final LPF:   -0.02215

### Increment 104
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.789e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.427e-06|    |        |    |        |    |        |
|     |   2  |       |3.893e-12|    |        |    |        |    |        |
|     |   3  |       |5.455e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |5.455e-16|   9| -1.0000|   3| -1.0000|   6| -0.6651|

* final LPF:   -0.01287

### Increment 105
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.729e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.307e-06|    |        |    |        |    |        |
|     |   2  |       |3.536e-12|    |        |    |        |    |        |
|     |   3  |       |7.345e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |7.345e-16|   9| -1.0000|   3| -1.0000|   6| -0.6281|

* final LPF:  -0.003818

### Increment 106
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.706e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.298e-06|    |        |    |        |    |        |
|     |   2  |       |3.554e-12|    |        |    |        |    |        |
|     |   3  |       |4.873e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |4.873e-16|   9| -1.0000|   3| -1.0000|   6| -0.5923|

* final LPF:   0.004925

### Increment 107
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.716e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.393e-06|    |        |    |        |    |        |
|     |   2  |       |3.931e-12|    |        |    |        |    |        |
|     |   3  |       |5.369e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |5.369e-16|   9| -1.0000|   3| -1.0000|   6| -0.5568|

* final LPF:    0.01327

### Increment 108
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |1.755e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.600e-06|    |        |    |        |    |        |
|     |   2  |       |4.770e-12|    |        |    |        |    |        |
|     |   3  |       |4.414e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.414e-16|   3| -1.0000|   9| -1.0000|   6| -0.5205|

* final LPF:    0.02112

### Increment 109
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.823e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.947e-06|    |        |    |        |    |        |
|     |   2  |       |6.340e-12|    |        |    |        |    |        |
|     |   3  |       |6.011e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |6.011e-16|   3| -1.0000|   9| -1.0000|   6| -0.4821|

* final LPF:    0.02833

### Increment 110
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |1.924e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.480e-06|    |        |    |        |    |        |
|     |   2  |       |9.222e-12|    |        |    |        |    |        |
|     |   3  |       |3.180e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |3.180e-16|   9| -1.0000|   3| -1.0000|   6| -0.4405|

* final LPF:    0.03477

### Increment 111
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.059e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.282e-06|    |        |    |        |    |        |
|     |   2  |       |1.467e-11|    |        |    |        |    |        |
|     |   3  |       |4.507e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |4.507e-16|   3| -1.0000|   9| -1.0000|   6| -0.3939|

* final LPF:    0.04023

### Increment 112
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.237e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.481e-06|    |        |    |        |    |        |
|     |   2  |       |2.550e-11|    |        |    |        |    |        |
|     |   3  |       |9.660e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |9.660e-16|   3| -1.0000|   9| -1.0000|   1| -0.3425|

* final LPF:    0.04445

### Increment 113
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.466e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.287e-06|    |        |    |        |    |        |
|     |   2  |       |4.822e-11|    |        |    |        |    |        |
|     |   3  |       |9.844e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |9.844e-16|   3| -1.0000|   9| -1.0000|   1| -0.4295|

* final LPF:    0.04713

### Increment 114
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.756e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.002e-05|    |        |    |        |    |        |
|     |   2  |       |9.842e-11|    |        |    |        |    |        |
|     |   3  |       |2.902e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.902e-16|   9| -1.0000|   3| -1.0000|   7|  0.5276|

* final LPF:    0.04785

### Increment 115
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.115e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.415e-05|    |        |    |        |    |        |
|     |   2  |       |2.131e-10|    |        |    |        |    |        |
|     |   3  |       |6.857e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |6.857e-16|   9| -1.0000|   3| -1.0000|   1| -0.6391|

* final LPF:     0.0461

### Increment 116
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.537e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.019e-05|    |        |    |        |    |        |
|     |   2  |       |4.725e-10|    |        |    |        |    |        |
|     |   3  |       |2.557e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |2.557e-16|   9| -1.0000|   3| -1.0000|   7|  0.7659|

* final LPF:    0.04128

### Increment 117
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.987e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.825e-05|    |        |    |        |    |        |
|     |   2  |       |9.991e-10|    |        |    |        |    |        |
|     |   3  |       |2.820e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.820e-16|   9| -1.0000|   3| -1.0000|   1| -0.9078|

* final LPF:    0.03271

### Increment 118
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |4.361e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.642e-05|    |        |    |        |    |        |
|     |   2  |       |1.754e-09|    |        |    |        |    |        |
|     |   3  |       |4.800e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.800e-16|   7|  1.0585|   1| -1.0585|   9| -1.0000|

* recycling increment

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.508e-03|    |        |    |        |    |        |
|     |   2  |       |1.336e-05|    |        |    |        |    |        |
|     |   3  |       |5.081e-11|    |        |    |        |    |        |
|     |   4  |       |9.225e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  2  |   4  |   7   |9.225e-16|   7|  1.0000|   1| -1.0000|   9| -0.9482|

* final LPF:    0.02062

### Increment 119
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   7   |3.567e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.540e-06|    |        |    |        |    |        |
|     |   2  |       |1.709e-11|    |        |    |        |    |        |
|     |   3  |       |3.841e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |3.841e-16|   7|  1.0000|   1| -1.0000|   3| -0.8462|

* final LPF:   0.006556

### Increment 120
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   7   |2.824e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.180e-06|    |        |    |        |    |        |
|     |   2  |       |1.372e-11|    |        |    |        |    |        |
|     |   3  |       |2.999e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |2.999e-16|   7|  1.0000|   1| -1.0000|   9| -0.7896|

* final LPF:  -0.008773

### Increment 121
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   7   |2.290e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.520e-06|    |        |    |        |    |        |
|     |   2  |       |1.614e-11|    |        |    |        |    |        |
|     |   3  |       |6.960e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |6.960e-16|   1| -1.0000|   7|  1.0000|   9| -0.7740|

* final LPF:   -0.02463

### Increment 122
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -1   |2.153e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.941e-06|    |        |    |        |    |        |
|     |   2  |       |1.577e-11|    |        |    |        |    |        |
|     |   3  |       |2.323e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |2.323e-16|   7|  1.0000|   1| -1.0000|   9| -0.8020|

* final LPF:   -0.04016

### Increment 123
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   7   |2.700e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |5.584e-06|    |        |    |        |    |        |
|     |   2  |       |6.267e-12|    |        |    |        |    |        |
|     |   3  |       |3.311e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |3.311e-16|   7|  1.0000|   1| -1.0000|   9| -0.8852|

* final LPF:    -0.0542

### Increment 124
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |   7   |4.066e-03|   7|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.167e-05|    |        |    |        |    |        |
|     |   2  |       |1.407e-11|    |        |    |        |    |        |
|     |   3  |       |1.576e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   7   |1.576e-16|   9| -1.0479|   3| -1.0479|   7|  1.0000|

* recycling increment

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.521e-03|    |        |    |        |    |        |
|     |   2  |       |1.845e-05|    |        |    |        |    |        |
|     |   3  |       |2.923e-11|    |        |    |        |    |        |
|     |   4  |       |5.666e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  2  |   4  |  -9   |5.666e-16|   9| -1.0000|   3| -1.0000|   7|  0.9587|

* final LPF:   -0.06458

### Increment 125
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |4.717e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.073e-05|    |        |    |        |    |        |
|     |   2  |       |1.674e-11|    |        |    |        |    |        |
|     |   3  |       |8.567e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |8.567e-16|   3| -1.0000|   9| -1.0000|   1| -0.7816|

* final LPF:   -0.06885

### Increment 126
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |4.504e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.724e-05|    |        |    |        |    |        |
|     |   2  |       |1.823e-11|    |        |    |        |    |        |
|     |   3  |       |4.958e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |4.958e-16|   9| -1.0000|   3| -1.0000|   7|  0.6346|

* final LPF:   -0.06761

### Increment 127
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |4.114e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.197e-05|    |        |    |        |    |        |
|     |   2  |       |1.393e-11|    |        |    |        |    |        |
|     |   3  |       |4.808e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.808e-16|   3| -1.0000|   9| -1.0000|   1| -0.5209|

* final LPF:   -0.06164

### Increment 128
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |3.690e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.484e-06|    |        |    |        |    |        |
|     |   2  |       |5.395e-12|    |        |    |        |    |        |
|     |   3  |       |4.985e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.985e-16|   9| -1.0000|   3| -1.0000|   7|  0.4343|

* final LPF:   -0.05164

### Increment 129
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |3.300e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |4.431e-06|    |        |    |        |    |        |
|     |   2  |       |1.199e-12|    |        |    |        |    |        |
|     |   3  |       |2.493e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.493e-16|   9| -1.0000|   3| -1.0000|   1| -0.3675|

* final LPF:   -0.03819

### Increment 130
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -9   |2.961e-03|   3|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.581e-06|    |        |    |        |    |        |
|     |   2  |       |2.444e-13|    |        |    |        |    |        |
|     |   3  |       |2.556e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -3   |2.556e-16|   3| -1.0000|   9| -1.0000|  10|  0.3295|

* final LPF:   -0.02171

### Increment 131
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.673e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |1.529e-06|    |        |    |        |    |        |
|     |   2  |       |7.492e-14|    |        |    |        |    |        |
|     |   3  |       |4.503e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.503e-16|   3| -1.0000|   9| -1.0000|  10|  0.3827|

* final LPF:  -0.002576

### Increment 132
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|  1  |   0  |  -3   |2.429e-03|   9|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |9.442e-07|    |        |    |        |    |        |
|     |   2  |       |4.621e-14|    |        |    |        |    |        |
|     |   3  |       |4.785e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |  -9   |4.785e-16|   9| -1.0000|   3| -1.0000|  10|  0.4302|

* final LPF:    0.01893
\pagebreak
 

### Create result object from analysis results for step   1

    write result   1/132 (LPF:    0.01945)
    write result   2/132 (LPF:    0.03628)
    write result   3/132 (LPF:    0.05013)
    write result   4/132 (LPF:    0.06059)
    write result   5/132 (LPF:     0.0671)
    write result   6/132 (LPF:    0.06898)
    write result   7/132 (LPF:    0.06544)
    write result   8/132 (LPF:    0.05584)
    write result   9/132 (LPF:    0.04211)
    write result  10/132 (LPF:     0.0267)
    write result  11/132 (LPF:    0.01083)
    write result  12/132 (LPF:  -0.004609)
    write result  13/132 (LPF:   -0.01888)
    write result  14/132 (LPF:   -0.03127)
    write result  15/132 (LPF:   -0.04038)
    write result  16/132 (LPF:   -0.04566)
    write result  17/132 (LPF:   -0.04777)
    write result  18/132 (LPF:   -0.04734)
    write result  19/132 (LPF:    -0.0449)
    write result  20/132 (LPF:   -0.04086)
    write result  21/132 (LPF:   -0.03555)
    write result  22/132 (LPF:   -0.02923)
    write result  23/132 (LPF:    -0.0221)
    write result  24/132 (LPF:   -0.01433)
    write result  25/132 (LPF:  -0.006048)
    write result  26/132 (LPF:   0.002648)
    write result  27/132 (LPF:    0.01166)
    write result  28/132 (LPF:    0.02092)
    write result  29/132 (LPF:    0.03035)
    write result  30/132 (LPF:    0.03987)
    write result  31/132 (LPF:    0.04939)
    write result  32/132 (LPF:     0.0588)
    write result  33/132 (LPF:    0.06797)
    write result  34/132 (LPF:    0.07666)
    write result  35/132 (LPF:    0.08389)
    write result  36/132 (LPF:    0.08946)
    write result  37/132 (LPF:    0.09319)
    write result  38/132 (LPF:    0.09496)
    write result  39/132 (LPF:    0.09463)
    write result  40/132 (LPF:     0.0921)
    write result  41/132 (LPF:    0.08728)
    write result  42/132 (LPF:    0.08014)
    write result  43/132 (LPF:    0.07067)
    write result  44/132 (LPF:     0.0589)
    write result  45/132 (LPF:    0.04491)
    write result  46/132 (LPF:    0.02882)
    write result  47/132 (LPF:    0.01077)
    write result  48/132 (LPF:   -0.00907)
    write result  49/132 (LPF:   -0.03049)
    write result  50/132 (LPF:   -0.05329)
    write result  51/132 (LPF:   -0.07256)
    write result  52/132 (LPF:   -0.08633)
    write result  53/132 (LPF:   -0.09556)
    write result  54/132 (LPF:    -0.1009)
    write result  55/132 (LPF:    -0.1027)
    write result  56/132 (LPF:    -0.1016)
    write result  57/132 (LPF:   -0.09768)
    write result  58/132 (LPF:   -0.09149)
    write result  59/132 (LPF:   -0.08329)
    write result  60/132 (LPF:    -0.0734)
    write result  61/132 (LPF:   -0.06211)
    write result  62/132 (LPF:   -0.04969)
    write result  63/132 (LPF:    -0.0364)
    write result  64/132 (LPF:    -0.0225)
    write result  65/132 (LPF:  -0.008218)
    write result  66/132 (LPF:   0.006194)
    write result  67/132 (LPF:     0.0205)
    write result  68/132 (LPF:    0.03448)
    write result  69/132 (LPF:    0.04786)
    write result  70/132 (LPF:    0.06042)
    write result  71/132 (LPF:    0.07189)
    write result  72/132 (LPF:    0.08199)
    write result  73/132 (LPF:    0.09045)
    write result  74/132 (LPF:    0.09694)
    write result  75/132 (LPF:     0.1012)
    write result  76/132 (LPF:     0.1027)
    write result  77/132 (LPF:     0.1013)
    write result  78/132 (LPF:    0.09653)
    write result  79/132 (LPF:    0.08788)
    write result  80/132 (LPF:     0.0748)
    write result  81/132 (LPF:    0.05639)
    write result  82/132 (LPF:    0.03342)
    write result  83/132 (LPF:     0.0118)
    write result  84/132 (LPF:  -0.008252)
    write result  85/132 (LPF:   -0.02655)
    write result  86/132 (LPF:   -0.04291)
    write result  87/132 (LPF:   -0.05718)
    write result  88/132 (LPF:   -0.06925)
    write result  89/132 (LPF:   -0.07902)
    write result  90/132 (LPF:   -0.08647)
    write result  91/132 (LPF:   -0.09159)
    write result  92/132 (LPF:   -0.09443)
    write result  93/132 (LPF:   -0.09504)
    write result  94/132 (LPF:   -0.09354)
    write result  95/132 (LPF:   -0.09005)
    write result  96/132 (LPF:   -0.08473)
    write result  97/132 (LPF:    -0.0777)
    write result  98/132 (LPF:   -0.06915)
    write result  99/132 (LPF:   -0.06003)
    write result 100/132 (LPF:   -0.05063)
    write result 101/132 (LPF:   -0.04112)
    write result 102/132 (LPF:    -0.0316)
    write result 103/132 (LPF:   -0.02215)
    write result 104/132 (LPF:   -0.01287)
    write result 105/132 (LPF:  -0.003818)
    write result 106/132 (LPF:   0.004925)
    write result 107/132 (LPF:    0.01327)
    write result 108/132 (LPF:    0.02112)
    write result 109/132 (LPF:    0.02833)
    write result 110/132 (LPF:    0.03477)
    write result 111/132 (LPF:    0.04023)
    write result 112/132 (LPF:    0.04445)
    write result 113/132 (LPF:    0.04713)
    write result 114/132 (LPF:    0.04785)
    write result 115/132 (LPF:     0.0461)
    write result 116/132 (LPF:    0.04128)
    write result 117/132 (LPF:    0.03271)
    write result 118/132 (LPF:    0.02062)
    write result 119/132 (LPF:   0.006556)
    write result 120/132 (LPF:  -0.008773)
    write result 121/132 (LPF:   -0.02463)
    write result 122/132 (LPF:   -0.04016)
    write result 123/132 (LPF:    -0.0542)
    write result 124/132 (LPF:   -0.06458)
    write result 125/132 (LPF:   -0.06885)
    write result 126/132 (LPF:   -0.06761)
    write result 127/132 (LPF:   -0.06164)
    write result 128/132 (LPF:   -0.05164)
    write result 129/132 (LPF:   -0.03819)
    write result 130/132 (LPF:   -0.02171)
    write result 131/132 (LPF:  -0.002576)
    write result 132/132 (LPF:    0.01893)

End of Step 1
\pagebreak
 

## Job duration
Time measurement for execution times of "Model.build()" and "Model.run()".

    total  cpu time "build":      0.001 seconds
    total wall time "build":      0.000 seconds

    total  cpu time "run":        4.211 seconds
    total wall time "run":        4.141 seconds

