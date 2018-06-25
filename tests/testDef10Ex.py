"""
Authors: Stefan Strang
University of Freiburg - 2018

Operators:
next: 		Xf - ()
eventually 	Ff - <> => tt U f
always 		Gf - [] => ff R f
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g
derivat = set()

"""

import unittest
# import gc
# from unittest.case import TestCase
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives


class testDefintion10Ex1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testEx1(self):
        objects = toPnf('G F p1')
        # print(objects.getName())
        derCaseAnd = derivatives(objects, '{p1}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            # print(x.getName())
            solution.append(x.getName())
        self.assertEqual(len(solution), 2)
        # self.assertEqual(solution[1], 'R')

    def testEx2(self):
        objects = toPnf('F p1')
        # print(objects.getName())
        derCaseAnd = derivatives(objects, '{p1}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            # print(x.getName())
            solution.append(x.getName())
        self.assertEqual(len(solution), 2)
        # self.assertEqual(solution[1], 'U')

    def testNotEx1(self):
        objects = toPnf('G F p1')
        # print(objects.getName())
        derCaseAnd = derivatives(objects, '{x}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            # print(x.getName())
            solution.append(x.getName())
        self.assertEqual(len(solution), 1)
        self.assertEqual(solution[0], '&')

    def testNotEx2(self):
        objects = toPnf('F p1')
        # print(objects.getName())
        derCaseAnd = derivatives(objects, '{x}')
        solution = []
        # print(derCaseAnd)
        for x in derCaseAnd:
            # print(x.getName())
            solution.append(x.getName())
        self.assertEqual(len(solution), 1)
        self.assertEqual(solution[0], 'U')


def testEx():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testDefintion10Ex1))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
