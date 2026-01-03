"""
The TodoList Class This class will be the main engine for managing all tasks.
File: todolist.py
Purpose: To manage the collection of Task objects and handle file operations.
Attributes:
_tasks (list): A list to hold all the Task objects. The underscore _ indicates it's intended for internal use.
Methods:
__init__(self): Constructor that initializes the _tasks list as empty.
add_task(self, description: str, due_date: str): Creates a new Task object and adds it to the _tasks list.
list_tasks(self): Iterates through the _tasks list and prints each task. It should print a message if the list is empty. For a non-empty list, it should print each task with a 1-based index number for the user.
Example output:
1. [ ] Buy groceries (Due: 2025-08-10)
2. [ ] Finish project report (Due: 2025-08-12)


mark_task_complete(self, task_index: int): Marks a task as complete based on its 1-based index from the list_tasks view. Remember to convert the user's 1-based index to a 0-based list index. Handle invalid indices.
delete_task(self, task_index: int): Deletes a task from the _tasks list based on its 1-based index. Handle invalid indices.
save_to_file(self, filepath: str): Saves the entire list of tasks to a file. It should convert each Task object to a dictionary using task.to_dict() and then use the json module to write the list of dictionaries to the specified file.
load_from_file(self, filepath: str): Loads tasks from a file. It should use a try...except FileNotFoundError block. If the file exists, it reads the JSON data, iterates through the list of dictionaries, and uses Task.from_dict() to create Task objects to populate the _tasks list.
"""

from __future__ import annotations
import json
from typing import List
from task import Task

class TodoList:
    def __init__(self):
        self._tasks: List[Task] = []

    def add_task(self, description: str, due_date: str) -> None:
        new_task = Task(description, due_date)
        self._tasks.append(new_task)
        print("Task added successfully.")

    def list_tasks(self) -> None:
        if not self._tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self._tasks, start=1):
            print(f"{index}. {task}")

    def mark_task_complete(self, task_index: int) -> None:
        if 1 <= task_index <= len(self._tasks):
            self._tasks[task_index - 1].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index: int) -> None:
        if 1 <= task_index <= len(self._tasks):
            del self._tasks[task_index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def save_to_file(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self._tasks], file, indent=2, ensure_ascii=False)
        print("Tasks saved to file.")

    def load_from_file(self, filepath: str) -> None:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
            self._tasks = [Task.from_dict(data) for data in tasks_data]
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print("Data file is corrupted or empty. Starting with an empty task list.")
            self._tasks = []

