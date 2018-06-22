"""
Authors: Julia Abels & Stefan Strang
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

from LTL.tools.toPnfObjects import lFormula, toObjects, toPnf
#from LTL.tools.toPnfObjects import toObjects
from LTL.tools.ltlToPred import translate
#from LTL.tools.toPnfObjects import toPnf
import gc

import re

# doubles: U W R V M

doubles = ['U', 'W', 'R', 'V', 'M', '|', '&']

# singles: X F G
singles = ['X', 'F', 'G']

truth = ["tt", 'ff']

# standard: xor f^g, and & && /\ * , or | || \/ + ,
# implication -> -->, equivalence <->,
# negation ! ~


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
    lfset=set()
    #print(lfset)
    #print("in lf")
    # objects = toPnf(formula)
    #lfset = set()
    nameObj = formula.getName()
    #print(nameObj)
    if nameObj in doubles:
        
        first = formula.getFirst()
        second = formula.getSec()
        """print(nameObj)
        print(first.getName())
        print(second.getName())"""
        # call for function
        if nameObj == '|':
            firstForm = lf(first)
            secondForm = lf(second)
            lfset = firstForm.union(secondForm)
        elif nameObj == 'U':
            #print('>>>>>>>>>>>>>>>>>>>>>case U')
            #print(first.getName())
            #print(second.getName())
            setUntil = lf(second)
            #print(setUntil)
            secSet = caseUntil(first, second)

            lfset = lfset.union(setUntil, secSet)
            
        elif nameObj == 'R':
            # setUntil = lf(formula.pointSec) ?! allready in def release
            """print("in r")
            print(first.getName())
            print(second.getName())"""
            secSet = release(first, second)
            #print(secSet)

            lfset = lfset.union(secSet)
            """for x in lfset:
                print("-----")
                #print(x)
                for y in x:
                    if type(y) == tuple or type(y) == frozenset:
                        for z in y:
                            print(z.getName())
                else:
                    print(y.getName())"""
        elif nameObj == '&':

            secSet = caseAnd(first, second)
            lfset = lfset.union(secSet)
            
        elif nameObj == 'V':
            # firstSet = caseAnd(formula.pointFirst, formula.pointSec)  now in the def release
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

    #print(">>>>>>")
    #print(lfset)
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
    tt.setAtom()
    ttName = tt #.getName()
    return (ttName, ttName)


def literal(objects):
    ''' def for one linteral for linear factors '''
    oneSet = set()  # declaration of set, so that objectname istn't seperate
    oneSet.add(objects)
    oneSet = frozenset(oneSet)  # set to frozenset, so that hashable
    tt = lFormula('tt')
    tt.setAtom()
    ttName = tt#.getName()
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
    if form.getName() != '|' or form.getName() != '&':  # case for a Literal
        # oneSet.add(form)
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
                    AND = toObjects("&")[1]
                    AND.setFirst(element)
                    AND.setSec(i)
                    oneSet.add(AND)
                return oneSet


def caseUntil(fromCase, untilCase):
    ''' definition for case UNTIL '''
    iterable = lf(fromCase) # maybe allready in lf
    oneSet=set()
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
    #print(my)
    #print(ny)
    #print("----")
    if type(my) == tuple  or type(ny) == tuple:
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
    #print(total)
    #print("----")
    doubleNeg = False
    for i in total:
        for j in total:
            if (i.getName() == j.getName() and i.getNeg() != j.getNeg()):
                doubleNeg = True
    if(list(my)[0].getName() == 'ff' or list(ny)[0].getName() == 'ff'):
        return lFormula('ff')
    elif(doubleNeg == True):
        return lFormula('ff')
    else:
        #print(my, ny)
        solution = []
        for x in list(my):
            solution.append(x)
        for x in list(ny):
            solution.append(x)
        #print(solution)
        #print(">>>>",list(my), list(ny))
        return solution #(list(my)[0], list(ny)[0])


def caseAnd(first, second):
    #print("&")
    #print(first.getName())
    #print(second.getName())
    myPhi = list(lf(first))
    nyPsi = list(lf(second))
    """print("-----")
    print(myPhi)
    print(nyPsi)
    print("xxxxx")
    for x in nyPsi:
        print(x)
        for y in x:
            if type(y) == frozenset:
                for z in y:
                    print(z.getName())
            else:
                print(y.getName())"""
    ofSet = set()
    #print(">>>>>>>>>>>>")
    for i in myPhi:
        #print(i)
        for j in nyPsi:
            #print(j)
            if (defSix(i[0],j[0]) != 'ff'):
                #print("enter")
                lAnd = lFormula("&")
                lAnd.setFirst(i[1])
                lAnd.setSec(j[1])
                ofSet.add((frozenset(defSix(i[0],j[0])), lAnd))
    #print("######")
    """print(ofSet)
    for x in ofSet:
        for y in x:
            if type(y) == tuple:
                for z in y:
                    print(z.getName())
            else:
                print(y.getName())"""
    return ofSet

def concat(inp):
    if(type(inp) == tuple):
        return
    if(inp.getName()=='&'):
        if(inp.getFirst().getName()) == 'tt':
            inp.setName(inp.getSec().getName())
            inp.setFirst(inp.getSec().getFirst())
            inp.setSec(inp.getSec().getSec())
        if(inp.getSec() == None):
            return
        if(inp.getSec().getName() == 'tt'): # this part may be wrong but not likely
            inp.setName(inp.getFirst().getName())
            inp.setFirst(inp.getFirst().getFirst())

            inp.setSec(inp.getFirst().getSec())

def flatten(linFacs):
    for x in linFacs:
        #print(x)
        for j in x:
            #print("------")

            if type(j) == frozenset:
                for y in j:
                   concat(y)
            else:
                concat(j)


if __name__ == "__main__":
    inp = "G F p"
    first = toPnf(inp)
    #print(first.getName())
    linFacs = lf(first)
    flatten(linFacs)
