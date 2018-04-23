"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018
"""

call = {"tt": "0",
        "ff": "1",
        "&": "2"}

derivat = set()


def split(formulare):
    # split formulare in subformulare
    first = ""
    sec = ""
    for c in formulare:
        if c != call:
            if c == " ":
                continue
            first += c
        else:
            # da muss noch was gemacht werden, wird nicht funken
            derivative(formulare[c:])
    return first, sec


def derivative(formulare):
    # translate fromulare in derivative.
    # TODO: case for no correct formuulare
    for i in formulare:
        if i in call:
            case = call[i]
            if case == 0:
                derivat.add(caseTrue())
            elif case == 1:
                derivat.add(caseFalse())
            else:  # case == 2:
                first, sec = split(formulare[1:])
                derivat.add(caseAnd())
        elif i == " ":
            continue
        else:
            derivat.add(caseLiteral(i))
    return derivat


def caseTrue():
    # function for true case
    return "tt"


def caseFalse():
    # function for case fasle.
    return False


def caseLiteral(l):
    # function for case literal
    # literal = {l}
    return "<%c, tt>" % l


def caseAnd():
    # function for and operation of two formualres
    # case for recursion
    return "yes"
