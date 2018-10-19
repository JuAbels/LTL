"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives


def test10ex1():
    """
    >>> from LTL.tests.testDef10ExDoc import test10ex1
    >>> test10ex1()
    True
    True

    """
    objects = toPnf('G F p1')
    derCaseAnd = derivatives(objects, '{p1}')
    solution = []
    for x in derCaseAnd:
        solution.append(x.getName())
    helper = (len(solution) == 2)
    helper2 = (solution[1] == '&')
    if helper is True and helper2 is True:
        return True
