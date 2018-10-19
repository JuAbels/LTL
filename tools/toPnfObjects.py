"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

from copy import deepcopy
import sys

single = "XFG!"

duo = "UWRMV&|"

alphabet = set()

"""Class to init objects which are part of the L-Formula"""


class lFormula:

    def __init__(self, name):
        self.name = name
        self.pointFirst = None
        self.pointSec = None
        self.Atom = None
        self.Neg = False

    def setName(self, nombre):
        self.name = nombre

    def setAtom(self):
        self.Atom = True

    def setNeg(self):
        if (self.Neg is False):
            self.Neg = True
        else:
            self.Neg = False

    def setFirst(self, objekt):
        self.pointFirst = objekt

    def setSec(self, objekt):
        self.pointSec = objekt

    def getName(self):
        return self.name

    def getFirst(self):
        return self.pointFirst

    def getSec(self):
        return self.pointSec

    def getAtom(self):
        return self.Atom

    def getNeg(self):
        return self.Neg

    def __del__(self):
        pass


def pointers(obj, lObjects):
    if (obj.getName() in single and obj.getName() not in duo):
        obj.setFirst(lObjects[0])
        lObjects = lObjects[1:]
        if (obj.getFirst().getAtom is not True):
            pointers(obj.getFirst(), lObjects)
    elif (obj.getName() not in single and obj.getName() in duo and
          len(lObjects) != 0):
        obj.setFirst(lObjects[0])
        if len(lObjects) > 0:
            lObjects = lObjects[1:]
        if (obj.getFirst().getAtom is not True):
            lObjects, lObj = pointers(obj.getFirst(), lObjects)
        if len(lObjects) > 0:
            obj.setSec(lObjects[0])
            lObjects = lObjects[1:]
        if (obj.getSec() is not None):
            if (obj.getSec().getAtom is not True):
                lObjects, lObj = pointers(obj.getSec(), lObjects)

    return lObjects, obj


def toObjects(inPut):
    """Iterate over the string and make them to objects.

    Input: inPut is a ltl formula in polish notation
    Output: A list with all Objects and more important first Object
            with all pointers to the following.

    >>> from LTL.tools.toPnfObjects import toObjects
    >>> testObject = toObjects('G F p')[1]
    >>> testObject.getName()
    'G'
    >>> testObject.getAtom() == None
    True
    >>> testObject.getNeg()
    False
    >>> testObject.getFirst().getName()
    'F'
    >>> testObject.getFirst().getFirst().getName()
    'p'
    >>> testObject.getFirst().getFirst().getAtom()
    True

    >>> testObject = toObjects('! p')[1]
    >>> testObject.getName()
    '!'
    >>> testObject.getNeg()
    False
    >>> testObject.getFirst().getName()
    'p'
    >>> testObject.getFirst().getNeg() == False
    True
    >>> testObject.getFirst().getAtom()
    True


    """
    inp = inPut.split()
    lObjects = []
    global alphabet
    # Ensure that alphabet set is empty, if new formulare is called.
    if alphabet != {}:
        alphabet = set()
    """make the objects. stil empty and no pointer"""
    for x in inp:
        lObjects.append(lFormula(x))
    for x in lObjects:
        if(x.getName() not in single and x.getName() not in duo):
            x.setAtom()
            if x.getName() not in alphabet:
                alphabet.add(x.getName())
    deepLObjects = deepcopy(lObjects)
    stuff = pointers(lObjects[0], lObjects[1:])
    lObjects = stuff[0]
    return deepLObjects, stuff[1]


def redEM(lObjects, ele):
    """Eleminate "!" which are still objects. put them als negation
    to the following object"""
    if (ele.getFirst() is not None):
        if (ele.getFirst().getName() == "!"):
            ele.setFirst(ele.getFirst().getFirst())
            ele.getFirst().setNeg()
        lObjects = redEM(lObjects, ele.getFirst())
    if (ele.getSec() is not None):
        if (ele.getSec().getName() == "!"):
            ele.setSec(ele.getSec().getFirst())
            ele.getSec().setNeg()
        lObjects = redEM(lObjects, ele.getSec())
    return lObjects


def dealEM(lObjects, first):
    """Boundary condition for elemination of exclamation marks.
    also a helper for the recursion of redEM().

    Input: list with objects are given and the first object pointing on the
           rest. Including exclamationmarsk.
    Output: list with objects are given and the first object pointing on the
           rest. Excluding exclamationmarsk.

    testing for dealEM & redEM
    >>> from LTL.tools.toPnfObjects import toObjects, dealXFG, dealEM
    >>> testObj = toObjects('! p')
    >>> testObj = dealEM(testObj[0], testObj[1])[1]
    >>> testObj.getName()
    'p'
    >>> testObj.getNeg()
    True
    >>> testSec = toObjects('! & p ! q')
    >>> testSec = dealEM(testSec[0], testSec[1])[1]
    >>> testSec.getName()
    '&'
    >>> testSec.getNeg()
    True
    >>> testSec.getFirst().getName()
    'p'
    >>> testSec.getSec().getName()
    'q'
    >>> testSec.getSec().getNeg()
    True

    """
    if (first.getName() == "!"):
        first = first.getFirst()
        first.setNeg()
    lObjects = redEM(lObjects, first)
    return lObjects, first


