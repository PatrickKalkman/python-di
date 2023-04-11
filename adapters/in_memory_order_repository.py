from typing import Optional
from adapters.base_repository import BaseRepository
from domain.order import Order


class InMemoryOrderRepository(BaseRepository[Order]):
    def __init__(self):
        self.orders = {}

    def add(self, order: Order):
        self.orders[order.id] = order

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return self.orders.get(order_id)

    def update(self, order: Order):
        self.orders[order.id] = order

    def delete(self, order_id: int):
        self.orders.pop(order_id, None)
