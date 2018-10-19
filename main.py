"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""
from LTL.tools.getInp import getInp
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.toPnfObjects import returnAlphabet
from LTL.tools.omegaAutomaton import automat
from LTL.tools.omegaAutomaton import writeAutomaton
from LTL.tests.testMain import testMain
from LTL.tools.toGraphViz import toGraph
from LTL.tools.toGraphViz import calcEdges
from LTL.tools.tableauDecision import def17


if __name__ == "__main__":
    inp = getInp()
    formulare = inp[0]

    testMain()  # call testCases

    file_automat = inp[2]

    objects = toPnf(formulare)  # reform formulare to objects.

    alphabet = returnAlphabet()  # get all atoms of object formel
    omegaAutomaton = automat(objects, alphabet)

    writeAutomaton(file_automat, objects, omegaAutomaton)

    liste = calcEdges(omegaAutomaton.transitionsTable)
    toGraph(liste, omegaAutomaton.printGoal, omegaAutomaton.start,
            omegaAutomaton.alphabet)
    def17(objects, True)
