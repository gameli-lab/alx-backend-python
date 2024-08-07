#!/usr/bin/env python3
'''
An async generator that uses the random module to generate numbers
'''
import asyncio
import random


async def async_generator() -> float:
    '''
    async_generator generates random integers between 0 and 10
    yields the results
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
