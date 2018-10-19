"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

File to draw Graph of Semantic Tableau.

"""

from graphviz import Digraph


def tableauToGraph(edges):
    """ Print Graph in an file.
    edges<list>: List of tuple. Tuple are pathes of nodes. First place start
                 node, second place end node.
    """
    g = Digraph('G', filename='tableauDecisionGrafik')
    # Go through all edges and print them.
    for e in edges:
        g.edge(e[0], e[1])
    g.view()


def calcEdgesDict(firstNode):
    """ Calculate a nodes and childnodes of them.

    return<tuple>: with two places -> first place start nodes
                                   -> second place list of nodes which follow
    """
    childList = []  # list of the nodes which follow
    for x in firstNode.Pointers:
        try:  # if node has a child call child first
            if x.Pointers:
                result = calcEdgesDict(x)
                childList.append(result)
        except:  # insert node on that no other node follows.
            childList.append(x.Name)
    return (firstNode.Name, childList)


def calcEdges(liste):
    """ Calculate the list of states and prestates. """
    workListe = liste     # list of actual subtree
    edges = []            # insert all edges
    firstNode = liste[0]  # first node of an edge
    testList = []         # list to remember tuples which follow
    counter = 0           # counter to end loop
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
    return edges
