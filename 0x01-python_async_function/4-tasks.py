#!/usr/bin/env python3
import asyncio
import random
from typing import List


async def task_wait_random(max_delay: int) -> int:
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[int]:
    delay_list = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)
    return delay_list
