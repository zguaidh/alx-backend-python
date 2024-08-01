#!/usr/bin/env python3
'''multiply a float x by a multiplier'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiply a float x by a multiplier'''
    def multiplier_function(x: float) -> float:
        '''does the multiplication'''
        return x * multiplier
    return multiplier_function
