from typing import Optional

from domain.order import Order
from adapters.base_repository import BaseRepository


class SQLiteOrderRepository(BaseRepository[Order]):
    def __init__(self, connection):
        self.connection = connection
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                FOREIGN KEY (person_id) REFERENCES persons (id)
            )
        ''')
        self.connection.commit()

    def add(self, order: Order):
        query = """
        INSERT INTO orders (person_id, order_date, total_amount)
        VALUES (?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (order.person_id, order.order_date,
                               order.total_amount))
        order.id = cursor.lastrowid

    def update(self, order: Order):
        query = """
        UPDATE orders
        SET person_id = ?, order_date = ?, total_amount = ?
        WHERE id = ?
        """
        self.connection.execute(query, (order.person_id, order.order_date,
                                order.total_amount, order.id))

    def delete(self, order_id: int):
        query = "DELETE FROM orders WHERE id = ?"
        self.connection.execute(query, (order_id,))

    def get_by_id(self, order_id: int) -> Optional[Order]:
        query = """
        SELECT id, person_id, order_date, total_amount
        FROM orders WHERE id = ?
        """
        cursor = self.connection.execute(query, (order_id,))
        row = cursor.fetchone()
        if row:
            return Order(id=row[0], person_id=row[1], order_date=row[2],
                         total_amount=row[3])
        return None
