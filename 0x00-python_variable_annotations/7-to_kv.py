#!/usr/bin/env python3
'''Module for task 7'''
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple containing a number and it's square'''
    return (k, float(v ** 2))
