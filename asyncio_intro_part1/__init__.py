"""Tutorial demonstrating asyncio Coroutines and Tasks."""
import asyncio
from inspect import currentframe as current

from logger import LOGGER

from asyncio_intro_part1.coroutines import simple_coroutine
from asyncio_intro_part1.tasks import create_tasks
from asyncio_intro_part1.util import function_start_log, function_complete_log


async def init_script():
    """Script entry point."""
    await async_coroutines_example()  # Async code as Coroutines
    await async_tasks_example()  # Async code as Coroutines wrapped in Tasks


async def async_coroutines_example():
    """Run a function three times concurrently."""
    start_time = await function_start_log(current().f_code.co_name)
    await asyncio.gather(
        simple_coroutine(1),
        simple_coroutine(2),
        simple_coroutine(3),
    )
    await function_complete_log(current().f_code.co_name, start_time)


async def async_tasks_example():
    """Create Tasks to wrap coroutines and inspect their properties."""
    start_time = await function_start_log(current().f_code.co_name)
    tasks = await create_tasks()
    LOGGER.info(f"Created {len(tasks)} tasks about to be executed:")
    for task in tasks:
        LOGGER.info(task)
    tasks = await asyncio.gather(*tasks)
    LOGGER.success(f"Remaining tasks: {[task for task in tasks if task is not None]}")
    await function_complete_log(current().f_code.co_name, start_time)
