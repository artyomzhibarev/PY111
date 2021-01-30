from typing import Hashable, List

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path = []
    visited = {node: False for node in g.nodes}
    stack = [start_node]
    visited[start_node] = True
    while stack:
        current_node = stack.pop()
        path.append(current_node)
        for node in g.neighbors(current_node):
            if not visited[node]:
                stack.append(node)
                visited[node] = True

    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    # nx.draw(graph, with_labels=True)
    # plt.show()
    print(dfs(graph, 'A'))
