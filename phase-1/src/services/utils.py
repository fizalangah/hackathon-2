import uuid

def generate_unique_id() -> str:
    """Generates a unique string ID."""
    return str(uuid.uuid4())