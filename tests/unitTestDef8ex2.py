"""
Authors: Stefan Strang
University of Freiburg - 2018


"""

from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf


def testgfp():
    """
    >>> from LTL.tests.unitTestDef8ex2 import testgfp
    >>> testgfp()
    True

    """
    obs2 = toPnf('G F u')
    lin2 = lf(obs2)
    solution = set()
    for x in lin2:
        for y in x:
            if type(y) == frozenset:
                for t in y:
                    solution.add(t.getName())
            else:
                solution.add(y.getName())
    return solution == set({'u', 'R', 'tt', '&'})
