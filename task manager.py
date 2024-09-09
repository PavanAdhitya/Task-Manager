import json
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"{i}. {task['task']} - {status}")
def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")
def edit_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task_name = input("Enter the new task name: ")
        tasks[task_index]['task'] = new_task_name
        print("Task updated successfully!")
    else:
        print("Invalid task number!")
def delete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted successfully!")
    else:
        print("Invalid task number!")
def mark_task_complete(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Task '{tasks[task_index]['task']}' marked as complete!")
    else:
        print("Invalid task number!")
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Display tasks")
        print("2. Add a new task")
        print("3. Edit a task")
        print("4. Delete a task")
        print("5. Mark a task as complete")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved! Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")
if __name__ == "__main__":
    main()
