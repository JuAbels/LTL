"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

editor notes:

toGraphViz is now the correct function to print graph
"""

import sys
from LTL.tools.ltlToPred import translate
from LTL.tools.getInp import getInp
# from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.toPnfObjects import returnAlphabet
from LTL.tools.omegaAutomaton import Automaton
from LTL.tools.omegaAutomaton import setTable
from LTL.tools.omegaAutomaton import automat
from LTL.tools.omegaAutomaton import writeAutomaton
from LTL.tools.derivative import derivatives
from LTL.tools.tableauDecision import decisionTableGraph

# import doctest
# from LTL.tests.unitTests import test
# from LTL.tests.unitTest2 import test2
# from LTL.tests.unitTestDef8ex2 import testgfp
from LTL.tests.testMain import testMain
# import gc
# import os
# import shutil
# import subprocess
from LTL.tools.toGraphViz import toGraph
from LTL.tools.toGraphViz import calcEdges


if __name__ == "__main__":
    print(len(sys.argv))
    inp = getInp()
    formulare = translate(inp[0])
    file_automat = inp[2]

    # objects = toPnf('& p2 | p3 U p4 p2')  # formulare
    # objects = toPnf('& R X p3 U p1 p3')
    objects = toPnf('& p1 | p3 U X p4 R p2 p3')
    # objects = toPnf('| p1 R X p2 p1')
    alphabet = returnAlphabet()  # get all atoms of object formel
    print(alphabet,  "alphabet")

    derivatives(objects, inp[1])  # inp[1] gives x to the function

    # decisionTableGraph(objects)

    test = automat(objects, alphabet)
    print(test.goal, "goal")
    print(test.state, "state")
    print(test.start, "start")
    print(test.transitionsTable)
    print(test.printStart, "\t \t \t START")
    print(test.printState, "\t STATE")
    print(test.printGoal, "\t \t \t GOAL")
    writeAutomaton(file_automat, objects, test)

    liste = calcEdges(test.transitionsTable)
    print(liste, "HIER")
    toGraph(liste, test.printGoal, test.start)
    print("test")
    testMain()
