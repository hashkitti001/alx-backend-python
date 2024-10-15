#!/usr/bin/env python3
'''Module for task 2'''
import asyncio
import time
from importlib import import_module as require

async_comprehension = require('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the runtime of executing Task 1's routine four times'''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
