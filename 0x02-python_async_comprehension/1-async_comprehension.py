#!/usr/bin/env python3
'''create a coroutine called async_comprehension that collects
10 random numbers from async_generator then returns these numbers'''


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''asynchronous return the numbers from async_generator'''
    num = []
    async for num in async_generator():
        num.append(num)
    return num
