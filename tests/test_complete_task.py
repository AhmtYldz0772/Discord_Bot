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

def test_complete_task_success(test_db):
    task_id = test_db.add_task('Tamamlanacak görev')
    result = test_db.complete_task(task_id)
    assert result is True
    task = test_db.get_task(task_id)
    assert task[2] == 1

def test_complete_nonexistent_task(test_db):
    result = test_db.complete_task(9999)
    assert result is False

def test_complete_already_completed_task(test_db):
    task_id = test_db.add_task('Görev')
    test_db.complete_task(task_id)
    result = test_db.complete_task(task_id)
    assert result is True
    task = test_db.get_task(task_id)
    assert task[2] == 1
