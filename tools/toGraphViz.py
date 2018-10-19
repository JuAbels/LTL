"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf
from copy import deepcopy
import random

colors = ['black', 'green', 'red', 'antiquewhite4', 'aquamarine4',
          'brown', 'burlywood', 'cadetblue', 'chartreuse',
          'chocolate', 'coral', 'cyan3', 'darkorchid1',
          'deeppink1', 'darkslateblue', 'darkgreen', 'blue4',
          'darkgoldenrod3', 'goldenrod', 'darksalmon', 'darkolivegreen']


def toGraph(edges, goals, start, alphabet):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    edges: dictionary of list of edges with path, key is set of atoms.
    goals: set of goal states (strings).
    start: set of states from automaton.
    alphabet: power set of alphabetelements
    """
    global colors
    g = Digraph('G', filename='omegaAutomaton')

    counter1 = -1    # variable to create start arrow
    for e in start:  # creating start nodes with an arrow which point on start
        # start point of the arrow
        g.node('%d' % (counter1), shape='point')
        if e.getName() == '&':  # case for AND case -> arrow pict to diamond
            first = stringName(e.pointFirst)   # first place of AND
            second = stringName(e.pointSec)    # second place of AND
            # diamond depict node which can go in two different states at
            # same time
            g.node('%d' % (counter1 - 1), label='', shape='diamond')
            # arrow from start node to diamond
            g.edge('%d' % (counter1), '%d' % (counter1 - 1))
            g.edge('%d' % (counter1 - 1), first)
            g.edge('%d' % (counter1 - 1), second)
        else:
            # start point from arrow to node
            g.edge('%d' % (counter1), stringName(e))
        counter1 -= 2  # counting down -> no conflict with counter0

    testCase = []  # list of edges which are drawn before

    # calculate optimisation of labels
    number = len(edges)
    setAtoms = setLabels(edges, number, alphabet)

    counter0 = 0     # variable to create for AND cases diamonds
    colour = ""      # deklarate color of an arrow
    for p in edges:  # go through all edges with same Labeles
        for e in edges[p]:
            if e in testCase:  # if path exists dont't draw it twice
                continue
            key = deepcopy(e)
            key = tuple(key)
            if setAtoms[key] == '':  # case for arrow apply for all power sets
                colour = 'black'
            else:
                colorNumber = random.randint(1, len(colors) - 1)
                colour = colors[colorNumber]
            # case if formulare has an AND and could go in two states.
            if e[1][0] == '&':
                # split string in first place and second place of AND
                first, second = splitString(e[1])
                # declarate diamond node for AND
                g.node('%d' % (counter0), label='', shape='diamond')
                # draw path from last node to diamond
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
            counter0 += 2  # new index for startarrow point
    g.view()


def setLabels(dictionary, number, alphabet):
    '''
    Helpfunction to calculate the labels for the arrows. Keys are the
    path from one edge to other edge. Values is a set of the atoms with which
    the transition is possible.

    dictionary: dictionary of edges.
    number: number of length of subsets of alphabet.
    return: dictionary with key -> pathes
                            values -> optimizet string of formulare.
    '''
    dictLable = {}
    # generate dictionary in which keys are the path and values is a list of
    # alphabet which generate the path
    for i in dictionary:  # go through subsets of alphabet
        # go through pathes that are possible with the subset
        for j in dictionary[i]:
            j = tuple(j)
            if j in dictLable:
                if i not in dictLable[j]:
                    dictLable[j].append(i)
                continue
            else:
                dictLable[j] = [i]

    # simplyfy the pathes
    dictLable = helpSimplyFormulare(dictLable, number, alphabet)

    return dictLable


def helpSimplyFormulare(dictLable, number, alphabet):
    """
    Helpfunction to Simplify Lable sets of a path.

    dictLable<dictionary>: key    -> path of graph as tupel (start, end)
                           value  -> list of set of alphabet

    return<dictionary>: simplified Dictionary
    """
    # go through pathes for simplification
    alphabetList = [i.replace("{", "").replace("}", "") for i in alphabet]
    alphabetList.remove("")
    for i in dictLable:
        # counter to check if a element is in all subsets
        counter = len(dictLable[i])
        # check if all subsets of alphabet on this path
        if counter == number:
            dictLable[i] = ""
            continue
        dictLable[i] = simplifyOneLable(dictLable[i], alphabetList)
    return dictLable


def simplifyOneLable(lable, alphabetList):
    """ Simplify one Lable.

    lable<list>: list of subsets of alphabet that represents the subsets of
                 the transition
    alphabetList<liste>: list of strings. Each string is an subset of power
                         set.

    return<string>: mathematical optimization of subsets.
    """
    # list of subsets of an lable and how many sets they covering
    dictPath = []

    # generate tuple of each subset of alphabet with quantity of subsets they
    # are included
    for subset in alphabetList:
        activeTransitions = []
        literals = subset.split(',') if subset.find(',') != -1 else [subset]
        for transition in lable:
            include = True
            assert len(literals) > 0
            for literal in literals:
                include = include and literal in transition
            if include:
                activeTransitions.append(transition)
        dictPath.append((subset, activeTransitions, len(activeTransitions)))

    # Order active transition so that
    # first tuple in list covering most subsets
    dictPath = sorted(dictPath, key=lambda x: -x[2])

    maxFrequence = dictPath[0][2]
    numCommas = 0
    maxId = 0
    for index, actTrans in enumerate(dictPath):
        # merge of strings, if strings cover same transitions
        # case:
        # [('p1', ['{p1, p2}'], 1), ('p2', ['{p1, p2}'], 1), ('p1, p2',
        # ['{p1, p2}'], 1)]
        # because then not only elementary subset is enough, need of whole
        if actTrans[2] == maxFrequence and actTrans[0].count(",") > numCommas:
            maxId = index
            numCommas = actTrans[0].count(",")

    # Swap positions if active transistion in first place is shorter than
    # any active transition with the same frequence
    dictPath[0], dictPath[maxId] = dictPath[maxId], dictPath[0]

    # optimized string of all sets
    solution = ""

    # list to check if all sets are calculatet with formulare
    testList = []

    # List to compare if all sets of label are covered
    deleteList = deepcopy(lable)

    # generate a formualre of alphabet which cover all sets of the lable
    while deleteList:
        firstFormulare = dictPath[0]  # first alphabet which depict most subsets
        dictPath.pop(0)  # remove this, because it is used
        for i in firstFormulare[1]:
            if i in testList:
                continue
            testList.append(i)
            deleteList.remove(i)
        test = firstFormulare[0]
        if test.find(",") != -1:
            test = firstFormulare[0].replace(",", " &")
        if solution == "":
            solution = solution + test
        else:
            solution = solution + " | " + test
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
    """ Generate from transitionstable a Dictionary which have the information
    with which subset is a transition possible.

    return<dict>: Dictionary describes which edges are possible by transition
            with the set of alphabet.
            key   -> string of subset of alphabet power set
            value -> List of edges
    """
    edgesDict = {}
    # go through tranisions Table and insert possible edges for this subset.s
    for x in dictionary:
        edges = []
        for i in dictionary[x]:
            for j in dictionary[x][i]:
                tup = [i, j]
                edges.append(tup)
        edgesDict[x] = edges
    return edgesDict
