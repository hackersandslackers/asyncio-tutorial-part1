"""Tutorial demonstrating asyncio coroutines and tasks."""
import asyncio
from inspect import currentframe as current
from time import perf_counter as timer
from time import sleep

from logger import LOGGER

from asyncio_intro_part1.coroutines import simple_coroutine
from asyncio_intro_part1.tasks import create_tasks


async def init_script():
    """Script entry point."""
    await async_gather_example()
    sleep(2)
    await async_tasks_example()


async def async_gather_example():
    """Run a function three times concurrently."""
    start_time = timer()
    await asyncio.gather(
        simple_coroutine(1),
        simple_coroutine(2),
        simple_coroutine(3),
    )
    LOGGER.info(
        f"Executed {current().f_code.co_name} in {timer() - start_time:0.2f} seconds."
    )
    LOGGER.info("----------------------------------------------------------------")


async def async_tasks_example():
    """Create and inspect tasks to wrap simple functions."""
    tasks = await create_tasks()
    LOGGER.info(f"Created {len(tasks)} tasks about to be executed:")
    for task in tasks:
        LOGGER.info(task)
    tasks = await asyncio.gather(*tasks)
    LOGGER.info(f"Remaining tasks: {tasks}")
