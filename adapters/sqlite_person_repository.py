from typing import Optional

from adapters.base_repository import BaseRepository
from domain.person import Person


class SQLitePersonRepository(BaseRepository[Person]):
    def __init__(self, connection):
        self.connection = connection
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def add(self, person: Person):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO persons (name, age) VALUES (?, ?)",
            (person.name, person.age)
        )
        person.id = cursor.lastrowid

    def get_by_id(self, person_id: int) -> Optional[Person]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, age FROM persons WHERE id=?",
                       (person_id,))
        row = cursor.fetchone()
        if row:
            return Person(row[1], row[2], row[0])
        return None

    def update(self, person: Person):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE persons SET name=?, age=? WHERE id=?",
            (person.name, person.age, person.id)
        )

    def delete(self, person_id: int):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM persons WHERE id=?", (person_id,))
