from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from adapters.sql_alchemy_person_repository import SQLAlchemyPersonRepository
from adapters.sql_alchemy_order_repository import SQLAlchemyOrderRepository
from adapters.sql_alchemy_connection import SQLAlchemyConnection
from adapters.sql_alchemy_mappers import create_tables_and_mappers
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)


@contextmanager
def create_database_session():
    Base = declarative_base()
    create_tables_and_mappers(Base.metadata)
    engine = create_engine("sqlite:///./db/data.db")
    Base.metadata.create_all(engine)
    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()


with create_database_session() as session:
    connection = SQLAlchemyConnection(session)
    person_repository = SQLAlchemyPersonRepository(session)
    order_repository = SQLAlchemyOrderRepository(session)

    unit_of_work = UnitOfWork(connection, person_repository,
                              order_repository)
    create_use_case = CreatePersonAndOrderUseCase(unit_of_work)

    new_person = Person(id=None, name="John Doe", age=30)
    new_order = Order(person_id=None, order_date="2023-04-03",
                      total_amount=100.0)

    person, order = create_use_case.execute(new_person, new_order)
    print(person)
    print(order)
