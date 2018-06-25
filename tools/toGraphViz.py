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
    counter = 0
    startElements = []
    for e in start:
        if e.Atom is None:
            if e.pointSec is None and e.pointFirst.getName() not in \
               startElements:
                startElements.append(e.pointFirst.getName())
            else:
                if e.pointFirst.getName() in startElements:
                    if e.pointSec.getName() not in startElements:
                        startElements.append(e.pointSec.getName())
                    else:
                        continue
                elif e.pointSec.getName() in startElements:
                    if e.pointFirst.getName() not in startElements:
                        startElements.append(e.pointFirst.getName())
                    else:
                        continue
                else:
                    startElements.append(e.pointFirst.getName())
                    startElements.append(e.pointSec.getName())
    print(startElements)
    for e in startElements:
        # g.node('start', color='white')
        g.node('%d' % (counter), shape='point')
        g.edge('%d' % (counter), e)
        counter += 1
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
