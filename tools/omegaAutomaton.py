"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018
"""

from LTL.tools.lf import setBasedNorm
from LTL.tools.derivative import derivatives
from LTL.tools.iteratedDerivative import itePartialDeriv
from LTL.tools.toPnfObjects import toObjects
from LTL.tools.toPnfObjects import returnAlphabet
import itertools as it

"""Class to generate the omega Automaton"""

xSet = "{p1, p2, q1, q2, p3, p4}"


class Automaton:

    def __init__(self, formula):
        self.formula = formula   # the formula with all the pointer
        self.state = set()       # set with state status
        self.alphabet = []   # set of alphabet TODO: per input
        self.transition = set()  # set for the transition of automaton
        self.start = set()       # set of start status
        self.goal = set()        # set of the goal status
        self.transitionsTable = {}

        self.alphabetTEST = []

        self.printState = set()
        self.printTransition = set()
        self.printStart = set()
        self.printGoal = set()

    def setName(self, nombre):
        self.formulare = nombre

    def getName(self):
        return self.name

    def setStart(self):
        """
        Calculate start conditions.
        """
        norm = setBasedNorm(self.formula)
        self.start = self.start.union(norm)

    def setTransition(self):
        """
        return the Transition of the omega Automaton with the alphabet and
        the formel.

            return: set with pointer.
        """
        states = self.state
        states = calculateList(states)
        for j in self.alphabet:
            '''for i in states:
                derivative = derivatives(i, j)
                self.transition = self.transition.union(derivative)
                i = stringName(i)
                self.transitionsTable[i] = derivative'''
            derivative = setTable(states, j)
            self.transitionsTable[j] = derivative

    def setStatus(self):
        """
        Calculate the status of the omega automaton.
        """
        status = itePartialDeriv(self.formula)
        self.state = self.state.union(status)

    def setGoals(self, formula):
        """
        Calculate goal states of omega automaton.
        """
        TT = toObjects("tt")[1]
        TT.setAtom()
        self.goal.add(TT)
        releaseSet = Automaton(formula).setStatus()
        print(releaseSet, "HIER")
        rel = set()
        while releaseSet:           # Laufzeit ist so scheiße, muss evtl anders
            x = releaseSet.pop()    # gemacht, wenn relevant
            # sprint(x.getName())
            print(x.getName())
            if x.getName() == 'R':
                rel.add(x)
        self.goal = self.goal.union(rel)

    def setAlpabet(self, listAlpha):
        """
        Calculate all subfunctions of possible atoms.

        listAlpha: set of all atoms in formulare.
        """
        # TODO: empty set also?
        setAlpha = it.chain.from_iterable(it.combinations(listAlpha, n) for n in range(len(listAlpha)+1))
        for i in setAlpha:
            stringAlpha = "{"
            for j in i:
                stringAlpha = stringAlpha + j + ","
            stringAlpha = stringAlpha + "}"
            self.alphabet.append(stringAlpha)

    def setPrintState(self):
        test = self.state
        while test:
            element = test.pop()
            self.printState.add(stringName(element))

    def setPrintTransition(self):
        test = self.transition
        while test:
            element = test.pop()
            self.printTransition.add(stringName(element))

    def setPrintStart(self):
        test = self.start
        while test:
            element = test.pop()
            self.printStart.add(stringName(element))

    def setPrintGoal(self):
        test = self.goal
        while test:
            element = test.pop()
            self.printGoal.add(stringName(element))


def automat(objects, alphabet):
    """
    Compute elements of omega automat.

    objects: fomulare for the Automaton.
    alphabet: set of atoms.
    """
    automat = Automaton(objects)
    automat.setAlpabet(alphabet)
    automat.setStatus()
    automat.setTransition()
    automat.setStart()
    automat.setGoals(objects)
    return automat


def printAutomaton(objects, alphabet):
    """
    Compute elements of omega automat for printing.
    """
    automat = Automaton(objects)
    automat.setAlpabet(alphabet)
    automat.setStatus()
    automat.setTransition()
    automat.setStart()
    automat.setGoals(objects)
    automat.setPrintState()
    automat.setPrintTransition()
    automat.setPrintStart()
    automat.setPrintGoal()
    return automat


def setTable(state, setAtom):
    """
    Function to compute table for graph.

    states: all states of automaton.
    return: Matrix with 1 and 0, where 1 means there exists a path from the
            start state to the other states.
            Futhermore, the first line has the order of the statuses. Thereby
            first position is the status of the second list etc.
    """
    dictionary = {}  # End Matrix
    # state = calculateList(states)
    for i in state:
        # state = calculateList(states)
        trans = derivatives(i, setAtom)  # calculate translation for state
        trans = [stringName(i) for i in trans]
        key = stringName(i)
        dictionary[key] = trans
    dictionary.pop('tt', None)
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


def writeAutomaton(file_in, objects, automaton):
    '''
    Function to write every informations of Automaton in an textfile.

    file_in: file to write infromation
    object: formulare
    automaton: the Automat
    '''
    # test = returnAlphabet()
    with open(file_in, 'w') as out:
        out.write("States of the Automaton \n" +
                  "=" * 23 + '\n' + '\n' +
                  "Q: \t \t" + str(automaton.printState) + '\n' +
                  "Transition: \t" + str(automaton.printTransition) + '\n' +
                  "Start:\t \t" + str(automaton.printStart) + '\n' +
                  "F:\t \t" + str(automaton.printGoal) + '\n' + '\n' + '\n' +
                  "Transition Table \n" +
                  "=" * 16 + '\n' + '\n' +
                  "States \t \t | " + Automaton(objects).alphabet +
                  '\n' + "\t \t | \n"
                  )
        for i in automaton.transitionsTable:
            value = set()
            for j in automaton.transitionsTable[i]:
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
