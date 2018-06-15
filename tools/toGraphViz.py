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


def calcEdges(matrix):
    lines, rows = matrix.shape
    edges = []
    for i in range(rows - 1):
        for j in range(rows):
            tup = []
            if matrix[i + 1][j] == '1':
                tup.append(matrix[0][i])
                tup.append(matrix[0][j])
        if tup != []:
            edges.append(tup)
    return edges
