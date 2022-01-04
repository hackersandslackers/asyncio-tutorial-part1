"""Tutorial demonstrating asyncio Coroutines and Tasks."""
import asyncio
from inspect import currentframe as current

from logger import LOGGER

from asyncio_intro_part1.coroutines import simple_coroutine
from asyncio_intro_part1.tasks import create_tasks
from asyncio_intro_part1.util import function_complete_log, function_start_log


async def init_script():
    """Script entry point."""
    await async_coroutines_example()  # Async code as Coroutines
    await async_tasks_example()  # Async code as Coroutines wrapped in Tasks


async def async_coroutines_example():
    """Run a function three times concurrently."""
    function_name = current().f_code.co_name
    start_time = await function_start_log(function_name)
    await asyncio.gather(
        simple_coroutine(1),
        simple_coroutine(2),
        simple_coroutine(3),
    )
    await function_complete_log(function_name, start_time)


async def async_tasks_example():
    """Create Tasks to wrap coroutines and inspect their properties."""
    function_name = current().f_code.co_name
    start_time = await function_start_log(function_name)
    task_list = await create_tasks(5)
    done, pending = await asyncio.wait(task_list)
    if done:
        LOGGER.success(f"{len(done)} tasks completed: {[task.get_name() for task in done]}.")
    if pending:
        LOGGER.warning(f"{len(done)} tasks pending: {[task.get_name() for task in pending]}.")
    await function_complete_log(function_name, start_time)
