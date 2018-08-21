"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf
from copy import deepcopy
import re
from random import randint

colors = ['black', 'green', 'red', 'antiquewhite4', 'aquamarine4',
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
    # calculate optimisation of labels
    setAtoms = setLabels(edges, number, alphabet)
    counter0 = 0   # variable to create for AND cases diamonds
    countColor = 1
    colour = ""
    for p in edges:
        for e in edges[p]:
            if e in testCase:  # if path exists dont't draw it
                continue
            key = deepcopy(e)
            key = tuple(key)
            if setAtoms[key] == '':
                colour = 'black'
            else:
                colour = colors[countColor]
            # case if formulare has an AND and could go in two states.
            if e[1][0] == '&':
                first, second = splitString(e[1])
                g.node('%d' % (counter0), label='', shape='diamond')
                g.edge(e[0], '%d' % (counter0), color=colour,
                       label=setAtoms[key], fontcolor=colour)
                g.edge('%d' % (counter0), first, color=colour)
                g.edge('%d' % (counter0), second, color=colour)
                testCase.append(e)
            else:
                g.edge(e[0], e[1], color=colour,
                       label=setAtoms[key], fontcolor=colour)
                testCase.append(e)
            # draw another figure (doublecircle) if state is an endstate
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
    # generate dictionary in which keys are the path and values is a list of
    # alphabet which generate the path
    for i in dictionary:
        for j in dictionary[i]:
            j = tuple(j)
            if j in dictLable:
                dictLable[j].append(i)  # dictLable[j] + ", " + i
                continue
            else:
                dictLable[j] = [i]
    # simplyfy the pathes
    dictLable = helpSimplyFormulare(dictLable, number, alphabet)
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
    print(dictLable)
    for i in dictLable:
        # counter to check if a element is in all subsets
        counter = len(dictLable[i])
        # check if all subsets of alphabet on this path
        if counter == number:
            dictLable[i] = ""
            continue
        # simplify function
        dictLable[i] = simplifyOneLable(dictLable[i], alphabetList)
    print(dictLable)
    return dictLable


def simplifyOneLable(lable, alphabetList):
    """ Simplify one Lable.
    """
    dictPath = []
    solution = ""
    for i in alphabetList:
        listTest = [x for x in lable if re.search(i, x) is not None]
        dictPath.append((i, listTest, len(listTest)))
    # first tuple in list covering most subsets
    dictPath = sorted(dictPath, key=lambda x: -x[2])
    testList = []  # list to check if all sets are calculatet with formulare
    deleteList = deepcopy(lable)
    while deleteList:
        firstFormulare = dictPath[0]  # first alphabet which depict most subsets
        dictPath.pop(0)  # remve this, because it is used
        for i in firstFormulare[1]:
            if i in testList:
                continue
            testList.append(i)
            deleteList.remove(i)
        if solution == "":
            solution = solution + firstFormulare[0]
        else:
            solution = solution + " | " + firstFormulare[0]
    print(lable, solution)
    return solution


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
        edges = []
        for i in dictionary[x]:
            for j in dictionary[x][i]:
                tup = [i, j]
                edges.append(tup)
        edgesDict[x] = edges
    return edgesDict
