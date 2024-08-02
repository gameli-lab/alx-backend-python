#!/usr/bin/env python3

from typing import TypeVar, Dict, Optional

k = TypeVar('k')
v = TypeVar('v')

def safely_get_value(dct: Dict[k, v],  key: k, default: Optional[v] = None) ->Optional[v]:
    if key in dct:
        return dct[key]
    else:
        return default
