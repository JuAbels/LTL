"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018

"""
from LTL.tools.toPnfObjects import toObjects
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf

"""
zero = {"tt": 0,
        "ff": 1}


one = {"F": 0,
       "G": 1,
       "X": 2}


two = {"&": 0,
       "|": 1,
       "U": 2,
       "R": 3}

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g
derivat = set()
"""


def derivatives(formulare, inp1):
    # fuction so that decides which part of the Defintion has to be applied.
    solution= set()
    #X = inp1
    if(formulare.getName() == 'tt'):
        solution = caseTrue(formulare)
    elif(formulare.getName() == 'ff'):
        solution = caseFalse(formulare)
    elif(formulare.getName() == "&"):
        #print("case and")
        solution = caseAnd(formulare, inp1)
    else:
        solution = caseFormel(formulare, inp1)
    return solution


def caseTrue(literal):
    # function for true case
    # gives back the whole object. that knows if Neg. is flipped or not.
    return frozenset({literal})


def caseFalse(literal):
    # function for case fasle.
    # give back the whole object. knows if Neg. is flipped or not
    return frozenset({literal})

def getX(inp1):
    solution = set()
    inp1 = inp1.strip().strip("\"")[1:-1].split(",")
    for i in inp1:
        solution.update({i.strip().strip("\"")})
    #print(solution) 
    return solution # {"p", "p2", "q1", "q2"}

def checkX(my, inp1): # can we propose that x is unsatisifable
    XXX = getX(inp1) # where do we get the x from?
    XXX.add('tt')
    if type(my) == frozenset:
        #print("frozenset")
        for x in my:
            if(x.getName().strip("\"") in XXX and x.getNeg() != True):
                return True
    else: # so we got a object
        if(my.getName() in XXX and my.getName() != True):
            #print(my.getName())
            return True
    #for x in my:
    #    print(x.getName())
    return False


def caseFormel(formular, inp1):
    # function for case literal
    lfPhi = lf(formular)
    for x in lfPhi:
         pass
         #print(x[1].getName())
    solution = set()
    for act in lfPhi:
        current= checkX(act[0], inp1)
        #print(current)
        if(current == True):
            solution.add(act[1])
    #print(solution)
    return solution


def caseAnd(literal, inp1):
    # function for and operation of two formualas
    # Input has to be an & with the pointers to the interessting subformulas

    partMy = caseFormel(literal.getFirst(),inp1)
    partPhi = caseFormel(literal.getSec(),inp1)
    solution= set()
    #print(partMy, "partmy")
    #print(partPhi, "partphi")
    for i in partMy:
        for j in partPhi:
            AND = toObjects("&")[1]
            AND.setFirst(i)
            AND.setSec(j)
            solution.add(AND)
    #print(solution)
    return solution


