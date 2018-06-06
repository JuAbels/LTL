"""
Authors: Stefan Strang
University of Freiburg - 2018

This is module for explicit testing of large functiosn of the fosaccs2018.

"""

import unittest
from unittest.case import TestCase


class testLf(unittest.TestCase):
    def setUp(self):
        print("setup")
    
    def tearDown(self):
        print("tear down")
    def test(self):
        self.assertEqual( 1, 1)


def test():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(testLf))
    
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(result)

if __name__ == '__main__':
    unittest.main()
