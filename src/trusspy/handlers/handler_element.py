# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import numpy as np

from ..core.element import Element


class ElementHandler:
    "Handler for Elements"

    def __init__(self):
        self.labels = None
        self.conns = None
        self.elem_type = None
        self.mat_type = None
        self.material_properties = None
        self.geometric_properties = None

    def __enter__(self):
        return self

    def __exit__(self, H_type, H_value, H_traceback):
        pass

    def assign_material(self, labels, mprop, mtype=None):
        if labels == "all":
            labels = self.labels

        # reshape (extend) material properties
        if self.material_properties.shape[1] < len(mprop):
            extend = np.zeros(
                (
                    self.material_properties.shape[0],
                    len(mprop) - self.material_properties.shape[1],
                )
            )
            self.material_properties = np.hstack((self.material_properties, extend))
        elif self.material_properties.shape[1] > len(mprop):
            extend = np.zeros(self.material_properties.shape[1] - len(mprop))
            mprop = np.append(mprop, extend)

        for label in labels:
            self.material_properties[np.where(self.labels == label)] = [mprop]
            if mtype is not None:
                self.mat_type[np.where(self.labels == label)] = [mtype]

    def assign_geometry(self, labels, gprop):
        if labels == "all":
            labels = self.labels
        for label in labels:
            self.geometric_properties[np.where(self.labels == label)] = [gprop]

    def assign_geometries(self, labels, gprops):
        if labels == "all":
            labels = self.labels
        for label, gprop in zip(labels, gprops):
            self.geometric_properties[np.where(self.labels == label)] = [gprop]

    def assign_etype(self, labels, elem_type):
        if labels == "all":
            labels = self.labels
        for label in labels:
            self.elem_type[np.where(self.labels == label)] = elem_type

    def assign_mtype(self, labels, mat_type):
        if labels == "all":
            labels = self.labels
        for label in labels:
            self.mat_type[np.where(self.labels == label)] = mat_type

    def add_element(self, E, *args, **kwargs):
        "add single element to ElementManager"

        # raw node
        if "Element" not in str(type(E)):
            E = Element(E, *args, **kwargs)

        if self.labels is None:
            self.labels = np.array([E.label])
            self.elem_type = np.array([E.elem_type])
            self.mat_type = np.array([E.mat_type])
            self.conns = np.array([E.conn])
            self.material_properties = np.array([E.material_properties])
            self.geometric_properties = np.array([E.geometric_properties])
        else:
            self.labels = np.append(self.labels, E.label)
            self.conns = np.vstack((self.conns, E.conn))
            self.elem_type = np.append(self.elem_type, E.elem_type)
            self.mat_type = np.append(self.mat_type, E.mat_type)
            self.material_properties = np.vstack(
                (self.material_properties, E.material_properties)
            )
            self.geometric_properties = np.vstack(
                (self.geometric_properties, E.geometric_properties)
            )

    def del_element(self, label):
        idx = np.where(self.labels == label)[0]
        self.labels = np.delete(self.labels, idx, axis=0)
        self.conns = np.delete(self.conns, idx, axis=0)
        self.material_properties = np.delete(self.material_properties, idx, axis=0)
        self.geometric_properties = np.delete(self.geometric_properties, idx, axis=0)

    def add_elements(self, EE):
        "add several elements from element list to ElementManager"
        for E in EE:
            self.add_element(E)

    def get_nodes(self, label):
        "choose element label and return connected end node"
        return self.conns[np.where(self.labels == label)][0]

    def NE(self, label):
        "choose element label and return connected end node"
        return self.conns[np.where(self.labels == label)][0, -1]

    def NA(self, label):
        "choose element label and return connected begin node"
        return self.conns[np.where(self.labels == label)][0, -2]

    def get_material_type(self, label):
        "choose element label and return material type"
        return self.mat_type[np.where(self.labels == label)][0]

    def get_element_type(self, label):
        "choose element label and return element type"
        return self.elem_type[np.where(self.labels == label)][0]

    def get_material_properties(self, label):
        "choose element label and return material properties"
        return self.material_properties[np.where(self.labels == label)][0]

    def get_geometric_properties(self, label):
        "choose element label and return element area"
        return self.geometric_properties[np.where(self.labels == label)][0]
