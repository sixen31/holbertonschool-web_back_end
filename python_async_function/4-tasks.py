#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns a list of delays in ascending order
    """
    delays = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        await task
        delays.append(task.result())
    delays.sort()
    return delays
