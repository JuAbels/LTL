"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018

"""
from LTL.tools.toPnfObjects import toObjects, toPnf
from LTL.tools.lf import lf
from collections import Iterable


def derivatives(formulare, inp1):
    """ fuction so that decides which part of the Defintion has to be
    applied."""
    solution = set()
    if(formulare.getName() == 'tt'):
        solution = caseTrue(formulare)
    elif(formulare.getName() == 'ff'):
        solution = caseFalse(formulare)
    elif(formulare.getName() == "&"):
        solution = solution.union(caseAnd(formulare, inp1))
    else:
        solution = caseFormel(formulare, inp1)
    return solution


def caseTrue(literal):
    """function for true case
    gives back the whole object. that knows if Neg. is flipped or not."""
    return frozenset({literal})


def caseFalse(literal):
    """function for case fasle.
    give back the whole object. knows if Neg. is flipped or not"""
    return frozenset({literal})


def getX(inp1):
    """Translate the inp string to a usable set."""
    solution = set()
    inp1 = inp1.strip().strip("\"")[1:-1].split(",")
    for i in inp1:
        solution.update({i.strip().strip("\"")})
    return solution


def checkX(my, inp1):
    """Check wheter x is satisfiable."""
    XXX = getX(inp1)
    XXX.add('tt')
    helper = set()
    if (isinstance(my, Iterable)):
        for x in my:
            if x.getName() in XXX:
                helper.add(True)
            else:
                helper.add(False)
    if False in helper:
        return False
    else:
        return True


def caseFormel(formular, inp1):
    """function for case literal."""
    lfPhi = lf(formular)
    solution = set()
    for act in lfPhi:
        current = checkX(act[0], inp1)
        if(current is True):
            solution.add(act[1])
    return solution


def caseAnd(literal, inp1):
    """ function for and operation of two formualas
     Input has to be an & with the pointers to the interessting
     subformulas"""
    partMy = caseFormel(literal.getFirst(), inp1)
    partPhi = caseFormel(literal.getSec(), inp1)
    solution = set()
    for i in partMy:
        for j in partPhi:
            AND = toPnf("&")
            AND.setFirst(i)
            AND.setSec(j)
            solution.add(AND)
    return solution
