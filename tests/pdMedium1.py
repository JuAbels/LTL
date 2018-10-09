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
# from LTL.tools.lf import lf
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
        # pd = derivatives(toPnf('& p2 | p3 U p4 p2'), "{'q'}")
        # pd = derivatives(toPnf('& p2 | p1 p3'), "{p2, |}")
        pd = derivatives(toPnf('p2'), "{p2}")
        # print(pd)
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual({'tt'}, solu)        
        pd = derivatives(toPnf('& p2 p3'), "{p2, p3}")
        #print(pd)
        solu = set()
        for x in pd:
            solu.add(x.getName())
            solu.add(x.getFirst().getName())
            solu.add(x.getSec().getName())
        self.assertEqual({'&','tt'}, solu)
        print(">>>>>")
        # like this, it evalueates to not empty set. but is this
        # how we want it to be??? this means iff all came up. but there
        # is an or in it. looks like there could be a semantic error
        # e.g. that when p1 or p3 arent in formula. should it also evaltuate to true? and not to empty set. in this coding it evaluates to empty set
        pd = derivatives(toPnf('& p2 | p1 p3'), "{p2, p1, p2, |}")
        print('!!!!!!!',pd)
        solu = set()
        for x in pd:
            print(x.getName())
            print(x.getFirst().getName())
            print(x.getSec().getName())
        pd = derivatives(toPnf('& p2 | p1 p3'), "{p2, p2, |}")
        print('!!!!!!!',pd)
        solu = set()
        for x in pd:
            print(x.getName())
            print(x.getFirst().getName())
            print(x.getSec().getName())
        
    """ 
    R | q1 p2 p3  	zu true und false
    | U q p | a b 	zu true und false
    X R q p & a b 	zu true und false
    """


def pdMedium():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(pd))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
