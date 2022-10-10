#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:21:23 2022.

@author: fabian
"""

import numpy as np
import xarray as xr

from linopy import Model


def test_basic_matrices():
    m = Model()

    lower = xr.DataArray(np.zeros((10, 10)), coords=[range(10), range(10)])
    upper = xr.DataArray(np.ones((10, 10)), coords=[range(10), range(10)])
    x = m.add_variables(lower, upper, name="x")
    y = m.add_variables(name="y")

    m.add_constraints(1 * x + 10 * y, "=", 0)

    obj = (10 * x + 5 * y).sum()
    m.add_objective(obj)

    assert m.matrices.A.shape == (*m.matrices.clabels.shape, *m.matrices.vlabels.shape)
    assert m.matrices.clabels.shape == m.matrices.sense.shape
    assert m.matrices.vlabels.shape == m.matrices.ub.shape
    assert m.matrices.vlabels.shape == m.matrices.lb.shape
