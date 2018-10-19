"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""


import unittest
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf
from LTL.tools.derivative import derivatives


class pd(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testRelease1(self):
        pd = derivatives(toPnf('R | q1 p2 p3'), "{p2, p3, q1}")

        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual({'tt', 'R'}, solu)
        self.assertEqual(len(pd), 3)

    def testRelease2(self):
        pd = derivatives(toPnf('R | q1 p2 p3'), "{p3}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual({'R'}, solu)

        self.assertEqual(len(pd), 1)

    def testRelease3(self):
        pd = derivatives(toPnf('R | q1 p2 p3'), "{p3, q1}")
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual({'R', 'tt'}, solu)

        self.assertEqual(len(pd), 2)

    def testOr1(self):
        """ | U q p | a b"""
        pd = derivatives(toPnf('| U q p | a b'), "{a, q, p, b}")
        self.assertEqual(len(pd), 4)
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual(solu, {'U', 'tt'})

    def testOr2(self):
        """| U q p | a b"""
        pd = derivatives(toPnf('| U q p | a b'), "{a, p, b}")
        self.assertEqual(len(pd), 3)
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual(solu, {'tt'})

    def testX1(self):
        """X R q p & a b"""
        pd = derivatives(toPnf('X R q p & a b'), "{tt}")
        self.assertEqual(len(pd), 1)
        solu = set()
        for x in pd:
            solu.add(x.getName())
        self.assertEqual(solu, {'R'})


def pdMedium2():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(pd))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
