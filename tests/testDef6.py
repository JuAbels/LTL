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
from LTL.tools.lf import lf, defSix
from LTL.tools.derivative import derivatives
# from LTL.tools.flat import flat
# from LTL.tools.flat import toWords


class six(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testEmptyCase(self):
        first = toPnf('ff')
        second = toPnf('ff')
        self.assertEqual(defSix(first,second).getName(), 'ff')

    def testEmptyCase2(self):
        second = toPnf('ff')
        third = toPnf('p')
        self.assertEqual(defSix(second, third).getName(), 'ff')

    def testEmptyCase3(self):
        first = toPnf('! p')
        second = toPnf('p')
        self.assertEqual(defSix(first,second).getName(), 'ff')

    def testEmptyMerge(self):
        first = toPnf('q')
        second = toPnf('p')
        solu = defSix(first,second)
        soluSet = set()
        for x in solu:
            soluSet.add(x.getName())
        self.assertEqual(soluSet, {'q','p'})



def def6():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(six))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
