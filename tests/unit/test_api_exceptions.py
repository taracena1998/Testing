import pytest
import src.tasks.api as t1
import src.tasks.tasks_m as t2

class TestUpdate():
    """Test expcted exceptions with tasks.update()."""
    def test_bad_id(self):
        """A non int id should raise an exception."""
        with pytest.raises(TypeError):
            t1.update(task_id={'dict instead': 1},
                      task=t2.Task())
    def test_bad_task(self):
        """A non Task should raise an exception"""
        with pytest.raises(TypeError):
            t1.update(task_id=1, task='not a tas')


def test_add_raises():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        t1.add(task= 'not a task object')



def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo:
        t1.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "'db_type must be a 'tiny' or 'mongo'"

@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError) as e:
        t1.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        t1.get(task_id='123')