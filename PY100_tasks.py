from collections import deque
from random import randint
from itertools import cycle

import networkx as nx

"""1. Оценить асимптотическую сложность приведенного ниже алгоритма:"""


def task1():
    pass
    # a = len(arr) - 1   #O(1)
    # out = list()       #O(1)
    # while a > 0:       #O(len(a)) ~ #O(1)
    #     out.append(arr[a]) #O(1)
    #     a = a // 1.7       #O(1)
    # out.merge_sort()      #O(nlogn)


"""
2. Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась,
вылетает. Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""


def task2(N, K): # не смог
    man = [i for i in range(N)]
    for i in range(K):
        man[K - N] = 0
    print(man)
    for j in range(len(man)):
        if man[j] != 0:
            return j


"""
3. Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
"""


def task3(g):
    # nx.draw(g, with_labels=True)
    # plt.show()

    deque_nodes = deque()
    visited = {node: False for node in g.nodes}
    component = 0
    for item in visited:
        if not visited[item]:
            deque_nodes.append(item)
            while deque_nodes:
                current_node = deque_nodes.popleft()
                for node in g.neighbors(current_node):
                    if not visited[node]:
                        deque_nodes.append(node)
                        visited[node] = True
            component += 1

    return component


"""
4. Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
(все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и
вывести этот путь.
"""




def task4():
    list_of_values = [
        [2, 5, 6],
        [7, 1, 9],
        [6, 4, 2]
    ]
    path = []
    cost = list_of_values.copy()
    for j in range(1, len(cost[0])):
        cost[0][j] += cost[0][j - 1]
    # print(cost[0])

    for i in range(1, len(cost[0])):
        cost[i][0] += cost[i - 1][0]
    # print([row[0] for row in cost])

    for i in range(1, len(cost)):
        for j in range(1, len(cost)):
            cost[i][j] += min(cost[i][j - 1], cost[i - 1][j])
            # if cost[i][i-j] <=cost[i-1][j] and (i, j - 1) != coords[-1]
    return cost[2][2]


"""
Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк 
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т,
в четвертой – снова А). Для входного списка из N строк одинаковой длины построить консенсус-строку.
"""


def task5():
    list_strings = ['ATTA', 'ACTA', 'AGCA', 'ACAK']
    list_ = []
    dict_ = dict()
    for j in range(len(list_strings)):
        for i in range(len(list_strings)):
            for char in list_strings[i][j]:
                if char in dict_:
                    dict_[char] += 1
                else:
                    dict_[char] = 1
        list_.append(max(dict_, key=dict_.get))
        dict_.clear()
    return ''.join(list_)



"""
6. Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
(час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
(т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
"""


def task6():
    times_ = [(0, 1), (5, 6), (3, 4), (1, 2)]
    times = times_.copy()
    s = []
    times_sorted = sorted(times, key=lambda x: x[1])
    print(times_sorted)
    # for index, item in range(len(times_sorted)):
    #     s.append(item[index][1] - item[index+1][0])
    for i in range(len(times_sorted) + 1):
        print(times_sorted[i][1] - times_sorted[i + 1][0])
    print(s)


"""
7. Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""


def task7(list_, min_, max_):
    c = [0 for i in range(min_, max_ + 1)]
    for number in list_:
        c[number - min_] += 1
    list_.clear()
    for i in range(len(c)):
        list_ += [i + min_] * c[i]
    return list_


if __name__ == '__main__':
    # graph = nx.Graph()
    # graph.add_nodes_from("ABCDEFG")
    # graph.add_edges_from([
    #     ('A', 'B'),
    #     ('B', 'C'),
    #     ('C', 'D'),
    #     ('F', 'G'),
    # ])
    # print(task3(graph))
    # print(task4())
    # print(task6())
    print(task5())
    # print(task7([randint(13, 25) for i in range(10)], 13, 25))
