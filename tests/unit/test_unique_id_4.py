import pytest
import src.tasks.api as t2
import src.tasks.tasks_m as t1


@pytest.mark.xfail(t1.__version__ < '0.2.0',
                  reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers"""
    ret1 = t2.unique_id()
    ret2 = t2.unique_id()
    assert ret1 == ret2


@pytest.mark.xfail()
def test_unique_id_is_duck():
    """Demonstrate xfail"""
    uid = t2.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demonstrate xpass"""
    uid = t2.unique_id()
    assert uid != 'a duck'
