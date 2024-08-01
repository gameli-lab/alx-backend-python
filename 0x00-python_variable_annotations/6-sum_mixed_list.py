#!/usr/bin/env python3
'''
mixed list sumation method module
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum_mixed_list method that takes mxd_lst of int and float as argument
    returns their sum as float
    '''
    return sum(float(item) for item in mxd_lst)
