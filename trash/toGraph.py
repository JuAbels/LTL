"""Author Stefan Strang - Uni Freiburg.
Installation with:

pip conda install pip
pip install graphviz

Todo:
installiere anaconda um graphviz richtig installieren
und nutzen zu können

"""

import graphviz as graph


def toGraph(nodes, edges):
    """Simplify to render the automat.

    Input: list of nodes and edges
           Format nodes: ["A", "B", "C"]
           Format edges: [["A","B"],["B","C"]]
    Output: Nothing - prints the graph

    """
    """g1 = graph.Digraph(format="svg")
    for(n in nodes):
        g1.node(n)
    for(e in edges):
        g1.edge(e[0], e[1])
    g1.render('img/g1')
    """
    print(nodes)
    print(edges)
        
