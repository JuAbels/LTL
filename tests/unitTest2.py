"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

import unittest
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf


class testLfex1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testLfFp(self):
        objects = toPnf('F p')
        linFac = lf(objects)
        solution = set()
        for x in linFac:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                elif type(y) == tuple:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual({'tt', 'p', 'U'}, solution)
        first = objects.getFirst()
        sec = objects.getSec()
        del first
        del sec
        objects.setFirst(None)
        objects.setSec(None)
        del objects

    def __del__(self):
        pass


def test2():
    load = unittest.TestLoader()
    su = unittest.TestSuite()

    su.addTests(load.loadTestsFromTestCase(testLfex1))

    runn = unittest.TextTestRunner(verbosity=1)
    result2 = runn.run(su)
    print(result2)
