import pytest
from src.models.task import Task
from src.services.task_repository import TaskRepository

@pytest.fixture
def repo():
    return TaskRepository()

def test_add_task(repo):
    task = Task("Test Task")
    repo.add(task)
    assert len(repo.get_all()) == 1
    assert repo.get_all()[0].title == "Test Task"

def test_get_all_tasks_empty(repo):
    assert repo.get_all() == []

def test_get_all_tasks_multiple(repo):
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    repo.add(task1)
    repo.add(task2)
    tasks = repo.get_all()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks

def test_get_by_id_found(repo):
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    repo.add(task1)
    repo.add(task2)
    found_task = repo.get_by_id(task1.id)
    assert found_task == task1

def test_get_by_id_not_found(repo):
    task1 = Task("Task 1")
    repo.add(task1)
    found_task = repo.get_by_id("non-existent-id")
    assert found_task is None

def test_update_task_existing(repo):
    task = Task("Original Task")
    repo.add(task)
    updated_task = Task("Updated Task", id=task.id, status="Completed")
    assert repo.update(updated_task) is True
    retrieved_task = repo.get_by_id(task.id)
    assert retrieved_task.title == "Updated Task"
    assert retrieved_task.status == "Completed"

def test_update_task_non_existing(repo):
    task = Task("Original Task")
    repo.add(task)
    non_existent_task = Task("Non Existent", id="some-other-id")
    assert repo.update(non_existent_task) is False
    assert repo.get_by_id(task.id).title == "Original Task" # Original task unchanged

def test_delete_task_existing(repo):
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    repo.add(task1)
    repo.add(task2)
    assert repo.delete(task1.id) is True
    assert len(repo.get_all()) == 1
    assert repo.get_by_id(task1.id) is None
    assert repo.get_by_id(task2.id) == task2

def test_delete_task_non_existing(repo):
    task1 = Task("Task 1")
    repo.add(task1)
    assert repo.delete("non-existent-id") is False
    assert len(repo.get_all()) == 1