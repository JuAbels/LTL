"""Author Stefan Strang, Julia Abels - Uni Freiburg.

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g

!(p1 U (p2 & GFp3))
"""

from graphviz import Digraph
from LTL.tools.omegaAutomaton import stringName
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf
from LTL.tools.tableauDecisionGrafik import calcEdges
from LTL.tools.tableauDecisionGrafik import calcEdgesDict
from LTL.tools.tableauDecisionGrafik import tableauToGraph


class preState:
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
        self.Name = obsToName(nameObj,"").strip()
        # the unstripped name
        self.nameObj = nameObj
        self.nextPre = set()

class State:
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
        self.Name = tupleToName(nameObj,"")
        # the unstripped name
        self.nameObj = nameObj


def tupleToName(obj, string):
    """Convert the given set of linear factors to a readable string."""
    # this may be buggy as a following of wrong depth in lf building
    #print("objekt: ", obj)

    string = string +"("
    #print(obj)
    #print(string)
    for x in obj:
        #string = string + "("
        if type(x) == frozenset:
            string = string +"{"
            for y in x:
                string = string + y.getName() + ","
                #print(y)
            string = string +"}"
        else:
            string = string + x.getName()
        string = string + ","
    string = string + ")"
    #print(string)
    length = len(string)-1
    for x in range(0,length):
        if string[x] == "," and string[x+1] == "}" :
            string = string[:x] +" " + string[x+1:]
    for x in range(0,length):
        if string[x] == "," and string[x+1] == ")" :
            string = string[:x] +" " + string[x+1:]
    # print(string.strip())
    string = string.replace(" ", "")
    return string

def obsToName(nameObj, string):
    """Convert the graph of formula objects to a readable string."""
    if(nameObj.getNeg() == True):
        string = string + "! "
    string = string + nameObj.getName() + " "
    if (nameObj.getFirst() != None):
        string = obsToName(nameObj.getFirst(),string)
    if (nameObj.getSec() != None):
        string = obsToName(nameObj.getSec(),string)
    return string

def getNames(formula):
    """just helper to debug. from objects to obj.getName()"""
    print("----")
    for x in formula:
        for y in x:
            if(type(y) == frozenset):
                for z in y:
                    print(z.getName())
            else:
                print(y.getName())

def checkForU(inp, aSet):
    """ we need to check wheter there is an U p q in the formula.
    this will be done in a recursive way. """
    if(inp.getName() == 'U'):
        aSet.add(inp.getSec().getName()) ### here maybe better not name
        return aSet
    else:
        if(inp.getFirst() != None):
            if(checkForU(inp.getFirst()) != False):
                return checkForU(inp.getFirst())
        if(inp.getSec() != None):
            if(checkForU(inp.getSec()) != False):
                return checkForU(inp.getFirst())
    return False

def checkEnd(node):
    # if allready visited => loop
    # or found in the search for
    # return true
    actual = obsToName(node.nameObj[1],"").strip()
    for x in globalVisited:
        if(actual == x):
            print("allready visited")
            return True
    print("not visited:")
    if(node.nameObj[1].getAtom() == True):
        for x in node.nameObj[0]:
            if x.getName() in globalCheckForX:
                print("searching for")
                return True
    pass



def makeGraph(node):
    firstState = preState(node)
    globalNodes.append(firstState)
    if firstState.Name in globalVisited or firstState.Name == 'tt': # or in found or as atom
        return #firstState
    #print(firstState.Name)
    globalVisited.add(firstState.Name)

    for x in lf(firstState.nameObj):
        actual = State(x)
        globalNodes.append(actual)
        firstState.Pointers.add(actual)
        #actual.Pointers.add(preState(actual.nameObj[1]))
    #print(firstState.Pointers)
    for x in firstState.Pointers:
        x.Pointers.add(makeGraph(x.nameObj[1]))
    """nextPres = set()
    for x in firstState.Pointers:
        for y in x.Pointers:
           nextPres.add(y)
    """
    #firstState.nextPre = nextPres

    return firstState

def printGraph(state):
    #if
    if state != None:
        print(state.Name)
        #print(state.Pointers)
        for x in state.Pointers:
            print(x.Name)
        for x in state.Pointers:
            for y in x.Pointers:
                printGraph(y)




def def17(formula):
    """Implement Algorithm as explained in the annotation.
    """

    global globalVisited
    globalVisited = set()
    #globalVisited.add('U q p')
    global globalCheckForX
    globalCheckForX = checkForU(formula, set())
    global globalNodes
    globalNodes = []
    #globalVisited.add('U q p')
    makeGraph(toPnf('& ! p U q p'))
    printGraph(globalNodes[0])
    results = calcEdgesDict(globalNodes[0])
    edges = calcEdges(results)
    tableauToGraph(edges)
