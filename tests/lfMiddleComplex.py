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
    # print("!!!!!!!!!!!!!!!!!!!!!!!")
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testMPart1(self):
        objects = toPnf('U p1 p2')
        linFac = lf(objects)
        self.assertEqual(len(linFac), 2)
        # print(linFac)

    def testMPart2(self):
        objects = toPnf('U p1 R p2 p3')
        linFac = lf(objects)
        part21 = lf(toPnf('R p2 p3'))
        sollPart21 = set()
        for x in part21:
            for y in x:
                if type(y) == tuple or type(y) == frozenset:
                    for z in y:
                        sollPart21.add(z.getName())
                else:
                    sollPart21.add(y.getName())
        self.assertEqual({'p2', 'p3', 'tt', 'p3', 'R'}, sollPart21)
        fullterm = set()
        for x in linFac:
            for y in x:
                # print(y)
                if type(y) == tuple or type(y) == frozenset:
                    for z in y:
                        fullterm.add(z.getName())
                else:
                    fullterm.add(y.getName())
        self.assertEqual(fullterm, {'p2', 'p3', 'tt', 'R', 'p1', 'U'})

    def testMedium(self):
        # 'U p1 & p2 G F p3'
        objects = toPnf('F p3')
        print("================>")
        # print(objects.getName())
        lines = lf(objects)
        # print("----")
        solution = set()
        for x in lines:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual(solution, {'p3', 'tt', 'U'})


def lfMedium():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
