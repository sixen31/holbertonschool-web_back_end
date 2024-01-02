#!/usr/bin/env python3
"""
This asynchronous routine that spawns multiple wait_random coroutines.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns multiple wait_random coroutines and returns a list of their delays
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
