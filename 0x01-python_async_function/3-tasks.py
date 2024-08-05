#!/usr/bin/env python3
'''Creates a task_wait_random function that takes
an integer max_delay and returns an asyncio.task'''


import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Returns an asyncio.task'''
    return asyncio.create_task(wait_random(max_delay))
