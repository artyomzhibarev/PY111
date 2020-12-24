"""
Taylor series
"""
from itertools import count
from math import factorial, exp, sin, fabs
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    sum_ = 0
    delta = 0.0001
    for n in count(0, 1):
        current_value = (x ** n) / factorial(n)
        if current_value <= delta:
            return sum_
        else:
            sum_ += current_value


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    delta = 0.0001
    for n in count(0, 1):
        current_value = (-1) ** n * ((x ** (2 * n + 1)) / factorial(2 * n + 1))
        if fabs(current_value) <= delta:
            return sum_
        else:
            sum_ += current_value


if __name__ == '__main__':
    # for value in range(10):
    #     print(ex(value))
    #     print(exp(value))
    #     print('--------')

    print(sinx(1.55433))
    print(sin(1.55433))
