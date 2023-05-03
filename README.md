<p align="center">
  <a href="https://trusspy.readthedocs.io"><img src="https://raw.githubusercontent.com/adtzlr/trusspy/main/docs/_static/logo.png" height="80px"/></a>
  <p align="center">Truss Solver for Python.</p>
</p>

[![PyPI version shields.io](https://img.shields.io/pypi/v/trusspy.svg)](https://pypi.python.org/pypi/trusspy/) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adtzlr/trusspy/main?labpath=docs%2Fexamples%2Fe101_nb_interactive.ipynb) <a target="_blank" href="https://colab.research.google.com/github/adtzlr/trusspy/blob/main/docs/examples/e101_nb_interactive.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> [![Documentation Status](https://readthedocs.org/projects/trusspy/badge/?version=latest)](https://trusspy.readthedocs.io/en/latest/?badge=latest) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Made with love in Graz (Austria)](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20in-Graz%20(Austria)-0c674a) [![codecov](https://codecov.io/gh/adtzlr/trusspy/branch/main/graph/badge.svg?token=2Z0ZKOUKPW)](https://codecov.io/gh/adtzlr/trusspy) [![DOI](https://zenodo.org/badge/145743574.svg)](https://zenodo.org/badge/latestdoi/145743574) ![Codestyle black](https://img.shields.io/badge/code%20style-black-black)

**TrussPy** is a 3D **Truss**-Solver written in **Py**-thon which is capable of material and geometric nonlinearities. It uses an object-oriented approach to structure the code in meaningful classes, attributes and methods. TrussPy contains both multistep functionality (multiple loadcase analysis with sequenced external forces) and an adaptive method to control incremental stepwidths. Input files may be written in Excel or directly in Python. A simple post-processing inside TrussPy is directly available via Matplotlib. Model Plots whether in undeformed or deformed configuration with optional contour plots on element forces are easy to show. They may also be generated for a series of increments and saved as a GIF Movie. Last but not least History (a.k.a. x-y) Plots for a series of increments or Path Plots along a given node path may be generated for nodal properties (displacements, forces) or global quantities like the Load-Proportionality-Factor (LPF).
   
Official Documentation: http://trusspy.readthedocs.io/

# Installation
Use `pip` to install TrussPy

```
pip install trusspy
```

# Example
```python
import trusspy as tp

M = tp.Model()

# create nodes
with M.Nodes as MN:
    MN.add_node(1, (0, 0, 0))
    MN.add_node(2, (1, 0, 0))

# create element
with M.Elements as ME:
    ME.add_element(1, [1, 2])
    ME.assign_material("all", [1])
    ME.assign_geometry("all", [1])

# create displacement (U) boundary conditions
with M.Boundaries as MB:
    MB.add_bound_U(1, (0, 0, 0))
    MB.add_bound_U(2, (1, 0, 0))

# create external forces
with M.ExtForces as MF:
    MF.add_force(2, (1, 0, 0))

# build model, run, show results
M.build()
M.run()

# plot results
M.plot_model()
M.plot_show()
```
	
# Online Notebook
Try TrussPy without installation in an [Interactive Online Notebook](https://mybinder.org/v2/gh/adtzlr/trusspy/main?labpath=docs%2Fexamples%2Fe101_nb_interactive.ipynb).

# Changelog
All notable changes to this project will be documented in [this file](CHANGELOG.md). The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# License
TrussPy - Truss Solver for Python (C) 2023 Andreas Dutzler, Graz (Austria).

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
