from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    mid = 0
    start = 0
    end = len(arr)
    while start <= end:
        if elem not in arr:
            return None
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return mid


if __name__ == '__main__':
    test_ = 2, [1, 2, 2, 2]
    list_ = [324, 311, 56, 7, 12, 67, 55, 7, 787]
    print(binary_search(2, [1, 2, 2, 2]))
