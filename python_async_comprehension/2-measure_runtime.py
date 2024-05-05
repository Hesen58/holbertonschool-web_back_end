#!/usr/bin/env python3
"""Async functions"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Collects 10 numbers"""
    asyncs = [async_comprehension() for i in range(0, 4)]
    s = time.perf_counter()
    await asyncio.gather(*asyncs)
    total = time.perf_counter() - s
    return total
