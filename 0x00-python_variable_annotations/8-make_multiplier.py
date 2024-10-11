#!/usr/bin/env python3
'''Module for task 8'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by a multiplier'''
    return lambda d: d * multiplier
