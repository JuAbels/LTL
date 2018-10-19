"""
Authors: Julia Abels
University of Freiburg - 2018

"""

import unittest

from LTL.tools.toPnfObjects import toPnf
from LTL.tools.tableauDecision import def17


class testTableauDecision(unittest.TestCase):

    def testOneElement(self):
        """test case with one element."""
        testTableau = def17(toPnf('p1'), False)
        self.assertEqual(testTableau, ('p1', ['({p1},tt)']))

    def testAnd(self):
        """test case with operator and."""
        testTableau = def17(toPnf('& p q'), False)
        if testTableau[1] == ['({p,q},tt)']:
            self.assertEqual(testTableau, ('& p q', ['({p,q},tt)']))
        else:
            self.assertEqual(testTableau, ('& p q', ['({q,p},tt)']))

    def testOr(self):
        """test case with operator and."""
        testTableau = def17(toPnf('| p q'), False)
        if testTableau[1] == ['({p},tt)', '({q},tt)']:
            self.assertEqual(testTableau, ('| p q', ['({p},tt)', '({q},tt)']))
        else:
            self.assertEqual(testTableau, ('| p q', ['({q},tt)', '({p},tt)']))

    def testUntil(self):
        """test case with operator and."""
        testTableau = def17(toPnf('U p q'), False)
        if testTableau[1] == ['({q},tt)', '({p},U)']:
            self.assertEqual(testTableau, ('U p q', ['({q},tt)', '({p},U)']))
        else:
            self.assertEqual(testTableau, ('U p q', ['({p},U)', '({q},tt)']))

    def testRelease(self):
        """test case with operator and."""
        testTableau = def17(toPnf('R p q'), False)
        if testTableau[1] == ['({p,q},tt)', '({q},R)']:
            self.assertEqual(testTableau, ('R p q', ['({p,q},tt)', '({q},R)']))
        elif testTableau[1] == ['({q,p},tt)', '({q},R)']:
            self.assertEqual(testTableau, ('R p q', ['({q,p},tt)', '({q},R)']))
        elif testTableau[1] == ['({q},R)', '({q,p},tt)']:
            self.assertEqual(testTableau, ('R p q', ['({q},R)', '({q,p},tt)']))
        else:
            self.assertEqual(testTableau, ('R p q', ['({q},R)', '({p,q},tt)']))


def testTableau():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(testTableauDecision))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
