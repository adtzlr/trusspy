# TrussPy

an object-oriented 3D **Truss** solver for **Py**thon licensed under the terms of GNU GPL v3

![TrussPy Logo](logo.png)

### Introduction
Download the package from the project's GitHub repository and extract the `trusspy` folder into your working directory. Currently there is no `pip install` setup available.

### Setting up a Model
Each object inside a TrussPy model is a Class with attributes and methods. There are several basic objects available: *Node*, *Element*, *Boundary* (mechanical and thermal boundary condition) and *ExternalLoad* which will be explained below.

##### Node
A **Node** class needs two attributes on initiation: It's `label` (node number) and a set of coordinates `[x,y,z]`, which may either be passed as a list or as an array.

```python
N = Node(label, [x,y,z])

#Example
N1 = Node(1, [0,0,0])
N2 = Node(2, [1,0,0])
```
##### Element
An **Element** class needs two attributes on initiation: It's `label` (node number) and a set of connected nodes `[node_A, node_B]`, which may either be passed as a list or as an array containing the node labels (**NOT** the node itself).

```python
E = E(label, [node_label_A, node_label_B])

# Example
E1 = Element(1, [1,2])
```

##### Boundary
There are two different boundary conditions possible: node-based mechanical or element-based thermal conditions. A **BoundaryU** class needs two attributes on initiation: It's `label` (corresponding node number) and a set of active/inactive (locked/free) flags in directions `[u,v,w]`, which may either be passed as a list or as an array.

```python
BU = BoundaryU(label, [flag_u,flag_v,flag_w])

#Example
BU1 = BoundaryU(1, [1,0,0]) # u=free and v,w=locked
BU2 = BoundaryU(2, [0,0,1]) # u,v=locked and w=free
```

A **BoundaryT** class needs two attributes on initiation: It's `label` (corresponding element number) and a normalized initial thermal value `(aT T) / (aT0 T0)`. **...currently not implemented**

```python
BT = BoundaryT(label, aTT_aT0T0)

#Example
BT1 = BoundaryT(1, 10)
```

##### ExternalLoad

##### A word on Managers

### Use Excel Input Files

### Run an Analysis
#### Settings
#### Solver
#### Run

### Postprocess Results
#### 

### Additional Settings