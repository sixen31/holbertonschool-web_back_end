#!/usr/bin/env python3
"""
This module contains a function to create a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create multiplies a float by the given multiplier.
    """
    def multiplier_function(number: float) -> float:
        """
        Multiplies a float by the multiplier and returns the result.
        """
        return number * multiplier
    return multiplier_function
