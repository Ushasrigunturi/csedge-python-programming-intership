tasks = []

def add_task(task_name):
    task = {
        'name': task_name,
        'completed': False
    }
    tasks.append(task)
    print(f"Task '{task_name}' added.")

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' deleted.")
    except IndexError:
        print("Invalid task index.")

def complete_task(task_index):
    try:
        tasks[task_index]['completed'] = True
        print(f"Task '{tasks[task_index]['name']}' marked as completed.")
    except IndexError:
        print("Invalid task index.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['name']} - {status}")
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_task(task_index)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            print(" exiting to-do list  task manager")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

tasks = []
