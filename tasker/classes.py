import sqlite3
import os


class Task:
    def __init__(self, *args):
        self.id = args[0]
        self.title = args[1]

    def __str__(self):
        return f"{self.id} :: {self.title}"


class TaskManager:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database', 'tasks.db')
        self.db_connection = sqlite3.connect(self.db_path)
        self.cursor = self.db_connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY, title char(256))")
        self.db_connection.commit()

    def create(self, title):
        self.cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title, ))
        self.db_connection.commit()
        print("Task created")

    def list(self):
        tasks = (Task(*task) for task in self.cursor.execute("SELECT * FROM tasks").fetchall())
        for task in tasks:
            print(task)

    def remove(self, index):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (index, ))
        self.db_connection.commit()
        print("Task removed")
