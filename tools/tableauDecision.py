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
    string = string +"{"
    for x in obj:
        string = string +"("
        for y in x:
            if type(y) == frozenset:
                string = string + "{"
                for z in y:
                    if z.getAtom() == True:
                        string = string +(z.getName()) #+  " "
                    else:
                        string = string +(obsToName(z, "").strip()) #+  " "
                string = string + "},"
            else:
                if y.getAtom() == True:
                    string = string +(y.getName()) #+  " "
                else:
                    string = string +(obsToName(y, "").strip()) #+  " "
        string = string +"),"
    string = string +"}"
    for x in range(0,len(string)-1):
        if string[x] == "," and string[x+1] == "}":
            string = string[:x] + "}"
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

def getGraph(node):# at this point we might need to add it to visited?! maybe allready in checkEnd
    """Building a Graph from States and Prestates."""
    if(node.State == "preState"):
        linFacs = lf(node.nameObj)
        for x in linFacs: 
            newState = State(x)
            node.Pointers.add(newState)
        for x in node.Pointers:
            getGraph(x)
    else:
        # check end
        if (checkEnd(node) == True):

            return # hopping return ist not to powerful
        # go with second as new state
        else:
            pass # new prestate

def def17(formula):
    """Implement Algorithm as explained in the annotation.
    TODO:
    - für den fall, dass es sich um einen prestate als zwischenstadium handelt. den übergang im graph implementieren
    - dafür muss auch gecheckt werden, ob es noch weitere reduktionsregeln gibt und welche dafür in betracht kommen.
    - evtl müssen linearfaktoren geprüft werden, da sie im paperbaum anders zu sein scheinen.

    """
    global globalVisited
    globalVisited = set()
    global globalCheckForX
    globalCheckForX = checkForU(formula, set())

    firstState = preState(formula)
    #globalVisited.add(firstState.Name)
    # print(State(lf(formula)).nameObj)
    #graph = getGraph(firstState)





"""this may be not up to date
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
    return liste"""

