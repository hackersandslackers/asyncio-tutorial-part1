"""Create multiple tasks from a coroutine."""
import asyncio
from asyncio import Task
from typing import List

from asyncio_intro_part1.coroutines import simple_coroutine


async def create_tasks() -> List[Task]:
    """
    Create five asyncio tasks to be executed.

    :returns: List[Task]
    """
    task_list = []
    for i in range(5):
        task = asyncio.create_task(simple_coroutine(i))
        task.set_name(f"Task #{i}")
        task_list.append(task)
    return task_list
