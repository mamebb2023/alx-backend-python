#!/usr/bin/env python3
"""Basic asyncio syntax"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Takes in an integer argument named wait_random that
    waits for a random delay between 0
    and max_delay seconds and eventually returns it.
    """
    rand_delay = uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
