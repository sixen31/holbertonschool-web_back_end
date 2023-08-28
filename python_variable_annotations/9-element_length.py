#!/usr/bin/env python3

"""
This function to calculate the length of elements in an iterable.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements and returns the result as a list of tuple
    """
    return [(i, len(i)) for i in lst]
