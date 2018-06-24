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
    #print("jubjubjub")
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testDummy(self):
        self.assertEqual( 1, 1)

        objects = toPnf('& R p2 X p3 U p1 p3')
        self.assertEqual(objects.getName(),'&')
        self.assertEqual(objects.getFirst().getName(),'R')
        self.assertEqual(objects.getFirst().getFirst().getName(),'p2')
        self.assertEqual(objects.getFirst().getSec().getName(),'X')
        self.assertEqual(objects.getSec().getName(),'U')
        self.assertEqual(objects.getSec().getFirst().getName(),'p1')
        self.assertEqual(objects.getSec().getSec().getName(),'p3')



def structure():
    #print("=======> jub")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
