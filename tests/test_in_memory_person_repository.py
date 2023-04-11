import pytest
from domain.person import Person
from adapters.in_memory_person_repository import InMemoryPersonRepository


@pytest.fixture
def repository():
    return InMemoryPersonRepository()


def test_add_person(repository):
    person = Person(name="John Doe", age=30, id=1)
    repository.add(person)

    retrieved_person = repository.get_by_id(1)
    assert retrieved_person is not None
    assert retrieved_person.name == person.name
    assert retrieved_person.age == person.age


def test_update_person(repository):
    person = Person(name="John Doe", age=30, id=1)
    repository.add(person)

    person.name = "Jane Doe"
    person.age = 28
    repository.update(person)

    updated_person = repository.get_by_id(1)
    assert updated_person.name == "Jane Doe"
    assert updated_person.age == 28


def test_delete_person(repository):
    person = Person(name="John Doe", age=30, id=1)
    repository.add(person)
    repository.delete(1)

    deleted_person = repository.get_by_id(1)
    assert deleted_person is None


def test_get_by_id_person_not_found(repository):
    non_existent_person = repository.get_by_id(999)
    assert non_existent_person is None
