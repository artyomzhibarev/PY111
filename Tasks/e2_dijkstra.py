from typing import Hashable, Mapping, Union

import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    dict_ = {node: float('inf') for node in g.nodes}
    visited = {node: False for node in g.nodes}
    distances = {}
    dict_[starting_node] = 0
    while not all(visited.values()):
        node_min_weight = min(dict_, key=dict_.get)
        for node in g.neighbors(node_min_weight):
            if not visited[node]:
                if dict_[node] > g.adj[node_min_weight][node]['weight'] + dict_[node_min_weight]:
                    dict_[node] = g.adj[node_min_weight][node]['weight'] + dict_[node_min_weight]
        visited[node_min_weight] = True
        distances[node_min_weight] = dict_[node_min_weight]
        del dict_[node_min_weight]
    return distances


if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    # print(list(graph.neighbors('D')))
    # print(graph)
    # nx.draw(graph, with_labels=True, )
    # plt.show()
    print(dijkstra_algo(graph, 'A'))
