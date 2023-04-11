from typing import Optional
from sqlalchemy.orm import Session

from adapters.base_repository import BaseRepository
from domain.order import Order


class SQLAlchemyOrderRepository(BaseRepository[Order]):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order):
        self.session.add(order)

    def update(self, order: Order):
        self.session.merge(order)

    def delete(self, order_id: int):
        order = self.session.get(Order, order_id)
        if order:
            self.session.delete(order)

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return self.session.get(Order, order_id)
