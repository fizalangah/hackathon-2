import dataclasses
from typing import Optional


@dataclasses.dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
