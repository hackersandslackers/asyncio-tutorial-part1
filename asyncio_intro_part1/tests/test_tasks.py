"""Test task creation."""
from asyncio import Task

import pytest

from asyncio_intro_part1.tasks import create_tasks


@pytest.mark.asyncio
async def test_create_tasks():
    """Test task creation."""
    task_list = await create_tasks(5)
    assert len(task_list) == 5
    assert isinstance(task_list, list)
    assert isinstance(task_list[0], Task)
