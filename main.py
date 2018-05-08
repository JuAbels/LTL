"""
Authors: Julia Abels and Stefan Strang
         University of Freiburg - 2018

editor notes:

toGraphViz is now the correct function to print graph
"""

import sys
from ltlToPred import translate
from getInp import getInp
from lf import lf
from toPnfObjects import toPnf
# <<<<<<< HEAD
from derivative import derivative
#from toGraph import toGraph

if __name__ == "__main__":
    inp = getInp()
    print(inp)
    formulare = translate(inp)
    print("This is Form:", formulare)
    objects = toPnf(formulare)
    linFac = lf(objects)
    print("This is formulare: ", linFac)
    print("")
    test = derivative(formulare)  # appeal derivative def
    print("This is sol:", test)
    #derivative(inp)
    #toGraph(["A", "B", "C"], [["A","B"],["B","C"]])
# =======
#from toGraphViz import toGraph
#from ltlPrint import ltlPrint

# if __name__ == "__main__":
    # inp = getInp()
    #print(inp)
    #print(translate(inp))
    #toGraph(["A", "B", "C"], [["A","B"],["B","C"]])
    #print(ltlPrint('p1 U (p2 & GFp3)'))


# >>>>>>> 0c97b155e0df62d9bb1f4f344c07846f835b0b3b
