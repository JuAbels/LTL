"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.lf import setBasedNorm
from LTL.tools.derivative import derivatives
from LTL.tools.iteratedDerivative import itePartialDeriv
from LTL.tools.toPnfObjects import toObjects

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
        return self.start

    def setStatus(self):
        """
        Calculate the status of the omega automaton.
        """
        status = itePartialDeriv(self.formula)
        self.state = self.state.union(status)
        test = self.state  # Testcase
        while test:
            x = test.pop()
            print(x.getName())
        return self.state

    def setGoals(self):
        """
        Calculate goal states of omega automaton.
        """
        TT = toObjects("tt")[1]
        TT.setAtom()
        self.goal.add(TT)
        releaseSet = self.state
        rel = set()
        while releaseSet:           # Laufzeit ist so scheiße, muss evtl anders
            x = releaseSet.pop()    # gemacht, wenn relevant
            # sprint(x.getName())
            if x.getName() == 'R':
                rel.add(x)
        self.goal = self.goal.union(rel)
        # print(self.goal)
        return self.goal


def printAutomaton(objects):
    """
    Function for printing all the states of the omega Automaton.

    objects: start of the formulare, hand commit of main funciton.
    """
    states = Automaton(objects).setStatus()
    transition = Automaton(objects).setTransition()
    start = Automaton(objects).setStart()
    goals = Automaton(objects).setGoals()

    test = states
    states = set()
    while test:
        element = test.pop()
        states.add(element.getName())

    test = transition
    transition = set()
    while test:
        element = test.pop()
        transition.add(element.getName())

    test = start
    start = set()
    while test:
        element = test.pop()
        start.add(element.getName())

    test = goals
    goals = set()
    while test:
        element = test.pop()
        goals.add(element.getName())

    print(states)
    print(transition)
    print(start)
    print(goals)
