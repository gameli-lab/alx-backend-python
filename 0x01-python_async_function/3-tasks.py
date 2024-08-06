#!/usr/bin/env python3 
'''
This module uses sencronous function to create async func
'''
import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asyncio Task to run wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio Task running the wait_random coroutine.
    '''
    return asyncio.create_task(wait_random(max_delay))
