import argparse
from utils import load_tasks, save_tasks, generate_id, get_today_tasks
from task import Task

def add_task(args):
    tasks = load_tasks()
    new_task = Task(
        id=generate_id(tasks),
        title=args.title,
        description=args.description,
        due_date=args.due_date
    )
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{args.title}' added with ID {new_task.id}.")

def list_tasks(args):
    tasks = load_tasks()
    
    if args.today:
        tasks_to_show = get_today_tasks(tasks)
        if not tasks_to_show:
            print("No tasks due today. Take a break!")
            return
        else:
            print("--- Tasks Due Today ---")
    else:
        tasks_to_show = tasks
        if not tasks_to_show:
            print("No tasks found. Add one with the 'add' command!")
            return
        else:
            print("--- All Tasks ---")

    for task in tasks_to_show:
        print(task)

def complete_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task.id == args.id:
            task.mark_complete()
            save_tasks(tasks)
            print(f"Task {task.id} marked complete.")
            return
    print("Task ID not found.")

def delete_task(args):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task.id != args.id]
    if len(tasks) == len(new_tasks):
        print("Task ID not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {args.id} deleted.")

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("title", help="The title of the task")
    add.add_argument("description", help="The description of the task")
    add.add_argument("--due_date", help="Optional due date in YYYY-MM-DD format")
    add.set_defaults(func=add_task)

    list_cmd = subparsers.add_parser("list", help="List all tasks")
    list_cmd.add_argument("--today", action="store_true", help="Only show tasks due today")
    list_cmd.set_defaults(func=list_tasks)

    complete = subparsers.add_parser("complete", help="Mark a task as complete")
    complete.add_argument("id", type=int, help="The ID of the task to complete")
    complete.set_defaults(func=complete_task)
  
    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("id", type=int, help="The ID of the task to delete")
    delete.set_defaults(func=delete_task)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()