from sqlalchemy.orm import Session
from adapters.base_connection import BaseConnection


class SQLAlchemyConnection(BaseConnection):
    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
