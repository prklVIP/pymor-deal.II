# -*- coding: utf-8 -*-
# This file is part of the pyMOR project (http://www.pymor.org).
# Copyright Holders: Rene Milk, Stephan Rave, Felix Schindler
# License: BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function

from pymor.core.interfaces import ImmutableInterface
from pymor.vectorarrays.interfaces import VectorArrayInterface


class DealIIVisualizer(ImmutableInterface):

    def __init__(self, impl):
        self.impl = impl

    def visualize(self, U, discretization, title=None, legend=None, separate_colorbars=True, filename=None):
        if isinstance(U, VectorArrayInterface):
            U = [U]
        if any(len(u) != 1 for u in U):
            raise NotImplementedError
        if not separate_colorbars:
            raise NotImplementedError
        assert title is None or filename is None
        assert legend is None or len(legend) == len(U)

        base_name = title or filename or 'out'
        if len(U) == 1 and not legend:
            filenames = [base_name]
        else:
            legend = legend or map(str, range(len(U)))
            filenames = ['_'.join((base_name, l)) for l in legend]

        for u, n in zip(U, filenames):
            self.impl.visualize(u._list[0].impl, n + '.vtk')
