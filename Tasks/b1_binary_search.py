from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == elem:
            while arr[mid - 1] == elem:
                mid -= 1
            return mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1

    return None
