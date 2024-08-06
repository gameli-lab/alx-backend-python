#!/usr/bin/env python3
'''
This module takes a previously defined method and alter it
'''
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n runs the imported function n times st a specified deley
    tasks takes list of tasks created by wait_random n times
    delays is a list of time taken to wait for subsequent tasks to be created
    sorted_delays sorts the delays as to which one was created first
    returns sorted delay
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
