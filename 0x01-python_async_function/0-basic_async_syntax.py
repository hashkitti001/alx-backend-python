#!/usr/bin/env python3
'''Task for module 0'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    An asynchronous coroutine that waits for a random number of seconds
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
