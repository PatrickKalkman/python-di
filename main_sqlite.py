from contextlib import contextmanager
import sqlite3

from adapters.sqlite_person_repository import SQLitePersonRepository
from adapters.sqlite_order_repository import SQLiteOrderRepository
from adapters.sqlite_connection import SQLiteConnection
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)


@contextmanager
def create_database_connection():
    db_connection = sqlite3.connect("./db/data.db")
    try:
        yield db_connection
    finally:
        db_connection.close()


with create_database_connection() as conn:
    connection = SQLiteConnection(conn)
    person_repository = SQLitePersonRepository(conn)
    order_repository = SQLiteOrderRepository(conn)

    unit_of_work = UnitOfWork(connection, person_repository,
                              order_repository)
    create_use_case = CreatePersonAndOrderUseCase(unit_of_work)

    new_person = Person(name="John Doe", age=30)
    new_order = Order(person_id=None, order_date="2023-04-03",
                      total_amount=100.0)

    person, order = create_use_case.execute(new_person, new_order)
