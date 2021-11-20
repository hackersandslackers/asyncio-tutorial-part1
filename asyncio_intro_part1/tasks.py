"""Create multiple tasks from a coroutine."""
import asyncio
from asyncio import Task
from typing import Coroutine, List


async def create_tasks(simple_coroutine: Coroutine) -> List[Task]:
    """
    Create asyncio tasks to be executed.

    :returns: List[Task]
    """
    task_list = []
    for i in range(5):
        task = asyncio.create_task(simple_coroutine(i, delay=i))
        task.set_name(f"Task Number {i}")
        task_list.append(task)
    return task_list
