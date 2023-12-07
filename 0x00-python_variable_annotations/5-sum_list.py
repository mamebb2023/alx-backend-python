#!/usr/bin/env pytho3
""" Python file """


def sum_list(input_list: list[float]) -> float:
    """ Sums up the floats in the list """
    sum = 0
    for i in input_list:
        sum += i

    return sum
