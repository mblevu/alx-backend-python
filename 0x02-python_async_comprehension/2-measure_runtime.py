#!/usr/bin/env python3
"""a coroutine that should measure the total runtime and return it"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The coroutine will execute async_comprehension four times in
    parallel using asyncio.gather."""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    total_runtime = end - start
    return total_runtime
