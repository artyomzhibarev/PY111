"""
My little Queue
"""
from typing import Any

my_queue = []  # начало слева, конец очереди справа


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return None if not my_queue else my_queue.pop(0)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None
