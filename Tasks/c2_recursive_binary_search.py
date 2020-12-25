from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    def binary_search_recursive(left: int, right: int):
        if left > right:
            return None
        mid = left + (right - left) // 2
        if arr[mid] == elem:
            while arr[mid - 1] == elem:
                mid -= 1
            return mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1

        return binary_search_recursive(left, right)

    return binary_search_recursive(0, len(arr) - 1)
