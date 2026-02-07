import uuid

class Task:
    @staticmethod
    def validate_title(title: str):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

    def __init__(self, title: str, description: str = "", status: str = "Pending", id: str = None):
        Task.validate_title(title)
        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "Pending")
        )