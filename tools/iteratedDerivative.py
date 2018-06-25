"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.toPnfObjects import toObjects


doubles = ['U', 'W', 'R', 'V', 'M', '|', '&']


def itePartialDeriv(formulare):
    """ Function for the irerated partial derivatives definition.

        formulare: an object of the formulare
        returns: a set of the formula.
    """
    solution = set()
    form = set()
    if formulare.Atom:
        state = stateTrueFalse(formulare)
        solution = solution.union(state)
        return solution
    elif formulare.getName() == '|' or formulare.getName() == '&':
        state1 = itePartialDeriv(formulare.pointFirst)
        state2 = itePartialDeriv(formulare.pointSec)
        solution = solution.union(state1.union(state2))
        return solution
    elif formulare.getName() == 'X' or formulare.getName() == 'F' or \
            formulare.getName() == 'G':
        state = itePartialDeriv(formulare.pointFirst)
        form.add(formulare)
        solution = solution.union(form.union(state))
        return solution
    elif formulare.getName() == 'U' or formulare.getName() == 'R':
        form.add(formulare)
        state1 = itePartialDeriv(formulare.pointFirst)
        state2 = itePartialDeriv(formulare.pointSec)
        solution = solution.union(form.union(state1.union(state2)))
        return solution


def stateTrueFalse(formulare):
    """
    Helpfunction for test if true case or false case.
    """
    sol = set()
    element = ''
    if formulare.getName() == 'tt':
        element += 'tt'
    elif formulare.getName() == 'ff':
        element += 'ff'
    else:
        element += formulare.getName()
    ELE = toObjects(element)[1]
    ELE.setAtom()
    sol.add(ELE)
    return sol
