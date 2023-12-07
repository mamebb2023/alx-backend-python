#!/usr/bin/env python3
""" Python File """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return an array of tuples """
    return [(i, len(i)) for i in lst]
