"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

editor notes:

toGraphViz is now the correct function to print graph
"""

import sys
from ltlToPred import translate
from getInp import getInp
from toGraphViz import toGraph
from ltlPrint import ltlPrint

if __name__ == "__main__":
    inp = getInp()
    #print(inp)
    #print(translate(inp))
    #toGraph(["A", "B", "C"], [["A","B"],["B","C"]])

