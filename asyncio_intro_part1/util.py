"""Helpers for logging the invocation & execution time of functions."""
from time import perf_counter as timer
from time import sleep

from logger import LOGGER


async def function_start_log(function_name: str) -> timer:
    """
    Announces the start of a function & returns the start time of execution.

    :param str function_name: Name of function which is about to execute.

    :returns: timer
    """
    LOGGER.warning(f"About to run function `{function_name}`...")
    return timer()


async def function_complete_log(function_name: str, start_time: timer):
    """
    Announces the completion of a function & its execution time.

    :param str function_name: Name of function which has completed execution.
    :param timer start_time: Time at which the function began.
    """
    LOGGER.success(
        f"Executed {function_name} in {timer() - start_time:0.2f} seconds. \n----------------------------------------------------------------"
    )
    sleep(2)
