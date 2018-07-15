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

xSet = "{p1, p2, q1, q2, p3, p4}"


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

    def setGoals(self, formula):
        """
        Calculate goal states of omega automaton.
        """
        TT = toObjects("tt")[1]
        TT.setAtom()
        self.goal.add(TT)
        releaseSet = Automaton(formula).setStatus()
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
    goals = Automaton(objects).setGoals(objects)
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
        states.add(stringName(element))

    test = transition
    transition = set()
    while test:
        element = test.pop()
        transition.add(stringName(element))

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
        goals.add(stringName(element))

    print("Q: \t \t", states)
    print("Transition: \t", transition)
    print("Start:\t \t", start)
    print("F:\t \t", goals)

    return states, transition, start, goals


def setTable(states):
    """
    Function to compute table for graph.

    return: Matrix with 1 and 0, where 1 means there exists a path from the
            start state to the other states.
            Futhermore, the first line has the order of the statuses. Thereby
            first position is the status of the second list etc.
    """
    dictionary = {}  # End Matrix
    state = calculateList(states)
    for i in state:
        # dictionary[i.getName()] = []
        trans = derivatives(i, xSet)  # calculate translation for state
        # change to list -> easier to iterate
        # TODO: ich brauch die ganze Formel
        trans = [stringName(i) for i in trans]
        key = stringName(i)
        dictionary[key] = trans
    return dictionary


def stringName(formulare):
    """
    Helpfunction to transform a formulare sign to the cottect formulare.

    formulare: one formulare sign.
    return: string of formulare.
    """
    pointFirst = []  # list for fist subformulare of sign
    pointSec = []  # list for second subformulare of sign
    form = ''
    if formulare.pointFirst and formulare.pointSec:
        # case for binary formulare
        if formulare.pointFirst:
            # case for first
            first = stringName(formulare.pointFirst)
            pointFirst.append(first)
        if formulare.pointSec:
            # case for second
            second = stringName(formulare.pointSec)
            pointFirst.append(second)
    if formulare.Atom:
        # case if formulare atom
        form = form + formulare.getName()
    else:
        # case for transform binary form
        form = form + formulare.getName()
        if pointFirst:
            for i in pointFirst:
                form = form + " " + i
        if pointSec:
            for i in pointSec:
                form = form + " " + i
    return form


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
