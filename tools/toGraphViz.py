"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf


def toGraph(edges, goals, start):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    edges: list of edges with path.
    goals: set of goal states (strings).
    start: set of states from automaton.

    """
    g = Digraph('G', filename='hello.gv')
    # counter2 = 0
    counter0 = 0
    for e in edges:
        if e[1][0] == '&':
            first, second = splitString(e[1])
            g.node('%d' % (counter0), label='', shape='diamond')
            g.edge(e[0], '%d' % (counter0))
            g.edge('%d' % (counter0), first)
            g.edge('%d' % (counter0), second)
        else:
            g.edge(e[0], e[1])
        if e[1] in goals:
            g.node(e[1], shape='doublecircle')
        counter0 += 2
    counter1 = 0
    for e in start:
        # Node one for start path.
        g.node('%d' % (counter1), shape='point')
        if e.pointFirst and e.pointSec:
            first = stringName(e.pointFirst)
            second = stringName(e.pointSec)
            g.node('%d' % (counter1 + 1), label='', shape='diamond')
            g.edge('%d' % (counter1), '%d' % (counter1 + 1))
            g.edge('%d' % (counter1 + 1), first)
            g.edge('%d' % (counter1 + 1), second)
        else:  # case for one literal status.
            g.edge('%d' % (counter1), stringName(e))
        counter1 += 2
    g.view()


def splitString(formualre):
    '''
    Helpfunction to split the string

    formulare: string of fomulare whitch is going to be split.
    return: first  := first subfomulare of function.
            second := second subfomulare of function.
    '''
    objects = toPnf(formualre)
    first = stringName(objects.pointFirst)
    second = stringName(objects.pointSec)
    return first, second


def calcEdges(dictionary):
    # states = len(dictionary)
    edges = []
    for i in dictionary:
        for j in dictionary[i]:
            tup = [i, j]
            edges.append(tup)
    return edges
