from adapters.base_connection import BaseConnection
from adapters.base_repository import BaseRepository
from domain.order import Order
from domain.person import Person


class UnitOfWork:
    def __init__(self, connection: BaseConnection,
                 person_repository: BaseRepository[Person],
                 order_repository: BaseRepository[Order]):
        self.persons = person_repository
        self.orders = order_repository
        self.connection = connection

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
