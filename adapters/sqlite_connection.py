import sqlite3
from adapters.base_connection import BaseConnection


class SQLiteConnection(BaseConnection):
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
