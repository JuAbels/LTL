"""
Authors: Julia Abels & Stefan Strang
University of Freiburg - 2018

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g

U p1 & p2 G F p3

"""
from toPnfObjects import toObjects
from toPnfObjects import toPnf
from lf import lf


zero = {"tt": 0,
        "ff": 1}


one = {"F": 0,
       "G": 1,
       "X": 2}


two = {"&": 0,
       "|": 1,
       "U": 2,
       "R": 3}


derivat = set()


def derivatives(formulare):
    solution= set()
    if(formulare.getName() == 'tt'):
        print("case true")
        solution = caseTrue(formulare)
    elif(formulare.getName() == 'ff'):
        print("case false")
        solution = caseFalse(formulare)
    elif(formulare.getName() == "&"):
        print("case and")
        solution = caseAnd(formulare)
    else:
        #print("case formula")
        solution = caseFormel(formulare)
    """for x in solution:
        print(x.getName())
        print(x.getFirst().getName())
        print(x.getSec().getName())
        print(x.getSec().getFirst().getName())
        print(x.getSec().getSec().getName())
        print(x.getSec().getSec().getFirst().getName())
        print(x.getSec().getSec().getSec().getName())"""
    # here we get just on element, but it has to be a tuple.
    # don really understand the solution from def 10
    return solutionS
    """"
    # translate fromulare in derivative.
    # get objects in list with all pointers
    objects, first = toObjects(formulare)
    print(objects)
    print("Das ist der Name:", first.getName())

    # declaration for going on with recursion
    firstForm = first.pointFirst
    secondForm = first.pointSec
    if firstForm != None:
        print(firstForm.getName())

    if secondForm is None:
        # einstellig
        if firstForm is None:
            sol = firstForm.getName() # hier ist ein fehler. wenn etwas None ist hat es keinen namen und auch keine pointer. 
            sol = frozenset(sol)
            derivat.add(sol)
            print("Aktuelle", derivat)
        else:
            derivative(formulare[2:])

    if firstForm.pointSec:
        # Abfrage ob erste Formel zweistellig
        print("yes")
        sol = derivative(formulare[2:])
        sol = frozenset(sol)
        derivat.add(sol)
        print("Aktuelle menge:", derivat)

    if firstForm.pointFirst is None and firstForm.pointSec is None:
        # caseLiteral for first Formulare
        derivat.add(firstForm.getName())

    if secondForm.pointSec:
        # Abfrage ob zweite Formel zweistellig
        print("yes two")
        sol = derivative(formulare[4:])
        sol = frozenset(sol)
        derivat.add(sol)
        print("Aktuelle menge:", derivat)

    if secondForm.pointFirst is None and secondForm.pointSec is None:
        # caseLiteral for second formulare
        derivat.add(secondForm.getName())

    print(derivat)
    return derivat"""


def derivative(formulare):
    objects, first = toObjects(formulare)
    print(objects)
    print("Das ist der Name:", first.getName())


def caseTrue(literal):
    # function for true case
    # gives back the whole object. that knows if Neg. is flipped or not.
    
    # print(literal.getName())
    return frozenset({literal})


def caseFalse(literal):
    # function for case fasle.
    # give back the whole object. knows if Neg. is flipped or not
    return frozenset({literal})

def getX(): # needs to be clarified
    return {"p", "p2", "q1", "q2"}

def checkX(my): # can we propose that x is unsatisifable
    XXX = getX() # where do we get the x from?
    #print(my)
    #print("my")
    #print(type(my))
    #status = False # maybe here to bitarray
    if type(my) == frozenset:
        for x in my:
            if(x.getName() in XXX and x.getNeg() != True):
                return True
    else: # so we got a object
        if(my.getName() in XXX and neg!= True):
            return True
    return False
    """
    #exit()
    for x in my: ### dont know whether this is the right way to do
        print(x)
        name = x.getName()
        neg = x.getNeg()
        if(name in XXX and neg != True): # maybe not complex enough maybe needs to exhanced to complex formulas
            #print("in if")
            return True
    return False # if x is not in formula and if is negated in formula
    exit()""" 

def caseFormel(formular):
    # function for case literal
    #print(formular)
    lfPhi = lf(formular)
    #print(lfPhi)
    solution = set()
    for act in lfPhi:
        #print(act[0], "act")
        #exit()
        current= checkX(act[0])
        # print(current)
        if(current == True):
            solution.add(act[1])
            #print(act[1])
    return solution # dont know wheter this is apropriate way to give back


def caseAnd(literal):
    # function for and operation of two formualas
    # Input has to be an & with the pointers to the interessting subformulas

    partMy = caseFormel(literal.getFirst())
    partPhi = caseFormel(literal.getSec())
    solution= set()
    for i in partMy:
        for j in partPhi:
            AND = toObjects("&")[1]
            AND.setFirst(i)
            AND.setSec(j)
            solution.add(AND)
    return solution
    #return one, two


# delete this after finishing. need to use it because of reducing of logical
# complexity

if __name__ == "__main__":
    literal = "G F p"
    first = toPnf(literal)
    derivatives(first)
