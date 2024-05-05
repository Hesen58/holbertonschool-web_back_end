#!/usr/bin/env python3
"""Async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs an async function n times and returns list of results"""
    waits = [wait_random(max_delay) for i in range(0, n)]
    delays = []
    for i in asyncio.as_completed(waits):
        delay = await i
        delays.append(delay)

    return delays
