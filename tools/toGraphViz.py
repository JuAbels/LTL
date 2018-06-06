"""Author Stefan Strang - Uni Freiburg.


"""

from graphviz import Digraph


def toGraph(nodes, edges):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    """
    g = Digraph('G', filename='hello.gv')
    for e in edges:
        g.edge(e[0], e[1])
    g.view()
