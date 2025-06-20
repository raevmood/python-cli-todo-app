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
    print("Task added.")

def list_tasks(args):
    tasks = load_tasks()
    if args.today:
        tasks = get_today_tasks(tasks)
    if not tasks:
        print("No tasks found today, Take a break!")
    for task in tasks:
        print(task)

def complete_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task.id == args.id:
            task.mark_complete()
            save_tasks(tasks)
            print("Task marked complete.")
            return
    print("Task ID not found.")

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("title")
    add.add_argument("description")
    add.add_argument("--due_date", help="Due date in YYYY-MM-DD format")
    add.set_defaults(func=add_task)

    list_cmd = subparsers.add_parser("list")
    list_cmd.add_argument("--today", action="store_true")
    list_cmd.set_defaults(func=list_tasks)

    complete = subparsers.add_parser("complete")
    complete.add_argument("id", type=int)
    complete.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()