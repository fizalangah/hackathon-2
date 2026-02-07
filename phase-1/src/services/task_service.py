from src.models.task import Task
from src.services.task_repository import TaskRepository
from typing import Optional

class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        Task.validate_title(title) # Validate title before creating task
        new_task = Task(title=title, description=description if description is not None else "")
        self._repository.add(new_task)
        return new_task

    def get_all_tasks(self) -> list[Task]:
        return self._repository.get_all()

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        task = self._repository.get_by_id(task_id)
        if not task:
            return None # Task not found

        if title is not None:
            Task.validate_title(title) # Validate new title
            task.title = title
        
        if description is not None:
            task.description = description
        
        # If no title or description was provided, ensure at least one change was made
        if title is None and description is None:
            return task # No update needed, return original task

        self._repository.update(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        return self._repository.delete(task_id)

    def mark_task_complete(self, task_id: str) -> Optional[Task]:
        task = self._repository.get_by_id(task_id)
        if not task:
            return None # Task not found

        if task.status == "Completed":
            return task # Already completed, no change

        task.status = "Completed"
        self._repository.update(task)
        return task
