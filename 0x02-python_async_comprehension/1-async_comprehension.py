#!/usr/bin/env python3
'''Module for task 1'''
from importlib import import_module as require
from typing import List


async_generator = require('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns a list of 10 numbers from a 10 number generator'''
    result = [zahl async for zahl in async_generator()]
    return result
