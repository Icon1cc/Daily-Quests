"""
File: task.py
Purpose: To represent a single task with all its properties.
Attributes:
description (str): The text of the task (e.g., "Buy groceries").
due_date (str): The date the task is due (e.g., "2025-08-10").
status (str): The current state of the task. Should default to "Pending".
Methods:
__init__(self, description: str, due_date: str): Constructor to initialize a new task. The status should be set to "Pending" automatically.
__str__(self) -> str: Returns a user-friendly string representation. A checkbox [ ] or [x] should indicate the status.
Example output: "[ ] Buy groceries (Due: 2025-08-10)"
mark_complete(self): Changes the status of the task from "Pending" to "Completed".
to_dict(self) -> dict: (Crucial for saving) Returns a dictionary representation of the task object. This is needed for JSON serialization.
Example output: {'description': 'Buy groceries', 'due_date': '2025-08-10', 'status': 'Pending'}
@staticmethod from_dict(data: dict) -> Task: (Crucial for loading) Takes a dictionary (like the one from to_dict) and returns a new Task object.
"""

from __future__ import annotations
from typing import Dict

class Task:
    def __init__(self, description: str, due_date: str):
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

    def __str__(self) -> str:
        checkbox = "[x]" if self.status == "Completed" else "[ ]"
        return f"{checkbox} {self.description} (Due: {self.due_date})"

    def mark_complete(self) -> None:
        self.status = "Completed"

    def to_dict(self) -> Dict[str, str]:
        return {
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        task = Task(data["description"], data["due_date"])
        task.status = data.get("status", "Pending")
        return task
