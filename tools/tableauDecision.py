"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

from LTL.tools.lf import lf
from LTL.tools.tableauDecisionGrafik import calcEdges
from LTL.tools.tableauDecisionGrafik import calcEdgesDict
from LTL.tools.tableauDecisionGrafik import tableauToGraph


class preState:
    """PreState is class that has to be teared down to
       the smallest parts. Aswell as root of the tree/graph.
       Each node of this has to be manipulated with linear factors.
       Solution of lf gives input to generate states"""
    def __init__(self, nameObj):
        # written flag is
        # unwritten = 0
        # written = 1
        self.written = 0
        # state can vary betwenn State and preState
        self.State = "preState"
        # pointers to the next nodes
        self.Pointers = set()
        # getting the name of the node
        # alias stripping objects to string
        self.Name = obsToName(nameObj, "").strip()
        # the unstripped name
        self.nameObj = nameObj
        self.nextPre = set()


class State:
    """Give Objects for the result of lf(preState).
       these will be the leaves of the graph/tree."""
    def __init__(self, nameObj):
        # written flag is
        # unwritten = 0
        # written = 1
        self.written = 0
        # state can vary betwenn State and preState
        self.State = "State"
        # pointers to the next nodes
        self.Pointers = set()
        # getting the name of the node
        # alias stripping objects to string
        self.Name = tupleToName(nameObj, "")
        # the unstripped name
        self.nameObj = nameObj


def tupleToName(obj, string):
    """Convert the given set of linear factors to a readable string.
    Input: a tuple given by linear factors. this is called obj. aswell
           as an empty string.
    Output: Gives back linear factor as readable.
    >>> from LTL.tools.toPnfObjects import toPnf
    >>> from LTL.tools.lf import lf
    >>> from LTL.tools.tableauDecision import tupleToName
    >>> linfacs = lf(toPnf('p'))
    >>> for x in linfacs:
    ...    print(tupleToName(x,""))
    ({p},tt)

    """
    string = string + "("
    for x in obj:
        if type(x) == frozenset:
            string = string + "{"
            for y in x:
                string = string + y.getName() + ","
            string = string + "}"
        else:
            string = string + x.getName()
        string = string + ","
    string = string + ")"
    length = len(string)-1
    for x in range(0, length):
        if string[x] == "," and string[x+1] == "}":
            string = string[:x] + " " + string[x+1:]
    for x in range(0, length):
        if string[x] == "," and string[x+1] == ")":
            string = string[:x] + " " + string[x+1:]
    string = string.replace(" ", "")
    return string


def obsToName(nameObj, string):
    """Convert the formula and realted objects to a readable string.
    Input: An empty String and a ltl.Formula object.
    Output: name of ltl formula object and the related following
            pointers.
    >>> from LTL.tools.toPnfObjects import toPnf
    >>> from LTL.tools.tableauDecision import obsToName
    >>> help = toPnf('& p | q a')
    >>> print(obsToName(help, "").strip())
    & p | q a

    """
    if(nameObj.getNeg() is True):
        string = string + "! "
    string = string + nameObj.getName() + " "
    if (nameObj.getFirst() is not None):
        string = obsToName(nameObj.getFirst(), string)
    if (nameObj.getSec() is not None):
        string = obsToName(nameObj.getSec(), string)
    return string


def getNames(formula):
    """just helper to debug. from objects to obj.getName()"""
    for x in formula:
        for y in x:
            if(type(y) == frozenset):
                for z in y:
                    print(z.getName())
            else:
                print(y.getName())


def checkForU(inp, aSet):
    """check wheter there is an U p q in the formula.
    p and q are variable.
    this will be done in a recursive way.
    Input: Starting with empty set and a ltl-formula
    Output: a set of all found U p q combinations."""
    if(inp.getName() == 'U'):
        aSet.add(inp.getSec().getName())
        return aSet
    else:
        if(inp.getFirst() is not None):
            if(checkForU(inp.getFirst(), set()) is not False):
                return checkForU(inp.getFirst(), set())
        if(inp.getSec() is not None):
            if(checkForU(inp.getSec(), set()) is not False):
                return checkForU(inp.getFirst(), set())
    return False


def checkEnd(node):
    """give back wheter allready visited, found in searched for.
       in that case return true.
    Input: Node of Graph. Gotta be a State.
    Output: True if found. None if not found."""
    actual = obsToName(node.nameObj[1], "").strip()
    for x in globalVisited:
        if(actual == x):
            return True
    if(node.nameObj[1].getAtom() is True):
        for x in node.nameObj[0]:
            if x.getName() in globalCheckForX:
                return True
    pass


def makeGraph(node):
    """Build a tree as seen in Example 6.
    input is the formula and the Graph is build from the pointers.
    This is done in a recursive way and is stopped when a loop is found
    or maximal resolution is reached."""
    print(node.getName())
    firstState = preState(node)
    globalNodes.append(firstState)
    if firstState.Name in globalVisited or firstState.Name == 'tt':
        return  # firstState
    globalVisited.add(firstState.Name)
    for x in lf(firstState.nameObj):
        actual = State(x)
        globalNodes.append(actual)
        firstState.Pointers.add(actual)
    for x in firstState.Pointers:
        x.Pointers.add(makeGraph(x.nameObj[1]))
    return firstState


def printGraph(state):
    """This is a terminal output for the tree.
       Graphical output is found in tableaudecisiongrapfik.py."""
    if state is not None:
        print(state.Name)
        for x in state.Pointers:
            print(x.Name)
        for x in state.Pointers:
            for y in x.Pointers:
                printGraph(y)


def def17(formula, draw):
    """Header function to build decision tableau.
    Setting up frame sets and lists and call the subfunctions.
    Input: Concated LTL formula.
    draw<boolean>: if true, then Graph should be drawn.
    Output: None/ Saved decission tableau.
    """
    global globalVisited
    globalVisited = set()
    global globalCheckForX
    globalCheckForX = checkForU(formula, set())
    global globalNodes
    globalNodes = []
    makeGraph(formula)
    # printGraph(globalNodes[0])

    # From here call the building of the printable graph.
    results = calcEdgesDict(globalNodes[0])
    edges = calcEdges(results)
    if draw:
        tableauToGraph(edges)
    return results
