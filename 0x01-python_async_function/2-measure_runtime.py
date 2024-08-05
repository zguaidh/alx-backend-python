#!/usr/bin/env python3
'''Creates a measure_time function that measures the total execution time for wait_n and returns the average time'''


import asyncio
import time
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the average time'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

