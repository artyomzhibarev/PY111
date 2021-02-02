from collections import deque
from typing import Hashable, Mapping, Union

import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    dict_ = {node: float('inf') for node in g.nodes}  # словарь, заполненный inf для всех node
    visited = {node: False for node in g.nodes}  # словарь непосещенных вершин
    compare_nodes = dict()  # словарь для промежуточного вычисления минимальньго веса ребер
    dict_[starting_node] = 0  # вес начальной точки = 0
    deque_nodes = deque()  # очередь минимальных величн
    visited[starting_node] = True  # по условию задачи стартовая нода посещенная
    for node in g.neighbors(starting_node):  # для соседей стартовой ноды ищем соседей с мин весом
        compare_nodes[node] = g.adj[starting_node][node]['weight']  # помещаем их этот словарь
        dict_[node] = g.adj[starting_node][node]['weight']  # помещам в "общий" словарь с весами всех нод
    node_min_weight = min(g.neighbors(starting_node), key=compare_nodes.get)  # находим мин ноду и стартуем от неё
    compare_nodes.clear()  # очищаем промежуточный словарь

    deque_nodes.append(node_min_weight)  # добавляем ноду с мин весом, найденной из предыдущ. шага
    current_node = deque_nodes.popleft()  # чтобы "завязаться" на ноде, получаем ее виде сылки на этот объет при помощи поплефта
    for node in g.neighbors(current_node):  # идем по её соседям
        if not visited[node]: # если сосед этой ноды не посещен...
            compare_nodes[node] = g.adj[current_node][node]['weight'] # добавляем его в словарь для сравнений
    node_min_weight = min(g.neighbors(current_node), key=compare_nodes.get) # нашли соседа с мин весом для этой ноды
    if compare_nodes[node_min_weight] + dict_[node_min_weight] < dict_[node_min_weight]: # если вес её родителя + вес её самой < меньше чем то, что находится в "общем" словаре,
        dict_[node] = compare_nodes[node_min_weight] + dict_[node_min_weight] # меняем на новое значение = найден новый путь до ноды


# вот тут я не понимаю что делать...


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
    # graph.add_nodes_from('SABE')
    # graph.add_weighted_edges_from([
    #     ("S", "B", 2),
    #     ("S", "A", 6),
    #     ("B", "A", 3),
    #     ("A", "E", 1),
    #     ("B", "E", 5),
    #     ("S", "D", 1), ])
    # print(graph.adj['S']['B']['weight'])
    # print(graph.adj.get('B'))
    # print(list(graph.neighbors('D')))
    # nx.draw(graph, with_labels=True, )
    # plt.show()
    print(dijkstra_algo(graph, 'A'))
