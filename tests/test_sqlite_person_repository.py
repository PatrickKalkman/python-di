import sqlite3
from domain.person import Person
from adapters.sqlite_person_repository import SQLitePersonRepository
import pytest


@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def repository(connection):
    return SQLitePersonRepository(connection)


def test_add_person(repository):
    person = Person(name="John Doe", age=30)
    repository.add(person)

    retrieved_person = repository.get_by_id(person.id)
    assert retrieved_person is not None
    assert retrieved_person.name == person.name
    assert retrieved_person.age == person.age


def test_update_person(repository):
    person = Person(name="John Doe", age=30)
    repository.add(person)

    person.name = "Jane Doe"
    person.age = 28
    repository.update(person)

    updated_person = repository.get_by_id(person.id)
    assert updated_person.name == "Jane Doe"
    assert updated_person.age == 28


def test_delete_person(repository):
    person = Person(name="John Doe", age=30)
    repository.add(person)
    repository.delete(person.id)

    deleted_person = repository.get_by_id(person.id)
    assert deleted_person is None


def test_get_by_id_person_not_found(repository):
    non_existent_person = repository.get_by_id(999)
    assert non_existent_person is None
