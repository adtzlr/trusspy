# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:46:06 2018

@author: adutz
"""

import numpy as np


class Element:
    """Element class.

    Parameter
    ---------
    label : int
        Element ID number
    conn : array_like
        List of Element connectivity : `[Node 1, Node 2]`

    elem_type : int, optional
        Element Type. (default is 1 for truss)
    mat_type : int, optional
        Material Type. (default is 1 for linear-elastic)
    material_properties : array_like, optional
        List with material parameters,
        e.g. [Young's modulus, Thermal expansion coefficient] (default is [])
    geometric_properties : array_like, optional
        List with geometric parameters,
        e.g. [Section area] (default is [])

    Attributes
    ----------
    label : int
        Element ID number
    conn : ndarray
        Array containing Element connectivity : `[Node 1, Node 2]`
    elem_type : int, optional
        Element Type. (default is 1 for truss)
    mat_type : int, optional
        Material Type. (default is 1 for linear-elastic)
    material_properties : array_like, optional
        List with material parameters,
        e.g. [Young's modulus, Thermal expansion coefficient] (default is [])
    geometric_proerties : array_like, optional
        List with geometric parameters,
        e.g. [Section area] (default is [])

    Todo
    ----
    + DONE rewrite material parameter storage
    + DONE material properties: type, mechanical and thermal parameter
    + DONE geometric porperties: section area
    """

    def __init__(
        self,
        label,
        conn,
        elem_type=1,
        mat_type=1,
        material_properties=[np.nan],
        geometric_properties=[np.nan],
        mprop=None,
        gprop=None,
    ):

        self.label = label
        self.conn = np.array(conn)
        self.elem_type = elem_type
        self.mat_type = mat_type

        if material_properties != [np.nan] and mprop is not None:
            raise TypeError(
                'Wrong Material Properties. Use either "material_properties" or "mprop", not both.'
            )

        if geometric_properties != [np.nan] and gprop is not None:
            raise TypeError(
                'Wrong Geometric Properties. Use either "geometric_properties" or "gprop", not both.'
            )

        if mprop is not None:
            self.material_properties = mprop
        else:
            self.material_properties = material_properties

        if gprop is not None:
            self.geometric_properties = gprop
        else:
            self.geometric_properties = geometric_properties

    # def get_NE(self):
    #    """get end node of element"""
    #    return self.conn[1]

    # def get_NA(self):
    #    """get begin node of element"""
    #    return self.conn[0]
