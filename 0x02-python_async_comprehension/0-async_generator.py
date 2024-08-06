#!/usr/bin/env python3
'''creates a coroutine called async_generator that yields a random number
between 0 and 10 with a 1 second delay'''


import asyncio
import random
from typing import AsyncGenerator


async def async_generator():
    '''yields a random number with a 1 second delay'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
