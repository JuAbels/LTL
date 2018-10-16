"""
Authors: Julia Abels
University of Freiburg - 2018

"""

import unittest

from LTL.tools.omegaAutomaton import automat
from LTL.tools.toPnfObjects import returnAlphabet
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.toGraphViz import setLabels
from LTL.tools.toGraphViz import calcEdges


class testTableauDecision(unittest.TestCase):

    def testOneElement(self):
        """test case with one element."""
        formulare = toPnf('p1')
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"p1"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1"})


def testTableau():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testTableauDecision))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
