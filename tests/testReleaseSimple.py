"""
Authors: Stefan Strang
University of Freiburg - 2018

This is module for explicit testing of large functiosn of the fosaccs2018.

"""

# import unittest
import gc
# from unittest.case import TestCase
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf


def testReleaseSimple(self):
    gc.collect()
    ob = toPnf('R p q')
    linFaca = lf(ob)
    sol = set()
    for x in linFaca:
        for y in x:
            if type(y) == frozenset:
                for i in y:
                    sol.add(i.getName())
            elif type(y) == tuple:
                for t in y:
                    sol.add(t.getName())
            else:

                sol.add(y.getName())
    self.assertEqual(sol, {'tt', 'q', 'p', 'R'})
    first = ob.getFirst()
    sec = ob.getSec()
    del first
    del sec
    ob.setFirst(None)
    ob.setSec(None)
    del ob
