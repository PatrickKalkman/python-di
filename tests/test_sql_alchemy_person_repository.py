import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from domain.person import Person
from adapters.sql_alchemy_person_repository import SQLAlchemyPersonRepository
from adapters.sql_alchemy_mappers import create_tables_and_mappers


Base = declarative_base()


@pytest.fixture(scope="module")
def engine():
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="module")
def connection(engine):
    with engine.connect() as connection:
        yield connection


@pytest.fixture(scope="module")
def session(engine, connection):
    Session = sessionmaker(bind=engine)
    create_tables_and_mappers(Base.metadata)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=connection)
    yield session
    session.close()


@pytest.fixture
def repository(session):
    return SQLAlchemyPersonRepository(session)


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


def test_delete_person(repository, session):
    person = Person(name="John Doe", age=30)
    repository.add(person)
    repository.delete(person.id)
    session.flush()

    deleted_person = repository.get_by_id(person.id)
    assert deleted_person is None


def test_get_by_id_person_not_found(repository):
    non_existent_person = repository.get_by_id(999)
    assert non_existent_person is None
