#!/usr/bin/env python3
'''Creates a function task_wait_n that uses task_wait_random
to return a list of delays in ascending order'''


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''returns a list of delays'''
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
