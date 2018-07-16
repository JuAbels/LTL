"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.lf import setBasedNorm
from LTL.tools.derivative import derivatives
from LTL.tools.iteratedDerivative import itePartialDeriv
from LTL.tools.toPnfObjects import toObjects
from copy import deepcopy

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
        self.transitionsTable = {}

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
            i = stringName(i)
            self.transitionsTable[i] = derivative
        return self.transition, self.transitionsTable

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
    transition, table = Automaton(objects).setTransition(states)
    start = Automaton(objects).setStart()
    goals = Automaton(objects).setGoals(objects)
    return states, transition, start, goals, table


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
        start.add(stringName(element))

    test = goals
    goals = set()
    while test:
        element = test.pop()
        goals.add(stringName(element))

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
        first = stringName(formulare.pointFirst)
        pointFirst.append(first)
        second = stringName(formulare.pointSec)
        pointFirst.append(second)
    elif formulare.pointFirst and formulare.pointSec is None:
        first = stringName(formulare.pointFirst)
        pointFirst.append(first)
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


def writeAutomaton(file_in, objects):
    '''
    Function to write every informations of Automaton in an textfile.

    file_in: file to write infromation
    object: formulare
    '''
    states, transition, start, goals, table = automat(objects)
    states, transition, start, goals = printAutomaton(objects, states,
                                                      transition, start,
                                                      goals)
    with open(file_in, 'w') as out:
        out.write("States of the Automaton \n" +
                  "=" * 23 + '\n' + '\n' +
                  "Q: \t \t" + str(states) + '\n' +
                  "Transition: \t" + str(transition) + '\n' +
                  "Start:\t \t" + str(start) + '\n' +
                  "F:\t \t" + str(goals) + '\n' + '\n' + '\n' +
                  "Transition Table \n" +
                  "=" * 16 + '\n' + '\n' +
                  "States \t \t | " + Automaton(objects).alphabet +
                  '\n' + "\t \t | \n"
                  )
        for i in table:
            value = set()
            for j in table[i]:
                value.add(stringName(j))
            if len(i) > 10:
                out.write(i + "\t | " + str(value) + "\n")
            else:
                out.write(i + "\t \t | " + str(value) + "\n")


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
