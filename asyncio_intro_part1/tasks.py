"""Create multiple tasks from a coroutine."""
import asyncio
from asyncio import Task
from random import randint
from typing import List

from asyncio_intro_part1.coroutines import simple_coroutine


async def create_tasks() -> List[Task]:
    """
    Create asyncio tasks to be executed.

    :returns: List[Task]
    """
    task_list = []
    for i in range(5):
        duration = randint(1, 5)
        task = asyncio.create_task(simple_coroutine(i, delay=duration))
        task.set_name(f"Task #{i} (Duration {duration})")
        task_list.append(task)
    return task_list
