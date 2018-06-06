"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

editor notes:

toGraphViz is now the correct function to print graph
"""

import sys
from LTL.tools.ltlToPred import translate
from LTL.tools.getInp import getInp
# from getInp import getInp

from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives
import doctest
from LTL.tests.unitTests import test

#from toGraph import toGraph


if __name__ == "__main__":
    doctest.testmod()
    doctest.testfile("./tools/getInp.py")
    doctest.testfile("./tools/ltlToPred.py")
    doctest.testfile("./tools/toPnfObjects.py")
    doctest.testfile("./tools/lf.py")
    
    test()
    #print(sys.argv[0])
    #print(sys.argv[1])
    #print(sys.argv[2])

    
    inp = getInp()
    #print(inp)
    formulare = translate(inp[0])

    objects = toPnf(formulare)  # objects to PNF for LF
    linFac = lf(objects)  # Formel to linear Factors
    (derivatives(objects, inp[1])) # inp[1] gives x to the function
