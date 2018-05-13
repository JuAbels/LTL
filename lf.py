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

from toPnfObjects import toObjects
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


def lf(formula, lfset=set()):
    """Get the set of Linear factors.

    >>> lf(tt)
    {('tt', 'tt')}

    """
    # objects = toPnf(formula)
    # lfset = set()
    nameObj = formula.getName()

    print("This is the object:", nameObj)

    if nameObj in doubles:
        first = formula.pointFirst
        second = formula.pointSec
        print(first.getName(), second.getName())
        # call for function
        if nameObj == '|':
            firstForm = lf(first)
            secondForm = lf(second)
            lfset = firstForm.union(secondForm)
    elif nameObj in singles:
        if nameObj == 'X':
            tup = caseNext(formula.pointFirst)
            lfset.add(tup)
    else:
        # appeal of helpfunction for new definiton
        tup = caseLiteral(nameObj, formula)
        lfset = lfset.union(tup)
    print("This is lfset:", lfset)
    return lfset


def caseLiteral(nameObj, formula, lfs=set()):
    ''' HELPFunction for request of single dicate subformulares '''
    trueFalse = re.search(r"[ft]", nameObj)
    # case for "tt" and "ff"
    if trueFalse and formula.pointFirst is None:
        test = trueFalse.group()
        if test == "t":
            tup = isTrue()
            lfs.add(tup)
    else:
        # case for literal
        tup = literal(nameObj)
        lfs.add(tup)
    return lfs


def isTrue():
    ''' def for case True '''
    return ('tt', 'tt')


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
    # case for a Literal
    if formular.pointFirst is None:
        oneSet = oneSet.union(setBasedNorm(formular.getName()))
    # case for formular is an OR and AND
    else:
        first = setBasedNorm(formular.pointFirst.getName())
        second = setBasedNorm(formular.pointSec.getName())
        # first = formular.pointFirst
        # second = formular.pointSec
        #if second:
        #    print(makeString(formular))
        if formular.getName() == '|':
            # TODO: if one of the formular is not literal
            oneSet = oneSet.union(first, second)
        else:
            print("TEST")
    oneSet = frozenset(oneSet)
    return ('tt', oneSet)


def makeString(form, solution=""):
    ''' HELPFunction makes a string '''
    first = str(form.pointFirst.getName())
    second = str(form.pointSec.getName())
    operator = str(form.getName())
    if form.pointFirst.pointFirst:
        first = makeString(form.pointFirst)
    if form.pointSec.pointFirst:
        second = makeString(form.pointFirst)
    solution += "%s %s %s" % (first, operator, second)
    return solution


def setBasedNorm(form):
    ''' HELPFunction for set-based conjunctive normal form for case Next '''
    oneSet = set()
    oneSet.add(form)
    oneSet = frozenset(oneSet)
    return oneSet


def release(first, second):
    ''' definition for release form '''
    if first == 'ff':
        setOf = lf(second)
        return(setOf)
