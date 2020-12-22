"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    min_index = 0
    for index, number in enumerate(arr):
        if number < arr[min_index]:
            min_index = index
    return min_index


if __name__ == '__main__':
    print(min_search([4, 6, 10, 3, 5]))
