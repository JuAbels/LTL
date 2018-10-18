"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g

& G p F ! p
"""

import sys
from LTL.tools.ltlToPred import translate
from LTL.tools.getInp import getInp
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.toPnfObjects import returnAlphabet
from LTL.tools.omegaAutomaton import Automaton
from LTL.tools.omegaAutomaton import setTable
from LTL.tools.omegaAutomaton import automat
from LTL.tools.omegaAutomaton import writeAutomaton
from LTL.tools.derivative import derivatives

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
from LTL.tools.tableauDecision import def17


if __name__ == "__main__":
    # print(len(sys.argv))
    # inp = getInp()
    # print(inp)
    # obs = toPnf('U q p')
    # linfacs = lf(toPnf('& ! p U q p'))
    # linfacs = lf(toPnf('U q p'))
    # print(linfacs)



    # results = def17(obs)
    # formulare = translate(inp[0])
    testMain()
    # linfacs = lf(toPnf("| U q p | a b"))
    # file_automat = inp[2]

    # objects = toPnf('& p2 | p3 U p4 p2')  # formulare
    # objects = toPnf('& R X p3 U p1 p3')
    # objects = toPnf('& p1 | p3 U X p4 R p2 p3')
    # def17(toPnf('& p q'), True)

    # objects = toPnf('| p1 R X p2 p1')
    # alphabet = returnAlphabet()  # get all atoms of object formel
    # objects = toPnf('& p1 | p3 U X p4 R p2 p3')
    # derivatives(objects, inp[1])  # inp[1] gives x to the function

    """test = automat(objects, alphabet)

    # writeAutomaton(file_automat, objects, test)

    liste = calcEdges(test.transitionsTable)
    # print(liste, "HIER")
    # toGraph(liste, test.printGoal, test.start, test.alphabet)
    print("test")

    # objects = toPnf('& G p F ! p')
    # def17('& G p F ! p')
    # def17('& G p F ! p')
    # def17('& ! p & X ! p U q p')"""
