#!/usr/bin/env python3
'''create a coroutine called async_comprehension that collects
10 random numbers from async_generator then returns these numbers'''


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''asynchronous return the numbers from async_generator'''
    result = []
    async for num in async_generator():
        result.append(num)
    return result
