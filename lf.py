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

# doubles: U W R V M

doubles = ['U', 'W', 'R', 'V', 'M', '|', '&']

# singles: X F G
singles = ['X', 'F', 'G']

# standard: xor f^g, and & && /\ * , or | || \/ + ,
# implication -> -->, equivalence <->,
# negation ! ~


def lf(formula):  # lfset=set()):
    """Get the set of Linear factors."""
    # objects = toPnf(formula)
    lfset = set()
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
    else:
        # case for literal
        print("Zwischenstufe", lfset)
        tup = literal(nameObj)
        print(tup)
        lfset.add(tup)

    print(lfset)
    return lfset


def literal(objects):
    # def for one linteral for linear factors
    oneSet = set()
    objects = objects
    oneSet.add(objects)
    oneSet = frozenset(oneSet)
    return (oneSet, 'tt')


def release(first, second):
    # definition for release form
    if first == 'ff':
        setOf = lf(second)
        return(setOf)
