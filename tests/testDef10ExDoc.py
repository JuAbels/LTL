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
derivat = set()

"""

# import unittest
# import gc
# from unittest.case import TestCase
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
    # print(objects.getName())
    derCaseAnd = derivatives(objects, 'p1')
    solution = []
    # print(derCaseAnd)
    for x in derCaseAnd:
        # print(x.getName())
        solution.append(x.getName())
    helper = (len(solution) == 2)
    helper2 = (solution[1] == '&')
    if helper is True and helper2 is True:
        return True
