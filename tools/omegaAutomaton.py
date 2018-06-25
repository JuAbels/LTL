"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.lf import setBasedNorm
from LTL.tools.derivative import derivatives
from LTL.tools.iteratedDerivative import itePartialDeriv
from LTL.tools.toPnfObjects import toObjects
import numpy as np

"""Class to generate the omega Automaton"""

xSet = "{p, p2, q1, q2, p3, p4}"


class Automaton:

    def __init__(self, formula):
        self.formula = formula   # the formula with all the pointer
        self.state = set()       # set with state status
        self.alphabet = xSet     # set of alphabet TODO: per input
        self.transition = set()  # set for the transition of automaton
        self.start = set()       # set of start status
        self.goal = set()        # set of the goal status

    def setStart(self):
        """
        Calculate start conditions.
        """
        norm = setBasedNorm(self.formula)
        self.start = self.start.union(norm)
        return self.start

    def setTransition(self, states):
        """
        return the Transition of the omega Automaton with the alphabet and
        the formel.

            return: set with pointer.
        """
        states = list(states)
        for i in states:
            derivative = derivatives(i, self.alphabet)
            self.transition = self.transition.union(derivative)
        return self.transition

    def setStatus(self):
        """
        Calculate the status of the omega automaton.
        """
        status = itePartialDeriv(self.formula)
        self.state = self.state.union(status)
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


def automat(objects):
    """
    Compute elements of omega automat.
    """
    states = Automaton(objects).setStatus()
    transition = Automaton(objects).setTransition(states)
    start = Automaton(objects).setStart()
    goals = Automaton(objects).setGoals()
    return states, transition, start, goals


def printAutomaton(objects, states, transition, start, goals):
    """
    Function for printing all the states of the omega Automaton.

    objects: start of the formulare, hand commit of main funciton.
    """
    # states, transition, start, goals = automat(objects)
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
        if element.pointFirst and element.pointSec:
            start.add("%s %s %s" % (element.pointFirst.getName(),
                      element.getName(), element.pointSec.getName()))
        elif element.pointFirst and element.pointSec is None:
            start.add("%s %s %s" % (element.getName(),
                      element.pointFirst.getName()))
        else:
            start.add(element.getName())

    test = goals
    goals = set()
    while test:
        element = test.pop()
        goals.add(element.getName())

    print("Q: \t \t", states)
    print("Transition: \t", transition)
    print("Start:\t \t", start)
    print("F:\t \t", goals)

    return states, transition, start, goals


def setTable(objects, states):
    """
    Function to compute table for graph.

    return: Matrix with 1 and 0, where 1 means there exists a path from the
            start state to the other states.
            Futhermore, the first line has the order of the statuses. Thereby
            first position is the status of the second list etc.
    """
    matrix = []  # End Matrix
    # states = Automaton(objects).setStatus()
    # calculate states of the automaton

    state = calculateList(states)

    TT = toObjects("tt")[1]
    TT.setAtom()
    state.append(TT)  # append of case "tt", because need for final state

    names = []  # List for order of states, first line matrix later.

    # run-through all states and check there is a path to another state
    for i in state:
        names.append(i.getName())
        trans = derivatives(i, xSet)  # calculate translation for state
        # change to list -> easier to iterate
        trans = [i.getName() for i in trans]
        tup = []  # list for 1 and 0's.
        for j in state:
            j = j.getName()
            if j in trans:  # check if state in transition, then append 1
                tup.append(1)
            else:
                tup.append(0)  # otherwise 0
        matrix.append(tup)
    matrix.insert(0, names)
    matrix.pop()  # last line not relevant, because "tt" is not relevant
    matrix = np.array(matrix)
    print(matrix)
    return matrix


def calculateList(states):
    """ Helpfunction
    Change Set to List.

    states: set of states
    returns: list with no doubeled elements.
    """
    solList = []
    testList = []
    while states:
        element = states.pop()
        testCase = element.getName()
        if testCase not in testList:
            solList.append(element)
            testList.append(testCase)
    return solList
