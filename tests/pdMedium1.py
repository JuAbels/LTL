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
from LTL.tools.lf import lf
from LTL.tools.derivative import derivatives
# from LTL.tools.flat import flat
# from LTL.tools.flat import toWords


class pd(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)
    
    def testPDMedium(self):
        pd = derivatives(toPnf('p2'), "{p2}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual({'tt'}, solu)        
        pd = derivatives(toPnf('& p2 p3'), "{p2, p3}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
            solu.add(x.getFirst().getName())
            solu.add(x.getSec().getName())
        self.assertEqual({'&','tt'}, solu)
        pd = derivatives(toPnf('& p2 | p1 p3'), "{p2, p1, p3}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
            solu.add(x.getFirst().getName())
            solu.add(x.getSec().getName())
        self.assertEqual(solu, {'&','tt'})
    
    def testPDMedium2(self):
        pd = derivatives(toPnf('& p2 | p1 p3'), "{p2}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
            solu.add(x.getFirst().getName())
            solu.add(x.getSec().getName())
        self.assertEqual(solu, set())

    def testPDMedium3(self):
        pd = derivatives(toPnf('& p2 | p3 U p4 p2'), "{p3, p2, p4}")
        #print(">>>",pd)
        self.assertEqual(len(pd), 3)
        solu = set()
        for x in pd:
             #print("-----")
             solu.add(x.getName())
             solu.add(x.getFirst().getName())
             solu.add(x.getSec().getName())
        self.assertEqual(solu, {'&', 'tt', 'U'})
  
    def testPDMedium4(self):
        pd = derivatives(toPnf('& p2 | p3 U p4 p2'), "{p3, p2}")
        #print(">>>",pd)
        self.assertEqual(len(pd), 2)
        solu = set()
        for x in pd:
             #print("-----")
             solu.add(x.getName())
             solu.add(x.getFirst().getName())
             solu.add(x.getSec().getName())
        self.assertEqual(solu, {'&', 'tt'})


def pdMedium():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(pd))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
