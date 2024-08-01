#!/usr/bin/env python3
'''
a multiplier annotated module
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    make_multiplier is a method that takes multiplier as argument.
    It calls multiplication to perform a multiplication operation
    and returns the result.
    returns the multiplication method
    '''
    def multiplication(n: float) -> float:
        return n * multiplier
    return multiplication
