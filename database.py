import sqlite3
import os
from datetime import datetime

class TaskDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def add_task(self, description):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (description, created_at) VALUES (?, ?)',
                      (description, datetime.now().isoformat()))
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return task_id
    
    def delete_task(self, task_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted
    
    def get_all_tasks(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, description, completed FROM tasks ORDER BY id')
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    
    def complete_task(self, task_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        updated = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return updated
    
    def get_task(self, task_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, description, completed FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        conn.close()
        return task
