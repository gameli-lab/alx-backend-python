#!/usr/bin/env python3
'''
Asyncronous coroutine module
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    wait_random delays for a default of 10 secs
    returns a float
    '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
