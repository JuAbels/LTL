"""
Authors: Stefan Strang
University of Freiburg - 2018

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g

U p1 & p2 G F p3

"""

from toPnfObjects import lFormula
from toPnfObjects import toObjects
from ltlToPred import translate
from toPnfObjects import toPnf
import doctest
import re

# doubles: U W R V M

doubles = ['U', 'W', 'R', 'V', 'M', '|', '&']

# singles: X F G
singles = ['X', 'F', 'G']

truth = ["tt", 'ff']

# standard: xor f^g, and & && /\ * , or | || \/ + ,
# implication -> -->, equivalence <->,
# negation ! ~


def lf(formula):  # , lfset=set()):
    """Get the set of Linear factors.

    >>> lf(tt)
    {('tt', 'tt')}

    """
    #print(formula)
    # objects = toPnf(formula)
    lfset = set()
    nameObj = formula.getName()

    # print("This is the object:", nameObj)

    if nameObj in doubles:
        first = formula.pointFirst
        second = formula.pointSec
        # call for function
        if nameObj == '|':
            firstForm = lf(first)
            secondForm = lf(second)
            lfset = firstForm.union(secondForm)
        elif nameObj == 'U':
            setUntil = lf(formula.pointSec)
            secSet = caseUntil(formula.pointFirst, formula.pointSec)
            lfset = lfset.union(setUntil, secSet)
        elif nameObj == '&':
            secSet = caseAnd(formula.pointFirst, formula.pointSec)
            lfset = lfset.union(secSet)
        elif nameObj == 'V':
            # firstSet = caseAnd(formula.pointFirst, formula.pointSec)  TODO: case like AND
            secSet = release(formula.pointFirst, formula.pointSec)
            firstSet = "NOTRELEVANT"
            lfset.union(firstSet, secSet)
    elif nameObj in singles:
        if nameObj == 'X':
            tup = caseNext(formula.pointFirst)
            lfset = lfset.union(tup)
    else:
        # appeal of helpfunction for new definiton
        tup = caseLiteral(nameObj, formula)
        lfset = lfset.union(tup)
    # print("This is lfset:", lfset)
    return lfset


def caseLiteral(nameObj, formula):  # , lfs=set()):
    ''' HELPFunction for request of single dicate subformulares '''
    lfs = set()
    trueFalse = re.search(r"[ft]", nameObj)
    # case for "tt" and "ff"
    if trueFalse and formula.pointFirst is None:
        test = trueFalse.group()
        if test == "t":
            tup = isTrue(nameObj)
            lfs.add(tup)
    else:
        # case for literal
        tup = literal(formula)
        lfs.add(tup)
    return lfs


def isTrue(tt):
    ''' def for case True '''
    tt = lFormula('tt')
    ttName = tt.getName()
    return (ttName, ttName)


def literal(objects):
    ''' def for one linteral for linear factors '''
    oneSet = set()  # declaration of set, so that objectname istn't seperate
    oneSet.add(objects)
    oneSet = frozenset(oneSet)  # set to frozenset, so that hashable
    tt = lFormula('tt')
    ttName = tt.getName()
    return (oneSet, ttName)


def caseNext(formular):
    ''' definition for case Next

    formular(object): is an object, so that information of pointFirst and
                      pointSec is also presented.
    return: tuple of definition

    '''
    oneSet = set()
    solution = set()
    tup = setBasedNorm(formular)
    oneSet = oneSet.union(tup)
    tt = lFormula('tt')
    ttName = tt
    while oneSet:
        i = oneSet.pop()
        solution.add((ttName, i))
    print(solution)
    return solution


def setBasedNorm(form):
    ''' HELPFunction for set-based conjunctive normal form for case Next '''
    oneSet = set()
    if form.pointFirst is None:  # case for a Literal
        # oneSet.add(form) TODO
        oneSet.add(form)
        return oneSet
    else:  # case for formular is an OR and AND
        if form.getName() == '|':  # case for OR
            first = setBasedNorm(form.pointFirst)
            second = setBasedNorm(form.pointSec)
            oneSet = oneSet.union(first, second)
            return oneSet
        else:  # case for AND
            first = setBasedNorm(form.pointFirst)
            second = setBasedNorm(form.pointSec)
            second = list(second)
            while first:
                element = first.pop()
                for i in second:
                    oneSet.add('%s & %s' % (element, i))
                return oneSet


