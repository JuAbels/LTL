"""Author Stefan Strang - Uni Freiburg.


"""

from graphviz import Digraph


def toGraph(nodes, edges, goals, start):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    """
    g = Digraph('G', filename='hello.gv')
    for e in edges:
        g.edge(e[0], e[1])
        if e[1] in goals:
            g.node(e[1], shape='doublecircle')
    for e in start:
        g.node('start', color='white')
        if e.Atom is None:
            # if e.getName() in g.node:
                # continue
            if e.pointSec is None:
                g.edge('start', e.pointFirst.getName())
            else:
                g.edge('start', e.pointFirst.getName())
                g.edge('start', e.pointSec.getName())
                # g.edge(node, e)
    g.view()


def calcEdges(matrix):
    lines, rows = matrix.shape
    edges = []
    for i in range(rows - 1):
        for j in range(rows):
            tup = []
            if matrix[i + 1][j] == '1':
                tup.append(matrix[0][i])  # first place, start of path
                tup.append(matrix[0][j])  # path goes to
            if tup != []:  # if there exist a path, append to edges
                edges.append(tup)
    return edges
