#!/usr/bin/env python3
""" Python File """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of mixed numbers in a list """
    sum = 0
    for n in mxd_lst:
        sum += n
    return sum
