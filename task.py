from datetime import date

class Task:
    def __init__(self, id, title, description, due_date=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        if self.completed:
          status = "✓"
        else: status = "✗"
        if self.due_date:
            due = self.due_date
        else: due = "No due date"
        return f"[{self.id}] {self.title} ({status}) - Due: {due}\n    {self.description}"
