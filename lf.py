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
    # objects = toPnf(formula)
    lfset = set()
    nameObj = formula.getName()

    print("This is the object:", nameObj)

    if nameObj in doubles:
        first = formula.pointFirst
        second = formula.pointSec
        # call for function
        if nameObj == '|':
            firstForm = lf(first)
            secondForm = lf(second)
            lfset = firstForm.union(secondForm)
        elif nameObj == 'U':
            secSet = caseUntil(formula.pointFirst, formula.pointSec)
        #elif nameObj == '&':
        #    secSet = caseAnd(formula.pointFirst, formula.pointSec)
    elif nameObj in singles:
        if nameObj == 'X':
            tup = caseNext(formula.pointFirst)
            lfset = lfset.union(tup)
    else:
        # appeal of helpfunction for new definiton
        tup = caseLiteral(nameObj, formula)
        lfset = lfset.union(tup)
    print("This is lfset:", lfset)
    return lfset


def caseLiteral(nameObj, formula):  #, lfs=set()):
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
        tup = literal(nameObj)
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
    return (oneSet, 'tt')


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
    while oneSet:
        i = oneSet.pop()
        solution.add(('tt', i))
    return solution


def setBasedNorm(form):
    ''' HELPFunction for set-based conjunctive normal form for case Next '''
    oneSet = set()
    if form.pointFirst is None:  # case for a Literal
        oneSet.add(form.getName())
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
    setUntil = lf(untilCase)
    iterable = lf(fromCase)
    print("BOTH CASCES:", setUntil, iterable)
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        oneSet.add(('%s, %s & %s U %s' % (first, second,
                                          fromCase.getName(),
                                          untilCase.getName())))
    return oneSet


def release(first, second):
    ''' definition for release form '''
    if first == 'ff':
        setOf = lf(second)
        return(setOf)

def caseAnd(first, second):
     # print(first.getName(), second.getName())
     myPhi = lf(first)
     nyPsi = lf(second) 
     print(myPhi)
     print(nyPsi)




