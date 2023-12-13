#!/usr/bin/env python3
""" Task 4 """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Takes in 2 int arguments (in this order): n and max_delay
    Spawns wait_random n times with the specified max_delay
    """
    delays_n = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay_n for delay_n in asyncio.as_completed(delays_n)]
