#!/usr/bin/env python3
""" Python Type Annotation """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuble of k and square of v """
    return (k, v*v)
