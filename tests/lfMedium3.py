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
# from LTL.tools.flat import flat
# from LTL.tools.flat import toWords


class linfacs(unittest.TestCase):
    # print("jubjubjub")
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testOr(self):
        # | U q p | a b
        # should be something like {({p},tt)({b},tt)({q},uqp)({a},tt)}
        linfacs = lf(toPnf("| U q p | a b"))
        solution = set()
        for x in linfacs:
            #print("------")
            #helper = set()
            for y in x:

                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
            #solution.append(helper)
        self.assertEqual(len(linfacs), 4)
        #print(solution)
        self.assertEqual(solution, {'p', 'b', 'q', 'U', 'a', 'tt'})

    def testX(self):
        # X R q & a b
        # gotta be something like {tt, {R q & a b}}
        linfacs = lf(toPnf("X R q & a b"))
        #print(linfacs)
        solu = set()
        for x in linfacs:
            for y in x:
                solu.add(y.getName())
        self.assertEqual(solu, {"tt", "R"})

def lfMedium3():
    # print("=======> jub")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
