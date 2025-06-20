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

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("title")
    add.add_argument("description")
    add.add_argument("--due_date", help="Due date in YYYY-MM-DD format")
    add.set_defaults(func=add_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()