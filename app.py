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