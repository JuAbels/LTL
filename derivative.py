"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018
"""

from toPnfObjects import toObjects
from lf import lf


zero = {"tt": 0,
        "ff": 1}


one = {"F": 0,
       "G": 1,
       "X": 2}


two = {"&": 0,
       "|": 1,
       "U": 2,
       "R": 3}


derivat = set()


def derivatives(formulare):
    # translate fromulare in derivative.
    # get objects in list with all pointers
    objects, first = toObjects(formulare)
    print(objects)
    print("Das ist der Name:", first.getName())

    # declaration for going on with recursion
    firstForm = first.pointFirst
    secondForm = first.pointSec

    print(firstForm.getName())

    if secondForm is None:
        # einstellig
        if firstForm is None:
            sol = firstForm.getName()
            sol = frozenset(sol)
            derivat.add(sol)
            print("Aktuelle", derivat)
        else:
            derivative(formulare[2:])

    if firstForm.pointSec:
        # Abfrage ob erste Formel zweistellig
        print("yes")
        sol = derivative(formulare[2:])
        sol = frozenset(sol)
        derivat.add(sol)
        print("Aktuelle menge:", derivat)

    if firstForm.pointFirst is None and firstForm.pointSec is None:
        # caseLiteral for first Formulare
        derivat.add(firstForm.getName())

    if secondForm.pointSec:
        # Abfrage ob zweite Formel zweistellig
        print("yes two")
        sol = derivative(formulare[4:])
        sol = frozenset(sol)
        derivat.add(sol)
        print("Aktuelle menge:", derivat)

    if secondForm.pointFirst is None and secondForm.pointSec is None:
        # caseLiteral for second formulare
        derivat.add(secondForm.getName())

    print(derivat)
    return derivat


def derivative(formulare):
    objects, first = toObjects(formulare)
    print(objects)
    print("Das ist der Name:", first.getName())


def caseTrue():
    # function for true case
    # TODO: change, if name of object is given
    return "tt"


def caseFalse():
    # function for case fasle.
    return "ff"


def caseFormel(formular):
    # function for case literal
    # TODO: right form
    # tuples = lf(formular)
    # check which form it is
    pass


def caseAnd(first, sec):
    # function for and operation of two formualres
    # case for recursion
    # one = caseLiteral(first)
    # two = caseLiteral(sec)
    one = str(first)
    two = str(sec)
    return one, two
