"""
Authors: Stefan Strang
University of Freiburg - 2018


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

    def testFirst(self):
        inp = toPnf('R | q1 p2 p3')
        linfacs = lf(inp)
        self.assertEqual(len(linfacs), 3)
        total = set()
        for i in linfacs:
            solu = set()
            for j in i:
                if(type(j) == frozenset):
                    for o in j: 
                        solu.add(o.getName())
                else:
                    solu.add(j.getName())
                    if(j.getName() == 'R'):
                        self.assertEqual('|',j.getFirst().getName())
                        self.assertEqual('q1',j.getFirst().getFirst().getName())
                        self.assertEqual('p2',j.getFirst().getSec().getName())
                        self.assertEqual('p3',j.getSec().getName())
            total.add(frozenset(solu))
        self.assertEqual({frozenset({'p3', 'tt', 'p2'}), frozenset({'p3', 'R'}), frozenset({'p3', 'tt', 'q1'})}, total)



def concatErr():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
