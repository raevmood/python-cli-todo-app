import json
import os
from task import Task
from datetime import date

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        data = json.load(f)
    return [Task(**task) for task in data]