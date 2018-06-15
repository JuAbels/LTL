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
from LTL.tools.omegaAutomaton import Automaton
from LTL.tools.omegaAutomaton import printAutomaton
from LTL.tools.omegaAutomaton import setTable
from LTL.tools.derivative import derivatives
import doctest
from LTL.tests.unitTests import test
from LTL.tests.unitTest2 import test2
from LTL.tests.unitTestDef8ex2 import testgfp
from LTL.tests.testMain import testMain
import gc
import os
import shutil
import subprocess
from LTL.tools.toGraphViz import toGraph
from LTL.tools.toGraphViz import calcEdges



if __name__ == "__main__":

    inp = getInp()

    formulare = translate(inp[0])

    objects = toPnf('& p q')#formulare)  # objects to PNF for LF
    #objects = toPnf('R q1 p')#formulare)  # objects to PNF for LF


    #print(lin1)
    #print(lin2)
    """for x in lin2:
        for z in x:
            if type(z) != frozenset:
                print(z.getName())
            else:
                for y in z:
                    print(y.getName())"""
    #linFac = lf(objects)  # Formel to linear Factors
    derivatives(objects, inp[1]) # inp[1] gives x to the function
    testMain()

    printAutomaton(objects)
    matrix = setTable(objects)
    nodes = matrix[0]
    liste = calcEdges(matrix)
    toGraph(nodes, liste)
    print("test")
    # toGraph()
    # linFac = lf(objects)  # Formel to linear Factors
    # (derivatives(objects, inp[1])) # inp[1] gives x to the function
    testMain()
