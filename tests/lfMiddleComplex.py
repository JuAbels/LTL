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
import gc
from unittest.case import TestCase
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf
from LTL.tools.flat import flat
from LTL.tools.flat import toWords

class linfacs(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testDummy(self):
        self.assertEqual( 1, 1)
    def testMPart1(self):
        objects = toPnf('U p1 p2')
        linFac = lf(objects)
        self.assertEqual(len(linFac), 2)
        helper = flat(linFac)
        self.assertEqual(len(helper),4)
        ron = []
        for x in helper:
            if(x.getAtom() != True):
                ron.append(x.getName())
                ron.append(x.getFirst().getName())
                ron.append(x.getSec().getName())
        self.assertEqual(ron, ['U','p1','p2'])
    def testMPart2(self):
        objects = toPnf('U p1 R p2 p3')
        linFac = lf(objects)
        part21 = lf(toPnf('R p2 p3'))
        print(">>>>>>")
        for x in part21:
            print(flat(x))
        
        
    def testMedium(self):
        objects = toPnf('U p1 & p2 G F p3')
        #linFac = lf(objects)


def lfMedium():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
