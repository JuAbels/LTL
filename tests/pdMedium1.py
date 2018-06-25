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
# from LTL.tools.lf import lf
from LTL.tools.derivative import derivatives
# from LTL.tools.flat import flat
# from LTL.tools.flat import toWords


class pd(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        self.assertEqual(1, 1)

    def testPDMedium(self):
        pd = derivatives(toPnf('& p2 | p3 U p4 p2'), "{'q'}")
        print(pd)


def pdMedium():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(pd))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)
