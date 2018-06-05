"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

from copy import deepcopy

single = "XFG!"

duo = "UWRMV&|"

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


def toObjects(inPut):
    """Iterate over the string and make them to objects.

    Input: inPut is a ltl formula in polish notation
    Output: A list with all Objects and more important first Object
            with all pointers to the following.

    >>> from toPnfObjects import toObjects
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
    # not ordered parts could still be problematic
    inp = inPut.split()
    listedFormula = deepcopy(inp)
    lObjects = []
    """make the objects. stil empty and no pointer"""
    while len(inp) != 0:
        first = inp.pop()
        lObjects.append(lFormula(first))
    listedFormula.reverse()
    inp = listedFormula
    """going over to objects manipulating them."""
    first = False
    for i in range(len(lObjects)):
        if not (lObjects[i].getName() in duo or lObjects[i].getName() in single):
            """setting the Atom attribute. so no pointer goes out"""
            lObjects[i].setAtom()
            # sec = first
            first = lObjects[i - 1]
        else:
            """if object is no item them set pointer."""
            if(lObjects[i].getName() in single):
                lObjects[i].setFirst(lObjects[i-1])
                first = lObjects[i]
            if(lObjects[i].getName() in duo):
                lObjects[i].setFirst(lObjects[i-1])
                lObjects[i].setSec(first)
                first = lObjects[i]
    return lObjects, first


def redEM(lObjects, ele):
    """Eleminate "!" which are still objects. put them als negation
    to the following object"""
    if (ele.getFirst() is not None):
        if (ele.getFirst().getName() == "!"):
            lObjects.remove(ele.getFirst())
            ele.setFirst(ele.getFirst().getFirst())
            ele.getFirst().setNeg()
        lObjects = redEM(lObjects, ele.getFirst())
    if (ele.getSec() is not None):
        if (ele.getSec().getName() == "!"):
            lObjects.remove(ele.getSec())
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
    >>> from toPnfObjects import toObjects
    >>> from toPnfObjects import dealXFG
    >>> from toPnfObjects import dealEM
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
        lObjects.remove(first)
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



    >>> from toPnfObjects import toObjects
    >>> from toPnfObjects import dealXFG
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
    # next: 		Xf - () - still to do - not in paper
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

    >>> from toPnfObjects import toObjects
    >>> from toPnfObjects import dealXFG
    >>> from toPnfObjects import dealEM
    >>> from toPnfObjects import pushIn
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


def toPnf(inPut):
    """Head-function to get formula in positive normal form
    Input: ltl formula in polish notation. 
    Output: object that points on rest-formula. negation only on atoms

    >>> from toPnfObjects import toPnf
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
