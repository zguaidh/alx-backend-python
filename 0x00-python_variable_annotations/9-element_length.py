#!/usr/bin/env python3
'''the annotated function'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return the lenght of a list lst'''
    return [(i, len(i)) for i in lst]
