#!/usr/bin/env python3
'''returns a tuple of stringe k and the square of int v'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple of stringe k and the square of int v'''
    return (k, float(v ** 2))
