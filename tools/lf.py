"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018

"""

from LTL.tools.toPnfObjects import lFormula, toObjects, toPnf
import re

# doubles: U W R V M

doubles = ['U', 'W', 'R', 'V', 'M', '|', '&']

# singles: X F G
singles = ['X', 'F', 'G']

truth = ["tt", 'ff']


def lf(formula):
    """Get the set of Linear factors.
    Input: object in positive normal form, that points on rest formula
    Output: linear factors according to the input formula.

    more tests in unittesting.

    >>> from LTL.tools.lf import lf
    >>> from LTL.tools.toPnfObjects import toPnf
    >>> solu = lf(toPnf('tt'))
    >>> some = [print(x[0].getName(),x[1].getName()) for x in solu]
    tt tt


    """

    lfset = set()
    nameObj = formula.getName()
    if nameObj in doubles:
        first = formula.getFirst()
        second = formula.getSec()
        # call for function
        if nameObj == '|':
            firstForm = lf(first)
            secondForm = lf(second)
            lfset = firstForm.union(secondForm)
        elif nameObj == 'U':
            setUntil = lf(second)
            secSet = caseUntil(first, second)

            lfset = lfset.union(setUntil, secSet)
        elif nameObj == 'R':
            secSet = release(first, second)
            lfset = lfset.union(secSet)
        elif nameObj == '&':

            secSet = caseAnd(first, second)
            lfset = lfset.union(secSet)
        elif nameObj == 'V':
            secSet = release(first, second)
            firstSet = "NOTRELEVANT"
            lfset.union(firstSet, secSet)
    elif nameObj in singles:
        if nameObj == 'X':
            tup = caseNext(formula.getFirst())
            lfset = lfset.union(tup)
    else:
        # appeal of helpfunction for new definiton
        tup = caseLiteral(nameObj, formula)
        lfset = lfset.union(tup)

    flatten(lfset)

    return lfset


def caseLiteral(nameObj, formula):  # , lfs=set()):
    ''' HELPFunction for request of single dicate subformulares '''
    lfs = set()
    trueFalse = re.search(r"[ft]", nameObj)
    if trueFalse and formula.pointFirst is None:
        test = trueFalse.group()
        if test == "t":
            tup = isTrue(nameObj)
            lfs.add(tup)
    else:
        tup = literal(formula)
        lfs.add(tup)

    return lfs


def isTrue(tt):
    ''' def for case True '''
    tt = lFormula('tt')
    tt.setAtom()
    ttName = tt
    return (ttName, ttName)


def literal(objects):
    ''' def for one linteral for linear factors '''
    oneSet = set()  # declaration of set, so that objectname istn't seperate
    oneSet.add(objects)
    oneSet = frozenset(oneSet)  # set to frozenset, so that hashable
    tt = lFormula('tt')
    tt.setAtom()
    ttName = tt
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
    return solution


def setBasedNorm(form):
    ''' HELPFunction for set-based conjunctive normal form for case Next '''
    oneSet = set()
    # case for formular is an OR and AND
    if form.getName() == '&' or form.getName() == '|':
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
                    AND = toObjects("&")[1]
                    AND.setFirst(element)
                    AND.setSec(i)
                    oneSet.add(AND)
            return oneSet
    else:  # case for a Literal
        oneSet.add(form)
        return oneSet


def caseUntil(fromCase, untilCase):
    ''' definition for case UNTIL '''
    iterable = lf(fromCase)
    oneSet = set()
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        lAnd = lFormula("&")
        lUntil = lFormula("U")
        lAnd.setFirst(second)
        lAnd.setSec(lUntil)
        lUntil.setFirst(fromCase)
        lUntil.setSec(untilCase)
        oneSet.add((first, lAnd))
    return oneSet


def release(firstCase, secondCase):
    ''' definition for release form '''
    iterable = lf(secondCase)
    oneSet = set()
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        lAnd = lFormula("&")
        lRel = lFormula("R")
        lRel.setFirst(firstCase)
        lRel.setSec(secondCase)
        lAnd.setFirst(second)
        lAnd.setSec(lRel)
        oneSet.add((first, lAnd))
    cA = caseAnd(firstCase, secondCase)
    oneSet = oneSet.union(cA)
    return oneSet


def defSix(my, ny):
    if type(my) == tuple or type(ny) == tuple:
        if type(my) == tuple:
            my = list(my)
        if type(ny) == tuple:
            ny = list(ny)
    else:
        if type(my) != frozenset:
            my = {my}
        if type(ny) != frozenset:
            ny = {ny}
    total = list(my) + list(ny)
    doubleNeg = False
    for i in total:
        for j in total:
            if (i.getName() == j.getName() and i.getNeg() != j.getNeg()):
                doubleNeg = True
    if(list(my)[0].getName() == 'ff' or list(ny)[0].getName() == 'ff'):
        return lFormula('ff')
    elif(doubleNeg is True):
        return lFormula('ff')
    else:
        solution = []
        for x in list(my):
            solution.append(x)
        for x in list(ny):
            solution.append(x)
        return solution


def caseAnd(first, second):
    myPhi = list(lf(first))
    nyPsi = list(lf(second))
    ofSet = set()
    for i in myPhi:
        for j in nyPsi:
            if (defSix(i[0], j[0]) != 'ff'):
                lAnd = lFormula("&")
                lAnd.setFirst(i[1])
                lAnd.setSec(j[1])
                ofSet.add((frozenset(defSix(i[0], j[0])), lAnd))
    return ofSet


def concat(inp):
    if(type(inp) == tuple):
        return
    if(inp.getName() == '&'):
        if(inp.getFirst().getName() == 'tt' and inp.getSec() is not None):
            inp.setName(inp.getSec().getName())
            inp.setFirst(inp.getSec().getFirst())
            inp.setSec(inp.getSec().getSec())
        if(inp.getSec() is None):
            return
        # this part may be wrong but not likely
        if(inp.getSec().getName() == 'tt' and inp.getFirst() is not None):
            inp.setName(inp.getFirst().getName())
            if(inp.getName() in doubles or inp.getName() in singles):
                inp.setFirst(inp.getFirst().getFirst())
                inp.setSec(inp.getFirst().getSec())
            else:
                inp.setAtom()


def flatten(linFacs):
    for x in linFacs:
        for j in x:
            if type(j) == frozenset:
                for y in j:
                    concat(y)
            else:
                concat(j)


if __name__ == "__main__":
    inp = "G F p"
    first = toPnf(inp)
    linFacs = lf(first)
    flatten(linFacs)