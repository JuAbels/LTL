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
    # & R p2 X p3 U p1 p3 
    def tesNext(self):
        objects = toPnf('U p1 p3')
        linFac = lf(objects)
        #print(linFac)
        solu = set()
        for x in linFac:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        solu.add(z.getName())
                else:
                    solu.add(y.getName())
        # linfacs have to be something like
        # {(p3,tt),(p1 , & tt U p1 p3)}
        self.assertEqual(solu,{'tt','p1','p3','U'})
        objects = toPnf('X p3')
        linFac = lf(objects)
        #print(linFac)
        soluX = []
        for x in linFac:
            for y in x:
                soluX.append(y.getName())
        self.assertEqual(soluX, ['tt', 'p3'])
        objects = toPnf('R p2 X p3')
        linFac = lf(objects)
        helper = set()
        for x in linFac:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                       helper.add(z.getName())
                else:
                    helper.add(y.getName() )
        # linfactors have to be something like 
        # {({p2,tt},& tt p3) ,(tt, & R p2 X p3 p3)}
        self.assertEqual(helper, {'p2','&','tt','p3'})
        objects = toPnf('& R p2 X p3 U p1 p3')
        #print("====>",objects.getName())
        #print("====>",objects.getFirst().getName())
        #print("====>",objects.getFirst().getFirst().getName())
        #print("====>",objects.getFirst().getSec().getName())
        #print("====>",objects.getSec().getName())
        #print("====>",objects.getSec().getFirst().getName())
        #print("====>",objects.getSec().getSec().getName())
        linFac = lf(objects)
        total = set()
        self.assertEqual(len(linFac),4)
        """for x in linFac:
            print("------")
            print(x)
            helper = set()
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        print(z.getName())
                else:
                    print(y.getName())
            #print(helper)"""
        
def lfMedium2():
    #print("=======> jub")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
