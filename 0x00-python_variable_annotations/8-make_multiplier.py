#!/usr/bin/env python3
""" Callable returns """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function using callable """
    return lambda x: x * multiplier
