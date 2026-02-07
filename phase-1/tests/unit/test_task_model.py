import pytest
from src.models.task import Task

def test_task_creation_valid_title():
    task = Task("Test Title", "Description")
    assert task.title == "Test Title"
    assert task.description == "Description"
    assert task.status == "Pending"
    assert isinstance(task.id, str)

def test_task_creation_empty_title_raises_error():
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task("", "Description")
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task("   ", "Description")

def test_task_to_from_dict_conversion():
    original_task = Task("Dict Test", "Convert Description", "Completed", "123-abc")
    task_dict = original_task.to_dict()
    
    assert task_dict["id"] == "123-abc"
    assert task_dict["title"] == "Dict Test"
    assert task_dict["description"] == "Convert Description"
    assert task_dict["status"] == "Completed"

    recreated_task = Task.from_dict(task_dict)
    assert recreated_task.id == original_task.id
    assert recreated_task.title == original_task.title
    assert recreated_task.description == original_task.description
    assert recreated_task.status == original_task.status

def test_task_from_dict_missing_description_or_status():
    data = {"id": "456-def", "title": "Missing Fields Test"}
    task = Task.from_dict(data)
    assert task.id == "456-def"
    assert task.title == "Missing Fields Test"
    assert task.description == ""
    assert task.status == "Pending"