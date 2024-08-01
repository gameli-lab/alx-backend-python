#!/usr/bin/env python3
'''
to_kv annotated method
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    to_kv method takes a string k and union int float
    returns a tuple of a str and int/float
    '''
    sqr = float(v * v)

    return (k, sqr)
