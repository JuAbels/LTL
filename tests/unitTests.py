"""
Authors: Stefan Strang
University of Freiburg - 2018

This is module for explicit testing of large functiosn of the fosaccs2018.

"""

import unittest
import gc
from unittest.case import TestCase
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf

class testLfdef8(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testDummy(self):
        self.assertEqual( 1, 1)

    # some tests from defintion 8
    def testlfL(self):
        objects = toPnf('l')
        linFac = lf(objects) 
        testHelper = []
        for i in linFac:
            first = i[0]
            sec = i[1]
        if type(first) == frozenset:
            for x in first:
                first = x
        self.assertEqual(('l', 'tt'), (first.getName(), sec.getName()))
        del first
        del sec

    def testlfF(self):
        objects = toPnf('ff')
        linFac = lf(objects) 
        self.assertEqual(set(), linFac)
        del linFac

    def testLfOrSimple(self):
        objects = toPnf('| p q')
        linFac = lf(objects)
        helper = set()
        for x in linFac:
            helper.add(x[1].getName())
            
            for y in x[0]: 
                helper.add(y.getName())
                
        self.assertEqual({'tt','q','p'}, helper)
        first = objects.getFirst()
        second = objects.getSec()
        
        del first 
        del second
        objects.setFirst(None)
        objects.setSec(None)
        del objects

    def testLfAndSimple(self):
        objects = toPnf('& p q')
        linFac = lf(objects)
        #print(linFac)
        check = []
        for x in linFac:
            for y in x:
                if type(y) == tuple:
                    for z in y:
                        check.append(z.getName())
                else:
                    check.append(y.getName())
        self.assertEqual(['p','q','tt'],check)
        first = objects.getFirst()
        second = objects.getSec()
        
        del first 
        del second
        objects.setFirst(None)
        objects.setSec(None)
        del objects
        #print(objects)
    def testlfNextSimple(self):
        objects = toPnf('X p')
        linFac = lf(objects)
        #print(linFac)
        solution = []
        for x in linFac:
            for y in x: 
                solution.append(y.getName())
        self.assertEqual([ 'tt', 'p'], solution)
        #print(objects.getName())
        first =  objects.getFirst()
        del first
        objects.setFirst(None)
        del objects
    def testlfUntilSimple(self):
        objects = toPnf('U p q')
        linFac = lf(objects)
        #print(linFac)
        solution = set()
        for x in linFac:
            for y in x: 
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual(solution, {'tt','U','p','q'})
        #print(objects.getName())
        first = objects.getFirst()
        sec = objects.getSec()
        del first
        del sec
        objects.setFirst(None)
        objects.setSec(None)
        del objects
    def testlfGFu(self):
        objects = toPnf('G F u')
        linFac = lf(objects)
        #print(linFac)
        solution = set()
        for x in linFac:
            for y in x: 
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual(solution, {'u','R','tt','&'})
        #print(objects.getName())
        """first = objects.getFirst()
        sec = objects.getSec()
        del first
        del sec
        objects.setFirst(None)
        objects.setSec(None)
        del objects"""
    def testlfFu(self):
        objects = toPnf('F p')
        linFac = lf(objects)
        #print(linFac)
        solution = set()
        for x in linFac:
            for y in x: 
                if type(y) == frozenset:
                    for z in y:
                        solution.add(z.getName())
                else:
                    solution.add(y.getName())
        self.assertEqual(solution, {'tt','p','U'})
        #print(objects.getName())
        """first = objects.getFirst()
        sec = objects.getSec()
        del first
        del sec
        objects.setFirst(None)
        objects.setSec(None)
        del objects"""




    def __del__(self):
        pass



def test():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(testLfdef8))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


if __name__ == "__main__":
    unittest.main()
