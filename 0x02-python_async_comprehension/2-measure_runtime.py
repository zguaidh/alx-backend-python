#!/usr/bin/env python3
'''create a coroutine called measure_runtime that will run async_comprehension
4 times in parallel and returns the total runtime'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''return the total run time of 4 async_comprehension in parallel'''
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
