from src.services.utils import generate_unique_id
import uuid

def test_generate_unique_id_returns_string():
    _id = generate_unique_id()
    assert isinstance(_id, str)

def test_generate_unique_id_returns_unique_values():
    id1 = generate_unique_id()
    id2 = generate_unique_id()
    assert id1 != id2

def test_generate_unique_id_returns_valid_uuid():
    _id = generate_unique_id()
    # Attempt to parse as UUID to check format validity
    uuid.UUID(_id)