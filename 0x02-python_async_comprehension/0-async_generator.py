#!/usr/bin/env python3
'''creates a coroutine called async_generator that yields a random number
between 0 and 10 with a 1 second delay'''


import asyncio
import random


async def async_generator() -> float:
    '''yields a random number with a 1 second delay'''
    num = []
    for i in range(10):
        await asyncio.sleep(1)
        num.append(random.uniform(0, 10))
    return num
