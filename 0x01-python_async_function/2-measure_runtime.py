#!/usr/bin/env python3
'''
This module measure the total time of execution
'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    measure_time calculates the execution time for wait_n
    returns the time taken to finish execution
    '''
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
