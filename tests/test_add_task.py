import pytest
import os
from database import TaskDatabase

@pytest.fixture
def test_db():
    db_path = 'test_tasks.db'
    db = TaskDatabase(db_path)
    yield db
    if os.path.exists(db_path):
        os.remove(db_path)

def test_add_task_success(test_db):
    task_id = test_db.add_task('Test görevi')
    assert task_id > 0
    task = test_db.get_task(task_id)
    assert task is not None
    assert task[1] == 'Test görevi'
    assert task[2] == 0

def test_add_multiple_tasks(test_db):
    id1 = test_db.add_task('Görev 1')
    id2 = test_db.add_task('Görev 2')
    assert id2 > id1
    tasks = test_db.get_all_tasks()
    assert len(tasks) == 2
