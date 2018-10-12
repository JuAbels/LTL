"""
Authors: Julia Abels
University of Freiburg - 2018

"""

import unittest

from LTL.tools.omegaAutomaton import automat
from LTL.tools.toPnfObjects import returnAlphabet
from LTL.tools.toPnfObjects import toPnf


class testAutomat(unittest.TestCase):

    def testOneElement(self):
        """test case with one element."""
        formulare = toPnf('p1')
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        self.assertEqual(testAutomat.printState, {"p1"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"p1"})

    def testAnd(self):
        pass

    def testOr(self):
        pass

    def testUntil(self):
        pass

    def testRelease(self):
        pass


def testAuto():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testAutomat))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
