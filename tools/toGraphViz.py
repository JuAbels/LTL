"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf
from copy import deepcopy
import re

colors = ['green', 'red', 'antiquewhite4', 'aquamarine4',
          'brown', 'burlywood', 'cadetblue', 'chartreuse',
          'chocolate', 'coral', 'cyan3', 'darkorchid1',
          'deeppink1', 'darkslateblue', 'darkgreen', 'blue4'
          'darkgoldenrod3', 'goldenrod', 'darksalmon', 'darkolivegreen']

# TODO: bessere Version für den Graphen


def toGraph(edges, goals, start, alphabet):
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

    counter1 = -1  # variable to create start arrow
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
    number = len(edges)
    setAtoms = setLabels(edges, number, alphabet)
    counter0 = 0   # variable to create for AND cases diamonds
    countColor = 0
    for p in edges:
        for e in edges[p]:
            if e in testCase:
                continue
            key = deepcopy(e)
            key = tuple(key)
            print(key, "key")
            if e[1][0] == '&':
                first, second = splitString(e[1])
                g.node('%d' % (counter0), label='', shape='diamond')
                g.edge(e[0], '%d' % (counter0), color=colors[countColor],
                       label=setAtoms[key], fontcolor=colors[countColor])
                g.edge('%d' % (counter0), first, color=colors[countColor])
                g.edge('%d' % (counter0), second, color=colors[countColor])
                testCase.append(e)
            else:
                g.edge(e[0], e[1], color=colors[countColor],
                       label=setAtoms[key], fontcolor=colors[countColor])
                testCase.append(e)
            if e[1] in goals:
                g.node(e[1], shape='doublecircle')
            counter0 += 2
        countColor += 1
    g.view()


def setLabels(dictionary, number, alphabet):
    '''
    Helpfunction to calculate the labels for the arrows. Keys are the
    path from one edge to other edge. Values is a set of the atoms with which
    the transition is possible.

    dictionary: dictionary of edges.
    number: number of length of subsets of alphabet.
    return: dictionary.
    '''
    dictLable = {}
    for i in dictionary:
        for j in dictionary[i]:
            j = tuple(j)
            if j in dictLable:
                dictLable[j].append(i)  # dictLable[j] + ", " + i
                continue
            else:
                dictLable[j] = [i]
    dictLable = helpSimplyFormulare(dictLable, number, alphabet)
    for i in dictLable:
        dictLable[i] = str(dictLable[i])
    print(dictLable)
    return dictLable


def helpSimplyFormulare(dictLable, number, alphabet):
    """
    Helpfunction to Simplify Lable sets of a path.

    dictLable<dictionary>: key    -> path of graph
                           value  -> list of set of alphabet

    return<dictionary>: simplified Dictionary
    """
    # go through pathes for simplification
    alphabetList = [i.replace("{", "").replace("}", "") for i in alphabet]
    alphabetList.remove("")
    for i in dictLable:
        solution = ""
        # counter to check if a element is in all subsets
        counter = len(dictLable[i])
        if counter == number:  # check if all subsets of alphabet on this path
            dictLable[i] = ""
            continue
        print(dictLable[i])
        dictPath = {}
        for j in alphabetList:
            print(j)
            listTest = [x for x in dictLable[i] if re.search(j, x) is not None]
            # test if a alphabet is in all other sets
            if len(listTest) == counter:
                solution = solution + j
            else:
                dictPath[(j, len(listTest))] = listTest
        solList = []
        while len(solList) != counter:
            search = list(dictPath)
            print(search)
            solList.append(True)
        dictLable[i] = solution
    print(dictLable)
    return dictLable


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
