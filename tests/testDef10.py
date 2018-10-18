"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

import unittest
# import gc
# from unittest.case import TestCase
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives


class testDefintion10(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def atestDummy(self):
        self.assertEqual(1, 1)

    def testCaseTrue(self):
        objects = toPnf('tt')
        derTT = derivatives(objects, 'tt')
        #print("===>", derTT)
        solution = []
        for x in derTT:
            solution.append(x.getName())
        self.assertEqual(solution, ['tt'])

    def testCaseFormula(self):
        objects = toPnf('p1')
        derF = derivatives(objects, '{p1}')
        solution = []
        #print("!!!!!!!!!!!!!", derF)
        for x in derF:
            solution.append(x.getName())
        self.assertEqual(solution, ['tt'])

    def testCaseFormulaInvalid(self):
        objects = toPnf('p1')
        derFNot = derivatives(objects, 'n')
        self.assertEqual(derFNot, set())

    def testCaseAndEmpty(self):
        objects = toPnf('& p1 p2')
        derCaseAnd = derivatives(objects, 'x')
        # solution = []
        self.assertEqual(derCaseAnd, set())

    def testCaseAnd(self):
        objects = toPnf('& p1 p2')
        derCaseAnd = derivatives(objects, '{p1, p2}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            solution.append(x.getName())
            solution.append(x.getFirst().getName())
            solution.append(x.getSec().getName())
        self.assertEqual(solution, ['&', 'tt', 'tt'])

    def testCaseOne(self):
        objects = toPnf('& p1 p2')
        derCaseAnd = derivatives(objects, '{p1, p2}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            solution.append(x.getName())
            solution.append(x.getFirst().getName())
            solution.append(x.getSec().getName())
        self.assertEqual(solution, ['&', 'tt', 'tt'])


def test10():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testDefintion10))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
