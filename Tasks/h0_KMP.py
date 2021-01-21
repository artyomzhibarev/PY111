from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    # pi = _prefix_fun(substr)
    # j = 0
    # for i in range(len(inp_string)):
    #     if inp_string[i] == substr[j]:

    pi = [0] * len(prefix_str)  # префикс таблица
    j = 0  # граница префикса
    i = 1  # граница суффикса
    while i < len(prefix_str):
        if prefix_str[i] == prefix_str[j]:
            pi[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]
    return pi


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    pi_ = _prefix_fun(substr)
    j = 0
    for i in range(len(inp_string)):
        if inp_string[i] == substr[j]:
            j += 1
            if j == len(substr):
                return i - j + 1
            else:
                continue
        else:
            j = pi_[j - 1]
    return None
