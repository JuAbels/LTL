"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

from LTL.tools.toPnfObjects import toPnf
from LTL.tools.lf import lf
from LTL.tools.derivative import derivatives
import os


def demo1():
    os.system('clear')
    input("Definition of Data Strucutre: ")
    print("Demonstrating '& p q'. translating to PNF-Objects")
    formula = toPnf('& p q')
    os.system('clear')
    print("this is the first ")
    print(formula)
    print("object.getName(): ", )
    print(formula.getName())
    input()
    os.system('clear')
    print("pointing on following")
    print(".getFirst() and .getSec()")
    print("=>", formula.getFirst().getName(), formula.getFirst())
    print("=>", formula.getSec().getName(), formula.getSec())

    input()
    os.system('clear')
    print("now printing LTL'formulas")
    print("also reading from input.txt")
    print("os.system('python3 -m LTL.main input.txt -latex')")
    os.system('python3 -m LTL.main input.txt -latex')
    input()
    os.system('clear')
    print("now demonstrating linear factors")
    input()
    os.system('clear')
    print("demonstrating for | p q")
    linfacs = lf(toPnf('| p q'))
    input()
    print(linfacs)
    input()
    print("kind of unhandy??")
    input()
    os.system('clear')
    print("linearfactors shoud be {({q}, tt),({p}, tt)}")
    input()
    for x in linfacs:
        for y in x:
            if type(y) == frozenset:
                for z in y:
                    print(z.getName())
            else:
                print(y.getName())
    input()
    os.system('clear')
    print("also available for larger formulas")
    print("print(lf(toPnf('U p1 & p2 G F p3')))")
    linfac = lf(toPnf('U p1 & p2 G F p3'))
    input()
    # print('U p1 & p2 G F p3')
    print(linfac)
    input()
    os.system('clear')
    print("Partial derivatives work aswell")
    input()
    print(derivatives(toPnf('G F p1'), '{p1}'))
    input()
    print("what should be something like \n {R ff U tt p1, & U tt p1 R ff ",
          "U tt p1}")
    for x in derivatives(toPnf('G F p1'), '{p1}'):
        print(x.getName())
        print(x.getFirst().getName())
        print(x.getSec().getName())
        print(". . .")
    input()
    os.system('clear')
    print("also first omega automatas available?!?!")

    os.system('python3 -m LTL.mainDemo input.txt')
    input()
    os.system('clear')
    print("and allread a lots of tests")
    input()
    os.system('clear')
    os.system('python3 -m LTL.main input.txt -test')
    input()
    os.system('clear')
    print("no this demo isn't hardcoded")
    os.system('gedit LTL/tools/lf.py')
    input()
    print("what is done yet?")
    input()
    print("1. defintion data strucutre")
    print("2. read in from file and other sources")
    print("3. printing ltl formulas")
    print("4. implementation of lf(def8)")
    print("5. implementation of partial derivatives(def10)")
    print("6. implementation of the AFA(def 16?!?!), aswell as printing"
          "them?!?!??!")
    input()
    os.system('clear')
    print("what is missing?")
    input()
    print("more tests for lf and partial derivatives")
    print("Defintion 17 ")
    print('corrections on the afa?!?')
