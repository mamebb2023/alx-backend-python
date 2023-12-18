#!/usr/bin/env python3
""" Measure runtime """
import asyncio
import time
import typing

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """ Measures runtime """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
