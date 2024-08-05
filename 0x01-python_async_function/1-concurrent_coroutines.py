#!/usr/bin/env python3
'''Creates an async routine wait_n that does wait_random n times and returns the list of delays'''
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns the list of delays in ascending order'''
    coroutines = []
    for i in range(n):
        coroutines.append(wait_random(max_delay))
        delays = await asyncio.gather(coroutines[i])
    return sorted(delays)

