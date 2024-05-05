#!/usr/bin/env python3
"""Async"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Runs an async function and returns results"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - s

    return total/n
