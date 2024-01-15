#!/usr/bin/env python3
"""measures the total execution runtime"""
import asyncio
import random
from typing import List
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """measures the total execution runtime"""
    async def run_wait_n():
        await wait_n(n, max_delay)

    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(run_wait_n())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
