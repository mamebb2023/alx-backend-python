#!/usr/bin/env python3
""" Async Generator """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    """
    Loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        t = random.randint(0, 10)
        yield t
        await asyncio.sleep(1)
