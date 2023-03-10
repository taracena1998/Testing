"""Use the Task type to show test failures"""

from src.tasks.tasks_m import Task

def test_task_equality():
    """Different tasks should nod be equal."""
    t1 = Task('sit here', 'brian')
    t2 = Task('do something', 'okken')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    t1_dict = Task('make sandwich', 'okken')._asdict()
    t2_dict = Task('make sandwich', 'okkem')._asdict()
    assert  t1_dict == t2_dict
