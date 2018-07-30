"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf


def decisionTableGraph(formulare):
    '''
    Function to create decisionTable.

    formulare: is input formulare
    '''
    g = Digraph('G', filename='decision.gv')
    start = stringName(formulare)
    linearFactor = doDecomposition(formulare)
    g.edge(start, linearFactor)
    g.view()


def doDecomposition(formulare):
    '''
    Helpfunction to calulate LF function.
    '''
    liste = []
    start = stringName(formulare)
    liste.append(start)
    end = lf(formulare)
    new = set()
    for i in end:
        if type(i[0]) is frozenset:
            ele = i[0].pop()
            new.add(stringName(ele))
        else:
            first = stringName(i[0])
            new.add(first)
        second = stringName(i[1])
        new.add(second)
    liste.append(new)
    print(liste)
    return liste
