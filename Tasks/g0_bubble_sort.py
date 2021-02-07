from random import randint
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    flag = True
    iterations = 0
    while flag:
        flag = False
        for i in range(len(container) - iterations - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                flag = True
    iterations += 1

    return container


if __name__ == '__main__':
    print(sort([randint(-10, 10) for i in range(10)]))
