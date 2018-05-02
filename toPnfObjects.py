"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

from copy import deepcopy

single = "XFG!"

duo = "UWRMV&|"

class lFormula:

    def __init__(self, name):
        self.name = name
        self.pointFirst = None
        self.pointSec = None
        self.Atom = None
        self.Neg = False

    def setName(self, name):
        self.name = name

    def setAtom(self):
        self.Atom = True

    def setNeg(self):
        if (self.Atom == False):
            self.Atom = True
        else:
            self.Atom = False

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
    inp = inPut.split()
    listedFormula = deepcopy(inp)
    lObjects = []
    """make the objects. stil empty and no pointer"""
    while len(inp) != 0:
        first = inp.pop()
        lObjects.append(lFormula(first))
    # lObjects.reverse()
    listedFormula.reverse()
    inp = listedFormula
    inpObjects = lObjects
    """going over to objects manipulating them."""
    first = False
    sec = False
    for i in range(len(lObjects)):
        if not (lObjects[i].getName() in duo or lObjects[i].getName() in single):
            """setting the Atom attribute. so no pointer goes out"""
            lObjects[i].setAtom()
            sec = first
            first = lObjects[i -1 ]
        else:
            """if object is no item them set pointers
            Diese Stelle ist schlampig gecoded und könnte fehlerpotential haben"""
            if(lObjects[i].getName() in single):
                lObjects[i].setFirst(lObjects[i-1])
                first = lObjects[i] # vllt raus oder anders
                
            if(lObjects[i].getName() in duo):
                lObjects[i].setFirst(lObjects[i-1])
                lObjects[i].setSec(first)
                first = lObjects[i]
    return lObjects, first

def dealQM(lObjects, first):
    print(i.getName())
    prev = i.getFirst()
    if (prev != None):
        print(prev.getName())
    prevprev = i.getSec()
    if (prevprev != None):
        print(prevprev.getName())

def pushIn(lObjects, first):
    dealQM()
    # print(lObjects)
    """print(first.getName())
    for i in lObjects:
        print("---")
        print(i.getName())
        prev = i.getFirst()
        if (prev != None):
            print(prev.getName())
        prevprev = i.getSec()
        if (prevprev != None):
            print(prevprev.getName())"""

def toPnf(inPut):
    lObjects, first = toObjects(inPut)
    pushIn(lObjects, first)

