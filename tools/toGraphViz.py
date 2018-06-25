"""Author Stefan Strang - Uni Freiburg.


"""

from graphviz import Digraph


def toGraph(edges, goals, start, statesPrint):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    """
    g = Digraph('G', filename='hello.gv')
    # counter2 = 0
    for e in edges:
        g.edge(e[0], e[1])
        if e[1] in goals:
            g.node(e[1], shape='doublecircle')
        '''if e[1] not in statesPrint:
            g.node('%d' % (counter2), label='', shape='diamond')
            # TODO: Formel: g.edge('%d' % (counter2), e[1].pointFirst.getName())
            # g.edge('%d' % (counter2), e[1].pointSec.getName())
            counter2 += 2'''
    counter1 = 0
    for e in start:
        # Node one for start path.
        g.node('%d' % (counter1), shape='point')
        if e.pointFirst and e.pointSec:
            g.node('%d' % (counter1 + 1), label='', shape='diamond')
            g.edge('%d' % (counter1), '%d' % (counter1 + 1))
            g.edge('%d' % (counter1 + 1), e.pointFirst.getName())
            g.edge('%d' % (counter1 + 1), e.pointSec.getName())
        else:  # case for one literal status.
            g.edge('%d' % (counter1), e.getName())
        # TODO: einstellige Elemente.
        counter1 += 2
    g.view()


def calcEdges(dictionary):
    # states = len(dictionary)
    edges = []
    for i in dictionary:
        for j in dictionary[i]:
            tup = [i, j]
            edges.append(tup)
        '''for j in range(rows):
            tup = []
            if matrix[i + 1][j] == '1':
                tup.append(matrix[0][i])  # first place, start of path
                tup.append(matrix[0][j])  # path goes to
            if tup != []:  # if there exist a path, append to edges
                edges.append(tup)'''
    print(edges)
    return edges
