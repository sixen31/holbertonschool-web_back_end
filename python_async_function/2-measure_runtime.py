#!/usr/bin/env python3
"""
function measure the runtime of wait_n and calculate the average time
"""


import time
import asyncio
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int, fn: Callable = wait_n) -> float:
    """
execution time for wait_n(n, max_delay) and returns average time per coroutine
    """
    start_time = time.time()
    asyncio.run(fn(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_coroutine = total_time / n
    return average_time_per_coroutine
