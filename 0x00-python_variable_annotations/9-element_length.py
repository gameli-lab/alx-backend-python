#!/usr/bin/env python3
'''
I am supposed to annotate the below function’s parameters and return
values with the appropriate types
'''
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    element length takes a list as argument
    returns the length of the list
    '''
    return [(i, len(i)) for i in lst]
