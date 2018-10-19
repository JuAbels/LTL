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

    def testOr(self):
        """should be something like {({p},tt)({b},tt)({q},uqp)({a},tt)}"""
        linfacs = lf(toPnf("| U q p | a b"))
        solution = set()
        for x in linfacs:
            for y in x:
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual(len(linfacs), 4)
        self.assertEqual(solution, {'p', 'b', 'q', 'U', 'a', 'tt'})

    def testX(self):
        """ X R q & a b
        gotta be something like {tt, {R q & a b}}"""
        linfacs = lf(toPnf("X R q & a b"))
        solu = set()
        for x in linfacs:
            for y in x:
                solu.add(y.getName())
        self.assertEqual(solu, {"tt", "R"})


def lfMedium3():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(linfacs))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
