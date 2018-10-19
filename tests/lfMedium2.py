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

    # & R p2 X p3 U p1 p3
    def testNext(self):
        objects = toPnf('U p1 p3')
        linFac = lf(objects)
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
        self.assertEqual(solu, {'tt', 'p1', 'p3', 'U'})
        objects = toPnf('X p3')
        linFac = lf(objects)
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
                    helper.add(y.getName())
        # linfactors have to be something like
        # {({p2,tt},& tt p3) ,(tt, & R p2 X p3 p3)}
        self.assertEqual(helper, {'p2', '&', 'tt', 'p3'})
        objects = toPnf('& R p2 X p3 U p1 p3')

        linFac = lf(objects)
        self.assertEqual(len(linFac), 4)
        between = set()
        for x in linFac:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        between.add(z.getName())
                else:
                    between.add(y.getName())
        self.assertEqual({'&', 'p3', 'p1', 'p2', 'tt'}, between)


def lfMedium2():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
