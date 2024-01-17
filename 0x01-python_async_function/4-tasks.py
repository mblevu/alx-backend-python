#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""
import asyncio
import random
from typing import List


async def task_wait_random(max_delay: int) -> int:
    """takes an integer max_delay and returns a asyncio.Task."""
    delay: int = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[int]:
    """alter wait_n into a new function task_wait_n"""
    delay_list: List[int] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay: int = await task
        delay_list.append(delay)
    return delay_list
