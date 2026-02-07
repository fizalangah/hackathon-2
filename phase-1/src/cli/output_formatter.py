from src.models.task import Task
from typing import List

def display_tasks(tasks: List[Task]):
    if not tasks:
        print("No tasks available.")
        return

    print(f"{'ID':<40} {'Title':<30} {'Status':<10}")
    print("-" * 80)
    for task in tasks:
        print(f"{task.id:<40} {task.title:<30} {task.status:<10}")