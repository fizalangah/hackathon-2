import pytest
from src.models.task import Task
from src.services.task_repository import TaskRepository
from src.services.task_service import TaskService
from unittest.mock import Mock, patch

@pytest.fixture
def task_repo_mock():
    return Mock(spec=TaskRepository)

@pytest.fixture
def task_service(task_repo_mock):
    return TaskService(task_repo_mock)

def test_add_task_success(task_service, task_repo_mock):
    title = "Buy groceries"
    description = "Milk, Eggs, Bread"
    
    task = task_service.add_task(title, description)
    
    assert isinstance(task, Task)
    assert task.title == title
    assert task.description == description
    assert task.status == "Pending"
    assert isinstance(task.id, str) # Check that an ID is assigned and it's a string
    assert task.id is not None
    task_repo_mock.add.assert_called_once()
    assert task_repo_mock.add.call_args[0][0].title == title

def test_add_task_empty_title_raises_error(task_service, task_repo_mock):
    with pytest.raises(ValueError, match="Title cannot be empty"):
        task_service.add_task("", "Description")
    task_repo_mock.add.assert_not_called()

def test_get_all_tasks_with_tasks(task_service, task_repo_mock):
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    task_repo_mock.get_all.return_value = [task1, task2]
    
    tasks = task_service.get_all_tasks()
    
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks
    task_repo_mock.get_all.assert_called_once()

def test_get_all_tasks_no_tasks(task_service, task_repo_mock):
    task_repo_mock.get_all.return_value = []
    
    tasks = task_service.get_all_tasks()
    
    task_repo_mock.get_all.assert_called_once()

def test_update_task_success(task_service, task_repo_mock):
    existing_task = Task("Old Title", "Old Description", "Pending", "123")
    task_repo_mock.get_by_id.return_value = existing_task
    
    updated_title = "New Title"
    updated_description = "New Description"
    
    updated_task = task_service.update_task("123", updated_title, updated_description)
    
    assert updated_task.id == "123"
    assert updated_task.title == updated_title
    assert updated_task.description == updated_description
    assert updated_task.status == "Pending" # Status should not change
    task_repo_mock.get_by_id.assert_called_once_with("123")
    task_repo_mock.update.assert_called_once()
    assert task_repo_mock.update.call_args[0][0].id == "123"
    assert task_repo_mock.update.call_args[0][0].title == updated_title

def test_update_task_not_found(task_service, task_repo_mock):
    task_repo_mock.get_by_id.return_value = None
    
    updated_task = task_service.update_task("non-existent-id", "New Title")
    
    assert updated_task is None
    task_repo_mock.get_by_id.assert_called_once_with("non-existent-id")
    task_repo_mock.update.assert_not_called()

def test_update_task_empty_title_raises_error(task_service, task_repo_mock):
    existing_task = Task("Old Title", "Old Description", "Pending", "123")
    task_repo_mock.get_by_id.return_value = existing_task
    
    with pytest.raises(ValueError, match="Title cannot be empty"):
        task_service.update_task("123", "")
    
    task_repo_mock.get_by_id.assert_called_once_with("123")
    task_repo_mock.update.assert_not_called()

def test_delete_task_success(task_service, task_repo_mock):
    task_id = "123"
    task_repo_mock.delete.return_value = True
    
    result = task_service.delete_task(task_id)
    
    assert result is True
    task_repo_mock.delete.assert_called_once_with(task_id)

def test_delete_task_not_found(task_service, task_repo_mock):
    task_id = "non-existent-id"
    task_repo_mock.delete.return_value = False
    
    result = task_service.delete_task(task_id)
    
    task_repo_mock.delete.assert_called_once_with(task_id)

def test_mark_task_complete_success(task_service, task_repo_mock):
    existing_task = Task("Pending Task", status="Pending", id="123")
    task_repo_mock.get_by_id.return_value = existing_task
    
    completed_task = task_service.mark_task_complete("123")
    
    assert completed_task.id == "123"
    assert completed_task.status == "Completed"
    task_repo_mock.get_by_id.assert_called_once_with("123")
    task_repo_mock.update.assert_called_once()
    assert task_repo_mock.update.call_args[0][0].status == "Completed"

def test_mark_task_complete_not_found(task_service, task_repo_mock):
    task_repo_mock.get_by_id.return_value = None
    
    result = task_service.mark_task_complete("non-existent-id")
    
    task_repo_mock.get_by_id.assert_called_once_with("non-existent-id")
    task_repo_mock.update.assert_not_called()

def test_mark_task_complete_already_complete(task_service, task_repo_mock):
    existing_task = Task("Completed Task", status="Completed", id="123")
    task_repo_mock.get_by_id.return_value = existing_task
    
    completed_task = task_service.mark_task_complete("123")
    
    assert completed_task.id == "123"
    assert completed_task.status == "Completed" # Status should remain Completed
    task_repo_mock.get_by_id.assert_called_once_with("123")
    task_repo_mock.update.assert_not_called()