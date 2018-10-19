"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""


import unittest
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
        derCaseAnd = derivatives(objects, '{p1}')
        solution = []
        for x in derCaseAnd:
            solution.append(x.getName())
        self.assertEqual(len(solution), 2)

    def testEx2(self):
        objects = toPnf('F p1')
        derCaseAnd = derivatives(objects, '{p1}')
        solution = []
        for x in derCaseAnd:
            solution.append(x.getName())
        self.assertEqual(len(solution), 2)

    def testNotEx1(self):
        objects = toPnf('G F p1')
        derCaseAnd = derivatives(objects, '{x}')
        solution = []
        for x in derCaseAnd:
            solution.append(x.getName())
        self.assertEqual(len(solution), 1)
        self.assertEqual(solution[0], '&')

    def testNotEx2(self):
        objects = toPnf('F p1')
        derCaseAnd = derivatives(objects, '{x}')
        solution = []
        for x in derCaseAnd:
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