def dealXFG(ele):
    """before we can push in to the atoms. which is required for
    the pnf we need to transform not defined operators - XFG.

    Input: An Element that has to be checked.
    Output: Nothing. transforms problematic Notation.
            Objects stay the same, but with different attributes.



    >>> from LTL.tools.toPnfObjects import toObjects, dealXFG
    >>> testObject = toObjects('G F p')[1]
    >>> dealXFG(testObject)
    >>> testObject.getName()
    'R'
    >>> testObject.getFirst().getName()
    'ff'
    >>> testObject.getSec().getName()
    'U'

    >>> testSec = toObjects('& p G q')[1]
    >>> dealXFG(testSec)
    >>> testSec.getName()
    '&'
    >>> testSec.getFirst().getName()
    'p'
    >>> testSec.getSec().getName()
    'R'
    >>> testSec.getSec().getFirst().getName()
    'ff'
    >>> testSec.getSec().getSec().getName()
    'q'


    """
    if(ele.getName() == "F"):
        ele.setName("U")
        ele.setSec(ele.getFirst())
        tt = lFormula('tt')
        ele.setFirst(tt)
        ele.getFirst().setAtom()
    elif(ele.getName() == "G"):
        ele.setName("R")
        ele.setSec(ele.getFirst())
        ff = lFormula('ff')
        ele.setFirst(ff)
        ele.getFirst().setAtom()
    if(ele.getFirst() is not None):
        dealXFG(ele.getFirst())
    if(ele.getSec() is not None):
        dealXFG(ele.getSec())


def debugPrint(ele):
    """just a printer for debugging"""
    print("-----")
    print(ele.getName())
    print(ele.getNeg())
    if(ele.getFirst() is not None):
        print(ele.getFirst().getName())
    if(ele.getSec() is not None):
        print(ele.getSec().getName())
    if(ele.getFirst() is not None):
        debugPrint(ele.getFirst())
    if(ele.getSec() is not None):
        debugPrint(ele.getSec())


def pushIn(ele):
    """recursive in-pushing of the negation until atoms are reached.

    Input:  Elements that are negated.
    Output: Elements. Only atomic elements are negated.

    >>> from LTL.tools.toPnfObjects import toObjects, dealXFG, dealEM ,pushIn
    >>> testObj = toObjects('! & p ! q')
    >>> testObj = dealEM(testObj[0], testObj[1])[1]
    >>> testObj = pushIn(testObj)
    >>> testObj.getName()
    '|'
    >>> testObj.getFirst().getName()
    'p'
    >>> testObj.getSec().getName()
    'q'
    >>> testObj.getFirst().getNeg()
    True
    >>> testObj.getSec().getNeg()
    False


    """

    if (ele.getNeg() is True):
        if(ele.getName() == "U"):
            ele.setName("R")
        elif(ele.getName() == "R"):
            ele.setName("U")
        elif(ele.getName() == "&"):
            ele.setName("|")
        elif(ele.getName() == "|"):
            ele.setName("&")
        if(ele.getAtom() is not True):
            ele.setNeg()
        if(ele.getFirst()is not None):
            ele.getFirst().setNeg()
        if(ele.getSec()is not None):
            ele.getSec().setNeg()
    if(ele.getFirst() is not None):
        pushIn(ele.getFirst())
    if(ele.getSec() is not None):
        pushIn(ele.getSec())
    return ele


def obsToName(nameObj, string):
    """Convert the formula and realted objects to a readable string.
    Input: An empty String and a ltl.Formula object.
    Output: name of ltl formula object and the related following
            pointers.
    >>> from LTL.tools.toPnfObjects import toPnf
    >>> from LTL.tools.tableauDecision import obsToName
    >>> help = toPnf('& p | q a')
    >>> print(obsToName(help, "").strip())
    & p | q a

    """
    if(nameObj.getNeg() is True):
        string = string + "! "
    string = string + nameObj.getName() + " "
    if (nameObj.getFirst() is not None):
        string = obsToName(nameObj.getFirst(), string)
    if (nameObj.getSec() is not None):
        string = obsToName(nameObj.getSec(), string)
    return string


def checkValid(formula, inPut):
    helper = obsToName(formula, "")
    if(helper[0] == 'U' and inPut[0] == 'F'):
        return
    if(helper[0] == 'R' and inPut[0] == 'G'):
        return
    if(inPut[0] == "!"):
        return
    if (helper.strip() != inPut.strip()):
        print("Wrong Formula input")
        sys.exit(1)


def toPnf(inPut):
    """Head-function to get formula in positive normal form
    Input: ltl formula in polish notation.
    Output: object that points on rest-formula. negation only on atoms

    >>> from LTL.tools.toPnfObjects import toPnf
    >>> first = toPnf('! & p ! q')
    >>> testObj.getName()
    '|'
    >>> testObj.getFirst().getName()
    'p'
    >>> testObj.getSec().getName()
    'q'
    >>> testObj.getFirst().getNeg()
    True
    >>> testObj.getSec().getNeg()
    False

    """
    lObjects, first = toObjects(inPut)
    dealXFG(first)
    lObjects, first = dealEM(lObjects, first)
    pushIn(first)
    return first


def returnAlphabet():
    global alphabet
    return alphabet
