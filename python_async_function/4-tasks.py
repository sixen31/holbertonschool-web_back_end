#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns a list of delays in ascending order
    """
    delays = [await task_wait_random(max_delay) for i in range(n)]
    delays.sort()
    return delays
