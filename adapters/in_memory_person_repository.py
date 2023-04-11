from typing import Optional
from adapters.base_repository import BaseRepository
from domain.person import Person


class InMemoryPersonRepository(BaseRepository[Person]):
    def __init__(self):
        self.persons = {}

    def add(self, person: Person):
        self.persons[person.id] = person

    def get_by_id(self, person_id: int) -> Optional[Person]:
        return self.persons.get(person_id)

    def update(self, person: Person):
        self.persons[person.id] = person

    def delete(self, person_id: int):
        self.persons.pop(person_id, None)
