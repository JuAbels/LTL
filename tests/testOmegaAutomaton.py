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


class testAutomat(unittest.TestCase):

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

    def testAnd(self):
        """Test for two elements which are interwinded by AND operator"""
        formulare = toPnf('& p1 p2')
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"& p1 p2"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2"})

    def testOr(self):
        """Test for two elements which are interwinded by OR operator"""
        formulare = toPnf('| p1 p2')
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"p1", "p2"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2"})

    def testUntil(self):
        """Test for two elements which are interwinded by UNTIL operator"""
        formulare = toPnf("U p1 p2")
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2", "U p1 p2"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"U p1 p2"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2",
                                   ("U p1 p2", "tt"): "p2",
                                   ("U p1 p2", "U p1 p2"): "p1"})

    def testRelease(self):
        """Test for two elements which are interwinded by RELEASE operator"""
        formulare = toPnf("R p1 p2")
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2", "R p1 p2"})
        self.assertEqual(testAutomat.printGoal, {"tt", "R p1 p2"})
        self.assertEqual(testAutomat.printStart, {"R p1 p2"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2",
                                   ("R p1 p2", "tt"): "p1 & p2",
                                   ("R p1 p2", "R p1 p2"): "p2"})

    def testComplexityVer1(self):
        """Test more complex formulare"""
        formulare = toPnf("| R p2 p1 p3")
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2", "R p2 p1", "p3"})
        self.assertEqual(testAutomat.printGoal, {"tt", "R p2 p1"})
        self.assertEqual(testAutomat.printStart, {"R p2 p1", "p3"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2",
                                   ("p3", "tt"): "p3",
                                   ("R p1 p2", "tt"): "p1 & p2",
                                   ("R p1 p2", "R p1 p2"): "p1"})

    def testComplexityVer2(self):
        """Test more complex formulare"""
        formulare = toPnf("| R p2 p1 & p2 p3")
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2", "R p2 p1", "p3"})
        self.assertEqual(testAutomat.printGoal, {"tt", "R p2 p1"})
        self.assertEqual(testAutomat.printStart, {"R p2 p1", "p3"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2",
                                   ("p3", "tt"): "p3",
                                   ("R p1 p2", "tt"): "p1 & p2",
                                   ("R p1 p2", "R p1 p2"): "p1"})

    def testComplexityVer3(self):
        """Test more complex formulare"""
        formulare = toPnf("& U p1 | p2 p3 p1")
        alphabet = returnAlphabet()
        testAutomat = automat(formulare, alphabet)
        liste = calcEdges(testAutomat.transitionsTable)
        setAtom = setLabels(liste, len(liste), testAutomat.alphabet)
        self.assertEqual(testAutomat.printState, {"p1", "p2", "U p1 | p2 p3",
                                                  "p3"})
        self.assertEqual(testAutomat.printGoal, {"tt"})
        self.assertEqual(testAutomat.printStart, {"R p2 p1", "p3"})
        self.assertEqual(setAtom, {("p1", "tt"): "p1", ("p2", "tt"): "p2",
                                   ("p3", "tt"): "p3",
                                   ("U p1 | p2 p3", "tt"): "p2 | p3",
                                   ("U p1 | p2 p3", "U p1 | p2 p3"): "p1"})


def testAuto():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testAutomat))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
