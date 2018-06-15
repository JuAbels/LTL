"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

import unittest
import gc
from unittest.case import TestCase
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives

class testDefintion10(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testDummy(self):
        self.assertEqual( 1, 1)
    def testCaseTrue(self):
        objects = toPnf('tt')
        derTT = derivatives(objects, 'tt')
        solution = []
        for x in derTT:
            solution.append(x.getName())
        self.assertEqual(solution, ['tt'])


def test10():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(testDefintion10))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
