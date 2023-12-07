#!/usr/bin/env python3
""" Python file """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums up the floats in the list """
    sum = 0
    for i in input_list:
        sum += i

    return sum
