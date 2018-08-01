"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf


colors = ['green', 'red', 'antiquewhite4', 'aquamarine4',
          'brown', 'burlywood', 'cadetblue', 'chartreuse',
          'chocolate', 'coral', 'cyan3', 'darkorchid1',
          'deeppink1', 'darkslateblue', 'darkgreen', 'blue4'
          'darkgoldenrod3', 'goldenrod', 'darksalmon', 'darkolivegreen']

# TODO: bessere Version für den Graphen


def toGraph(edges, goals, start):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    edges: dictionary of list of edges with path, key is set of atoms.
    goals: set of goal states (strings).
    start: set of states from automaton.

    """
    global colors
    g = Digraph('G', filename='hello.gv')
    counter1 = -1
    for e in start:
        # Node one for start path.
        g.node('%d' % (counter1), shape='point')
        if e.getName() == '&':  # case for AND case.
            first = stringName(e.pointFirst)
            second = stringName(e.pointSec)
            g.node('%d' % (counter1 - 1), label='', shape='diamond')
            g.edge('%d' % (counter1), '%d' % (counter1 - 1))
            g.edge('%d' % (counter1 - 1), first)
            g.edge('%d' % (counter1 - 1), second)
        else:
            g.edge('%d' % (counter1), stringName(e))
        counter1 -= 2
    testCase = []
    counter0 = 0
    countColor = 0
    for p in edges:
        for e in edges[p]:
            if e in testCase:
                continue
            if e[1][0] == '&':
                first, second = splitString(e[1])
                g.node('%d' % (counter0), label='', shape='diamond')
                g.edge(e[0], '%d' % (counter0), color=colors[countColor])
                g.edge('%d' % (counter0), first, color=colors[countColor])
                g.edge('%d' % (counter0), second, color=colors[countColor])
                testCase.append(e)
            else:
                g.edge(e[0], e[1], color=colors[countColor])
                testCase.append(e)
            if e[1] in goals:
                g.node(e[1], shape='doublecircle')
            counter0 += 2
        countColor += 1
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
    edgesDict = {}
    for x in dictionary:
        print(x)
        edges = []
        for i in dictionary[x]:
            for j in dictionary[x][i]:
                tup = [i, j]
                edges.append(tup)
        edgesDict[x] = edges
    return edgesDict
