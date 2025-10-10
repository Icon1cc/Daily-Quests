"""
This file will contain the user interface and the main application loop.
File: main.py
Purpose: To interact with the user, process commands, and orchestrate the TodoList object.
Workflow:
Define a constant for the filename, e.g., TODO_FILE = "mytasks.json".
Create an instance of the TodoList class.
Immediately call todo_list.load_from_file(TODO_FILE) to populate the list with any previously saved tasks.
Enter an infinite while True loop that presents the user with a menu of options.
The menu should show available commands: add, list, complete, delete, help, exit.
Use input() to get the user's command.
Use an if/elif/else block to process the command:
add: Prompt the user for a description and due date, then call todo_list.add_task().
list: Call todo_list.list_tasks().
complete: Prompt for a task number, then call todo_list.mark_task_complete().
delete: Prompt for a task number, then call todo_list.delete_task().
help: Print a helpful message explaining the commands.
exit: Call todo_list.save_to_file(TODO_FILE) to save all changes, then break the loop to end the program.
else: Handle invalid commands.
"""

from __future__ import annotations
from todolist import TodoList

TODO_FILE = "./Python Refresher/Command_Line_To-Do_List_Manager/mytasks.json"

def print_help() -> None:
    help_text = """
Available commands:
  add      - Add a new task
  list     - List all tasks
  complete - Mark a task as complete
  delete   - Delete a task
  help     - Show this help message
  exit     - Save and exit the program
"""
    print(help_text)

def main() -> None:
    todo_list = TodoList()
    todo_list.load_from_file(TODO_FILE)

    while True:
        command = input("\nEnter a command (add, list, complete, delete, help, exit): ").strip().lower()

        if not command:
            continue

        if command == "add":
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            todo_list.add_task(description, due_date)

        elif command == "list":
            todo_list.list_tasks()

        elif command == "complete":
            try:
                index = int(input("Enter task number to mark complete: ").strip())
                todo_list.mark_task_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "delete":
            try:
                index = int(input("Enter task number to delete: ").strip())
                todo_list.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "help":
            print_help()

        elif command == "exit":
            todo_list.save_to_file(TODO_FILE)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid command. Type 'help' to see available options.")

if __name__ == "__main__":
    main()
