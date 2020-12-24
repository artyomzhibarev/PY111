"""
Priority Queue

Queue priorities are from 0 to 10
"""
import heapq
from typing import Any

my_priority_queue = []  # начало слева, конец очереди справа


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param priority:
    :param elem: element to be added
    :return: Nothing
    """
    heapq.heappush(my_priority_queue, (priority, elem)[1])  # (priority, elem)[1] == elem


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    return None if not my_priority_queue else heapq.heappop(my_priority_queue)
    # по умолчанию heappop возвращает элемент с наименьшим приоритетом (0), по этому тест не проходит


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param priority:
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    return None if ind >= len(my_priority_queue) else my_priority_queue[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_priority_queue.clear()
    return None


if __name__ == '__main__':
    enqueue('dog', 1)
    enqueue('cat', )
    enqueue('fish', 3)
    enqueue('lobster', 8)
    enqueue('human', 5)
    # print(my_priority_queue)

    while my_priority_queue:
        print(my_priority_queue)
        next_item = dequeue()
        print(next_item)

    # print(my_priority_queue)
    # dequeue()
    # print(my_priority_queue)
    # dequeue()
    # print(my_priority_queue)
    # dequeue()
    # print(my_priority_queue)
    # dequeue()
    # print(my_priority_queue)
