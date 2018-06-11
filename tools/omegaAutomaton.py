"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.toPnfObjects import lFormula, toObjects, toPnf
from LTL.tools.ltlToPred import translate
from LTL.tools.lf import lf, setBasedNorm
from LTL.tools.derivative import derivatives

"""Class to generate the omega Automaton"""

xSet = "p, p2, q1, q2"


class Automaton:

    def __init__(self, formula):
        # self.element = element
        self.formula = formula
        self.state = set()
        self.alphabet = xSet
        self.transition = set()
        self.start = set()
        self.goal = set()

    def setTransition(self):
        """
        return the Transition of the omega Automaton with the alphabet and
        the formel.

            return: set with pointer.
        """
        derivative = derivatives(self.formula, self.alphabet)
        self.transition = self.transition.union(derivative)
        return self.transition

    def setStart(self):
        """
        Calculate start conditions.
        """
        norm = setBasedNorm(self.formula)
        self.start = self.start.union(norm)
        while self.start:
            x = self.start.pop()
            print(x.getName(), x.pointFirst.getName(), x.pointSec.getName())
        return self.start
