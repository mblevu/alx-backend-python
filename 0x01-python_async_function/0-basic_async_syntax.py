#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random: asynchronous coroutine that takes in an integer argument
    Args:
        max_delay (int, optional): [maximum value of delay]. Defaults to 10.
    Returns:
        float: [random number between 0 and max_delay]
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
