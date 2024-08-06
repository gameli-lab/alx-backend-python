#!/usr/bin/env python3
'''
Concurent coroutines module
'''

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random



async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n runs the imported function n times st a specified deley
    tasks takes list of tasks created by wait_random n times
    delays is a list of time taken to wait for subsequent tasks to be created
    sorted_delays sorts the delays as to which one was created first
    returns sorted delay
    '''
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []
    for task in tasks:
        delay = await task
        delays.append(delay)

    sorted_delay = []
    for delay in delays:
        inserted = False
        for i in range(len(sorted_delay)):
            sorted_delay.insert(i, delay)
            inserted = True
            break
        if not inserted:
            sorted_delay.append(delay)

    return sorted_delay
