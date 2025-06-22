from utils import load_tasks, save_tasks, generate_id, get_today_tasks
from task import Task

def add_task():
    """Prompts user for task details and adds a new task."""
    tasks = load_tasks()
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ")

    if not due_date:
        due_date = None

    new_task = Task(
        id=generate_id(tasks),
        title=title,
        description=description,
        due_date=due_date
    )
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\nTask '{title}' added with ID {new_task.id}.")

def list_tasks(today_only=False):
    """Lists all tasks or only tasks due today."""
    tasks = load_tasks()

    if today_only:
        tasks_to_show = get_today_tasks(tasks)
        header = "--- Tasks Due Today ---"
        no_tasks_message = "No tasks due today. Take a break!"
    else:
        tasks_to_show = tasks
        header = "--- All Tasks ---"
        no_tasks_message = "No tasks found. Add one using option '1'!"

    if not tasks_to_show:
        print(no_tasks_message)
        return

    print(header)
    for task in tasks_to_show:
        print(task)

def complete_task():
    """Marks a specific task as complete after getting an ID from the user."""
    list_tasks()
    tasks = load_tasks()
    if not tasks:
        return

    try:
        task_id = int(input("\nEnter the ID of the task to mark as complete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task.id == task_id:
            task.mark_complete()
            save_tasks(tasks)
            print(f"Task {task.id} marked complete.")
            return
    print("Task ID not found.")

def delete_task():
    """Deletes a specific task after getting an ID from the user."""
    list_tasks()
    tasks = load_tasks()
    if not tasks:
        return

    try:
        task_id = int(input("\nEnter the ID of the task to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    new_tasks = [task for task in tasks if task.id != task_id]
    if len(tasks) == len(new_tasks):
        print("Task ID not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted.")

def main():
    """Main application loop to display menu and handle user choices."""
    while True:
        print("\n===== CLI Task Manager =====")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. List tasks due today")
        print("4. Mark a task as complete")
        print("5. Delete a task")
        print("6. Exit")
        print("============================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks(today_only=True)
        elif choice == '4':
            complete_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()