"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""


import unittest
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf


class linfacs(unittest.TestCase):
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
                if type(y) == tuple or type(y) == frozenset:
                    for z in y:
                        fullterm.add(z.getName())
                else:
                    fullterm.add(y.getName())
        self.assertEqual(fullterm, {'p2', 'p3', 'tt', 'R', 'p1', 'U'})

    def testMedium(self):
        # 'U p1 & p2 G F p3'
        objects = toPnf('F p3')
        lines = lf(objects)
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
