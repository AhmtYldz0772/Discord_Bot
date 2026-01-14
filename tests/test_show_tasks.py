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

def test_show_empty_tasks(test_db):
    tasks = test_db.get_all_tasks()
    assert tasks == []

def test_show_tasks_with_data(test_db):
    test_db.add_task('Görev 1')
    test_db.add_task('Görev 2')
    tasks = test_db.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0][1] == 'Görev 1'
    assert tasks[1][1] == 'Görev 2'
