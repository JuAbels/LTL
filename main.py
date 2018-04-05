"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018
"""

import sys
from ltlToPred import translate
from getInp import getInp
from toGraph import toGraph

if __name__ == "__main__":
    #inp = getInp()
    #print(inp)
    #print(translate(inp))
    toGraph(["A", "B", "C"], [["A","B"],["B","C"]])

