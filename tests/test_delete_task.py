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

def test_delete_task_success(test_db):
    task_id = test_db.add_task('Silinecek görev')
    result = test_db.delete_task(task_id)
    assert result is True
    task = test_db.get_task(task_id)
    assert task is None

def test_delete_nonexistent_task(test_db):
    result = test_db.delete_task(9999)
    assert result is False
