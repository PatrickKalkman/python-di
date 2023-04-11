from typing import Optional
from sqlalchemy.orm import Session

from adapters.base_repository import BaseRepository
from domain.person import Person


class SQLAlchemyPersonRepository(BaseRepository[Person]):
    def __init__(self, session: Session):
        self.session = session

    def add(self, person: Person):
        self.session.add(person)
        # flush() is needed to get the id of the person
        self.session.flush()

    def update(self, person: Person):
        self.session.merge(person)

    def delete(self, person_id: int):
        person = self.session.get(Person, person_id)
        if person:
            self.session.delete(person)

    def get_by_id(self, person_id: int) -> Optional[Person]:
        return self.session.get(Person, person_id)
