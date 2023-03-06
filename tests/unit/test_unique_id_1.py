import pytest
import src.tasks.api as t2
import src.tasks.tasks_m as t1

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    t2.start_tasks_db(str(tmpdir), 'tiny')
    yield # this is where the testing happens
    # Teardown : stop db
    t2.stop_tasks_db()


@pytest.mark.skip(reason='misunderstod the API')
def test_unique_id0():
    """Calling unique_id() twice should return different number"""
    id_1 = t2.unique_id()
    id_2 = t2.unique_id()
    assert id_1 != id_2


def test_unique_id2():
    """Calling unique_id() twice should return different number"""
    ids = []
    ids.append(t2.add('one'))
    ids.append(t2.add('two'))
    ids.append(t2.add('three'))
    # grab a unique id
    uid = t2.unique_id()
    #make sure it isn't in the list of existing ids
    assert uid is not ids


@pytest.mark.skipif(t1.__version__ < '0.2.0',
                  reason='not supported until version 0.2.0')
def test_unique_id3():
    """Calling unique_id() twice should return different number"""
    id_1 = t2.unique_id()
    id_2 = t2.unique_id()
    assert id_1 == id_2
