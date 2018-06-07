"""
Authors: Stefan Strang
University of Freiburg - 2018

This is module for explicit testing of large functiosn of the fosaccs2018.

"""

import unittest
import gc
from unittest.case import TestCase
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
class testGFp(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testDummy(self):
        self.assertEqual( 1, 1)


    def testLfGFp(self):
        gc.collect()
        obs = toPnf('G F u')
        lins = lf(obs)
        solve = set()
        print(lins)
        for x in lins:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        print(z.getName())
                else:
                    print(y.getName())
    def __del__(self):
        pass


def testgfp():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(testGFp))
    
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
