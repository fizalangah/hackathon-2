from typing import List, Optional
from src.models.task import Task

class TaskRepository:
    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def get_all(self) -> List[Task]:
        return list(self._tasks) # Return a copy to prevent external modification

    def get_by_id(self, task_id: str) -> Optional[Task]:
        return next((task for task in self._tasks if task.id == task_id), None)

    def update(self, updated_task: Task) -> bool:
        for i, task in enumerate(self._tasks):
            if task.id == updated_task.id:
                self._tasks[i] = updated_task
                return True
        return False

    def delete(self, task_id: str) -> bool:
        initial_len = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) < initial_len