def caseUntil(fromCase, untilCase, oneSet=set()):
    ''' definition for case UNTIL '''
    iterable = lf(fromCase)
    # print(fromCase.getName(), untilCase.getName())
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        # form = "& %s U %s %s" % (second, fromCase.getName(), untilCase.getName())
        # TODO: formulare = toObjects(form)  # for case with objects 
        # Done - but just adding the object with the pointers.
        lAnd = lFormula("&") # hier könnte ein fehler sein, falls nicht immer ein neues objekt erzeugt wird
        lUntil = lFormula("U")
        lAnd.setFirst(second)
        lAnd.setSec(lUntil)
        lUntil.setFirst(fromCase)
        lUntil.setSec(untilCase)
        oneSet.add((first, lAnd))
    # print(oneSet)
    return oneSet


def release(firstCase, secondCase, oneSet=set()):
    ''' definition for release form '''
    iterable = lf(secondCase)
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        # form = "& %s V %s %s" % (second, firstCase.getName(), secondCase.getName())
        lAnd = lFormula("&")
        lRel = lFormula("R")
        lRel.setFirst(firstCase)
        lRel.setSec(secondCase)
        lAnd.setFirst(second)
        lAnd.setSec(lRel)
        oneSet.add((first, lAnd.getName()))
    cA = caseAnd(firstCase, secondCase)
    oneSet = oneSet.union(cA)
    return oneSet

def defSix(my, ny): #, first, second): 
    #print(list(my)[0].getName(), list(ny)[0].getName())
    total = list(my) + list(ny)
    # print (total)
    doubleNeg = False
    for i in total:

        for j in total:   # n² => yolo
            if (i.getName() == j.getName() and i.getNeg() != j.getNeg()):
                doubleNeg = True
    # print(doubleNeg)
    if(list(my)[0].getName() == 'ff' or list(ny)[0].getName() == 'ff'):
        return 'ff' ###lFormula('ff')
    elif(doubleNeg == True):
        return 'ff' ########## oder hier vllt besser lFormula('ff') ?!
    else:
        #print(.union(ny)
       
        return (list(my)[0], list(ny)[0]) #### !!! whaaaack!
    
    """total = ([first] + [second])
    doubleNeg = False
    for i in total:

        for j in total:   # n² => yolo
            if (i.getName() == j.getName() and i.getNeg() != j.getNeg()):
                doubleNeg = True
    #print(doubleNeg)
    if(list(my)[0] == 'ff' or list(ny)[0] == 'ff'):
        return 'ff' ########## oder hier vllt besser lFormula('ff') ?!
    elif(doubleNeg == True):
        return 'ff' ########## oder hier vllt besser lFormula('ff') ?!
    else:
        return my.union(ny)
    """

### Achtung! minimalbeispiel. muss auf größere mengen verallgemeinert werden
def caseAnd(first, second):
    # print(first.getName())
    # print(second.getName())
    myPhi = list(lf(first))
    nyPsi = list(lf(second))
    ofSet = set()
    #print(myPhi)

    #print(nyPsi)
    for i in myPhi:
        for j in nyPsi:
            #print(defSix(i[0],j[0]))
            if (defSix(i[0],j[0]) != 'ff'):
                lAnd = lFormula("&")
                #print(defSix(i[0],j[0]))
                #print()
                #print()
                lAnd.setFirst(myPhi[0][1])
                lAnd.setSec(nyPsi[0][1])
                ofSet.add((defSix(i[0],j[0]), lAnd))
    print(ofSet)
    return ofSet

"""my = (myPhi)[0]
    ny = (nyPsi)[0]
    Phi = myPhi[1]
    Psi = nyPsi[1]
    d6 = defSix(((myPhi)[0]), ((nyPsi)[0]), first, second)
    if d6 == 'ff':
        return frozenset()
    else:
        und = lFormula('&')
        und.setFirst(Phi)
        und.setSec(Psi)
        return set({d6, und})
"""

