"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.lf import setBasedNorm
from LTL.tools.derivative import derivatives

"""Class to generate the omega Automaton"""

xSet = "p, p2, q1, q2"


class Automaton:

    def __init__(self, formula):
        self.formula = formula   # the formula with all the pointer
        self.state = set()       # set with state status
        self.alphabet = xSet     # set of alphabet TODO: per input
        self.transition = set()  # set for the transition of automaton
        self.start = set()       # set of start status
        self.goal = set()        # set of the goal status

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
