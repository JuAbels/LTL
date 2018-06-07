"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

editor notes:

toGraphViz is now the correct function to print graph
"""

import sys
from LTL.tools.ltlToPred import translate
from LTL.tools.getInp import getInp
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives
import doctest
from LTL.tests.unitTests import test
from LTL.tests.unitTest2 import test2
from LTL.tests.unitTestDef8ex2 import testgfp
import gc
import os
import shutil

def tests():
    doctest.testmod()
    doctest.testfile("./tools/getInp.py")
    doctest.testfile("./tools/ltlToPred.py")
    doctest.testfile("./tools/toPnfObjects.py")
    doctest.testfile("./tools/lf.py")

    test()

    test2()

    testgfp()

if __name__ == "__main__":

    inp = getInp()

    formulare = translate(inp[0])

    objects = toPnf('& p q')#formulare)  # objects to PNF for LF

    linFac = lf(objects)  # Formel to linear Factors
    #(derivatives(objects, inp[1])) # inp[1] gives x to the function
    tests()
