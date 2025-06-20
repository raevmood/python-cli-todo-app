import json
import os
from task import Task
from datetime import date

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return [] 
    return [Task(**task) for task in data]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def generate_id(tasks):
    if not tasks:
      return 1
    else:
      return max(task.id for task in tasks) + 1

def get_today_tasks(tasks):
    today = date.today().isoformat()
    return [task for task in tasks if task.due_date == today]