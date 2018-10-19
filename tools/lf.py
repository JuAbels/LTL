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


def caseLiteral(nameObj, formula):
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
    '''Give back (tt, tt) if function called.
    Input: A tt string
    Output: Linear factor for tt => (tt, tt)'''
    tt = lFormula('tt')
    tt.setAtom()
    ttName = tt
    return (ttName, ttName)


def literal(objects):
    '''Give back Linearfactors in case of literal.
    Input: an ltl-formula literal
    Output: (litera, tt)'''
    oneSet = set()  # declaration of set, so that objectname istn't seperate
    oneSet.add(objects)
    oneSet = frozenset(oneSet)  # set to frozenset, so that hashable
    tt = lFormula('tt')
    tt.setAtom()
    ttName = tt
    return (oneSet, ttName)


def caseNext(formular):
    ''' definition for case Next

    Input: formular is an object, so that information of pointFirst and
                      pointSec is also presented.
    Output: (tt, def7(formula))
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
    ''' HelpFunction for set-based conjunctive normal form for case Next
    This is the def7.
    Manipulates the "( ) formula" formula and gives it back
    Input: the formula that has to be manipulated
    Output: Cleaned formula.'''
    oneSet = set()
    # case for formular is an OR or AND
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
    '''Generate linearfactors for the case that we are working on an 'U'.
    Input: in polish normalform - first and second subject of the U.
    Output: Second part of the linearfactor tuple.'''
    iterable = lf(fromCase)
    oneSet = set()
    while iterable:
        tup = iterable.pop()
        first = tup[0]
        second = tup[1]
        lAnd = lFormula("&")
        lUntil = lFormula("U")
        lUntil.setFirst(fromCase)
        lUntil.setSec(untilCase)
        lAnd.setFirst(second)
        lAnd.setSec(lUntil)
        oneSet.add((first, lAnd))
    return oneSet


def release(firstCase, secondCase):
    '''Give back the linearfactors in case of 'R'
    Input: in polish normalform - first and second subject of the U.
    Output: Linearfactors for R x y
    '''
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
    """Check wheter calculation of linear factor is allowed.
    if there are contradictory parts or a part is ff
    then reject and return false(ff)
    Input: two ltl formulas
    Output: Union of both or false."""
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
        solution = set()
        for x in list(my):
            solution.add(x)
        for x in list(ny):
            solution.add(x)
        return frozenset(solution)


def caseAnd(first, second):
    """Build Linearfactors in case of &.
    This function is called when & is found
    Input: First and second location of &
    Output: Linearfactors"""
    myPhi = list(lf(first))
    nyPsi = list(lf(second))
    ofAndSet = set()
    for i in myPhi:
        for j in nyPsi:
            if (type(defSix(i[0], j[0])) != frozenset):
                if defSix(i[0], j[0]).getName() != 'ff':
                    lAnd = lFormula("&")
                    lAnd.setFirst(i[1])
                    lAnd.setSec(j[1])
                    solu = (defSix(i[0], j[0]))
                    ofAndSet.add((solu, lAnd))
            if (type(defSix(i[0], j[0])) == frozenset):

                lAnd = lFormula("&")
                lAnd.setFirst(i[1])
                lAnd.setSec(j[1])
                solu = (defSix(i[0], j[0]))
                ofAndSet.add((solu, lAnd))
    return ofAndSet


def concat(inp):
    """search for & tt formula and reduce it to formula.
    input: ltl formula in linear factors
    output: none but manipulated linear factors."""
    if(type(inp) == tuple):
        return
    if(inp.getName() == '&'):
        if(inp.getFirst().getName() == 'tt' and inp.getSec() is not None):
            inp.setName(inp.getSec().getName())
            inp.setFirst(inp.getSec().getFirst())
            inp.setSec(inp.getSec().getSec())
        if(inp.getSec() is None):
            return
        if(inp.getSec().getName() == 'tt' and inp.getFirst() is not None):
            inp.setName(inp.getFirst().getName())
            if(inp.getName() in doubles or inp.getName() in singles):
                inp.setFirst(inp.getFirst().getFirst())
                inp.setSec(inp.getFirst().getSec())
            else:
                inp.setAtom()


def flatten(linFacs):
    """Reduce the & tt in the linear factors.
    Iterates through the linearfactors
    and calls for concating.
    Input: Linearfactors
    Output: None/ manipulated linear factors."""
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
