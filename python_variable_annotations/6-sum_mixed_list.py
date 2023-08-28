#!/usr/bin/env python3
"""
This modul calculate the sum of a list of mixed integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates list of mixed integers and floats and returns the result.
    """
    return sum(mxd_lst)
