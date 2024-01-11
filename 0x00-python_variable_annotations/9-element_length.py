#!/usr/bin/env python3
"""annotating function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of tuples"""
    return [(i, len(i)) for i in lst]
