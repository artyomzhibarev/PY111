from collections import deque
from typing import Hashable, List

import matplotlib.pyplot as plt
import networkx as nx


def drow_graph(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.savefig('Graph.png')
    plt.show()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    # drow_graph(g)

    visited = {node: False for node in g.nodes}  # словарь непосещенных вершин
    wait_nodes = deque()  # подоженные

    wait_nodes.append(start_node)
    visited[start_node] = True
    path = []

    while wait_nodes:
        current_node = wait_nodes.popleft()
        path.append(current_node)
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                wait_nodes.append(neighbor)
                visited[neighbor] = True

    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    # print(graph.nodes)
    # print(graph['A'])
    # print(list(graph.neighbors('A')))
    # drow_graph(graph)
    print(bfs(graph, 'A'))
