"""Test the t1.add() Api function"""
import pytest
import src.tasks.api as t1
from src.tasks.api import Task


def test_add_1():
    """Tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = t1.add(task)
    f_from_db = t1.get(task_id)
    # everything but the id should be the same
    assert equivalent(f_from_db, task)


def equivalent(a1, a2):
    """Check two tasks for equivalence"""
    # Compare everything but the id field
    return ((a1.summary == a2.summary) and
            (a1.owner == a2.owner) and
            (a1.done == a2.done))


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    """Connect to db before testing, dsconnect after"""
    t1.start_tasks_db(str(tmpdir), 'tiny')
    yield
    t1.stop_tasks_db()