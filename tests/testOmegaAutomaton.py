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
        """Test for two elements which are interwinded by AND operator"""
        formulare = toPnf('& p1 p2')

    def testOr(self):
        """Test for two elements which are interwinded by OR operator"""
        pass

    def testUntil(self):
        """Test for two elements which are interwinded by UNTIL operator"""
        pass

    def testRelease(self):
        """Test for two elements which are interwinded by RELEASE operator"""
        pass


def testAuto():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testAutomat))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
