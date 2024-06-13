import sqlite3

from models.db import create_connection

class CLI:
    def __init__(self):
        self.connection = create_connection

def display_menu():
    print("Task Manager CLI")
    print("1. Create Project")
    print("2. Delete Project")
    print("3. View All Projects")
    print("4. View Project Tasks")
    print("5. Find Project by ID")
    print("6. Create Task")
    print("7. Delete Task")
    print("8. View All Tasks")
    print("9. Find Task by ID")
    print("10. Exit")

def create_project():
    name = input("Enter project name: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO projects (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    print(f"Project '{name}' created.")

def delete_project():
    project_id = input("Enter project ID to delete: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    conn.close()
    print(f"Project with ID {project_id} deleted.")

def view_all_projects():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    projects = cursor.fetchall()
    conn.close()
    for project in projects:
        print(project)

def view_project_tasks():
    project_id = input("Enter project ID to view tasks: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE project_id = ?', (project_id,))
    tasks = cursor.fetchall()
    conn.close()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found for this project.")

def find_project_by_id():
    project_id = input("Enter project ID to find: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    project = cursor.fetchone()
    conn.close()
    if project:
        print(project)
    else:
        print("Project not found.")

def create_task():
    project_id = input("Enter project ID for the task: ")
    description = input("Enter task description: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description, project_id) VALUES (?, ?)', (description, project_id))
    conn.commit()
    conn.close()
    print(f"Task '{description}' created in project ID {project_id}.")

def delete_task():
    task_id = input("Enter task ID to delete: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print(f"Task with ID {task_id} deleted.")

def view_all_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    for task in tasks:
        print(task)

def find_task_by_id():
    task_id = input("Enter task ID to find: ")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    if task:
        print(task)
    else:
        print("Task not found.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            create_project()
        elif choice == '2':
            delete_project()
        elif choice == '3':
            view_all_projects()
        elif choice == '4':
            view_project_tasks()
        elif choice == '5':
            find_project_by_id()
        elif choice == '6':
            create_task()
        elif choice == '7':
            delete_task()
        elif choice == '8':
            view_all_tasks()
        elif choice == '9':
            find_task_by_id()
        elif choice == '10':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
