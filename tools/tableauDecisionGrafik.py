"""Author Stefan Strang, Julia Abels - Uni Freiburg.


"""

from graphviz import Digraph
# from LTL.tools.tableauDecision import def17
# from LTL.tools.tableauDecision import printGraph
# from LTL.tools.tableauDecision import makeGraph
from LTL.tools.toPnfObjects import toPnf


def tableauToGraph(edges):
    """ Print Graph in an file.
    edges<list>: List of tuple. Tuple are pathes of nodes. First place start
                 node, second place end node.
    """
    g = Digraph('G', filename='hello.gv')
    # durchgehen der Edges und diese printen.
    for e in edges:
        g.edge(e[0], e[1])
    g.view()


def calcEdgesDict(firstNode):
    """ Calculate a nodes and childnodes of them.

    return<tuple>: with two places -> first place start nodes
                                   -> second place list of nodes which follow
    """
    childList = []
    for x in firstNode.Pointers:
        try:
            if x.Pointers:
                result = calcEdgesDict(x)  # calcEdges(x)
                childList.append(result)
        except:
            childList.append(x.Name)
    dictEdges = (firstNode.Name, childList)
    return dictEdges


def calcEdges(liste):
    """ Calculate the list of states and prestates.
    """
    workListe = liste
    edges = []
    firstNode = liste[0]
    testList = []  # list to remember tuples which follow
    counter = 0
    while counter == 0:
        # go through tree and expans edges with start node and childnodes
        for x in workListe[1]:
            # case if element is a string, then it is a node without other
            # nodes and can inserted as path for edges.
            if type(x) == str:
                edges.append([firstNode, x])
            else:
                # another subtree, which is going be exploered
                testList.append(x)
                edges.append([firstNode, x[0]])
        if testList == []:  # cancel if tree finished
            counter = 1
            continue
        workListe = testList[0]
        firstNode = workListe[0]
        testList.pop(0)
    print(edges)
    return edges
