#!/usr/bin/env python3
"""a coroutine that takes no arugmensts"""
import asyncio
import random


async def async_generator():
    """loop 10 times each async wait 1 second then
    yield random number btn 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
