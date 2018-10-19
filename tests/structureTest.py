"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""


import unittest
from LTL.tools.toPnfObjects import toPnf


class linfacs(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

        objects = toPnf('& R p2 X p3 U p1 p3')
        self.assertEqual(objects.getName(), '&')
        self.assertEqual(objects.getFirst().getName(), 'R')
        self.assertEqual(objects.getFirst().getFirst().getName(), 'p2')
        self.assertEqual(objects.getFirst().getSec().getName(), 'X')
        self.assertEqual(objects.getSec().getName(), 'U')
        self.assertEqual(objects.getSec().getFirst().getName(), 'p1')
        self.assertEqual(objects.getSec().getSec().getName(), 'p3')


def structure():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
