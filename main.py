"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018
"""

import sys
from ltlToPred import translate
from getInp import getInp
from derivative import derivative
#from toGraph import toGraph

if __name__ == "__main__":
    inp = getInp()
    print(inp)
    formulare = translate(inp)
    str(formulare)
    print(formulare)
    test = derivative(formulare)  # appeal derivative def
    print(test)
    #derivative(inp)
    #toGraph(["A", "B", "C"], [["A","B"],["B","C"]])
