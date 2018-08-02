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
        aSet.add(inp.getSec())
        return aSet
    else:
        if(inp.getFirst() != None):
            if(checkForU(inp.getFirst()) != False):
                return checkForU(inp.getFirst())
        if(inp.getSec() != None):
            if(checkForU(inp.getSec()) != False):
                return checkForU(inp.getFirst())
    return False

def def17(formula):
    """Implement Algorithm as explained in the annotation.
    1. check if U is in formula
    2. nodes that are upcomming have to be saved so that 
       it can be checked if it allready exists
    3. calculate lf
    4. check if node state
       yes => partial derivative
       no  => e2
    5. allready existing?
       yes => error e3
       no => go back to # 3.
    6. a way to e3 exists and found
       => valid
    7. graphix
    
    """
    # transfer it to PNF
    # could also be given as input?!
    #print(formula)
    pnf = toPnf(formula)

    # 1. & 2.  
    # check if U is in formula. safing them to ifU so that they
    # can be checked
    ifU = checkForU(pnf, set())
    # print(ifU)
    # so if an U.getSec() ist found we need to search for more than just tt
    # if there is a way to satisfy 
        

    # 3. 
    # doing the linearfactor on it
    decomp = lf(pnf)
    # in the minimal case of U q p it has to be.
    # {({p}, tt),(q, U q p)}
    # by checking for having p in it we now need check 4.

    #print(decomp)
    """for x in decomp:
        print("-----")
        #print(x)
        for y in x:
            if type(y) != frozenset:
                print(y.getName())
            else:
                for z in y:
                    print(z.getName())"""
            #print(y)
            #print(type(y))
    #getNames(decomp)
