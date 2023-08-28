#!/usr/bin/env python3
"""
This module to create a tuple from a string and the square of an int/float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates string and the square of an int/float, returning the result.
    """
    return (k, v ** 2)
