"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018

"""
from LTL.tools.toPnfObjects import toObjects, toPnf
from LTL.tools.lf import lf
from collections import Iterable


def derivatives(formulare, inp1):
    # fuction so that decides which part of the Defintion has to be applied.
    #print("derivatives")
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
    return solution


def checkX(my, inp1):  # can we propose that x is unsatisifable
    """print('checkx')
    print(my)
    for x in my:
        print(x.getName(), inp1)
    """
    XXX = getX(inp1)
    XXX.add('tt')
    #print(XXX)
    # changed here a bit. dont know wheter is correct
    helper = set()
    if (isinstance(my, Iterable)):

        for x in my:
            if x.getName() in XXX:# inp1:
                #print("isinstance and in xxx")
                helper.add(True)
            else:
                helper.add(False)
    #print(helper)
    if False in helper:
        return False
    else:
        return True



    ### now this part may not be reached anymore ###
    if type(my) == frozenset:
        # print("frozenset")
        for x in my:
            if(x.getName().strip("\"") in XXX and x.getNeg() is not True):
                #print('in frozenset')
                return True
    else:  # so we got a object
        # print("object")
        if(((my.getName() in XXX) and (my.getName() is not True))):
            return True
    return False


def caseFormel(formular, inp1):
    # function for case literal
    #print('case formel', formular.getName(), inp1) #TODO: ändern
    lfPhi = lf(formular)
    
    #print(lfPhi)
    solution = set()
    for act in lfPhi:
        current = checkX(act[0], inp1)
        #print(current)
        if(current is True):
            solution.add(act[1])
    # print('solution', solution)
    return solution


def caseAnd(literal, inp1):
    # function for and operation of two formualas
    # Input has to be an & with the pointers to the interessting subformulas
    # print('case and') TODO: Ändern
    #print(inp1)
    partMy = caseFormel(literal.getFirst(), inp1)
    partPhi = caseFormel(literal.getSec(), inp1)
    solution = set()
    for i in partMy:
        for j in partPhi:
            #print(toPnf("&"), "<<<<")
            AND = toPnf("&")#toObject[1]
            #print(AND.getName(), "<<<<<<")
            AND.setFirst(i)
            AND.setSec(j)
            solution.add(AND)
            #print(AND.getName(), AND.getFirst().getName(), AND.getSec().getName())
    return solution
