from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    name: str
    age: int
    id: Optional[int] = None
