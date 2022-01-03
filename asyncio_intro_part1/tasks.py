"""Create multiple tasks from a Coroutine."""
import asyncio
from asyncio import Task
from typing import List

from logger import LOGGER

from asyncio_intro_part1.coroutines import simple_coroutine


async def create_tasks(num_tasks: int) -> List[Task]:
    """
    Create n number of asyncio tasks to be executed.

    :param int num_tasks: Number of tasks to create.

    :returns: List[Task]
    """
    task_list = []
    LOGGER.info(f"Creating {num_tasks} tasks to be executed...")
    for i in range(num_tasks):
        task = asyncio.create_task(simple_coroutine(i), name=f"Task #{i}")
        task_list.append(task)
        LOGGER.info(f"Created Task: {task}")
    return task_list
