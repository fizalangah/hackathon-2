from typing import List, Optional
from todo_app.models.task import Task


class TaskCollection:
    _next_id: int
    _tasks: List[Task]

    def __init__(self):
        self._next_id = 1
        self._tasks = []

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in self._tasks if task.id == task_id), None)

    def get_all_tasks(self) -> List[Task]:
        return self._tasks

    def update_task(self, task_id: int, new_title: Optional[str] = None, new_description: Optional[str] = None) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            if new_title is not None:
                task.title = new_title
            if new_description is not None:
                task.description = new_description
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        initial_len = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) < initial_len

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
            return task
        return None
