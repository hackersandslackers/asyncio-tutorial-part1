"""Script entry point."""
import asyncio
import time

from asyncio_intro_tutorial import init_script

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(init_script(start_time))
