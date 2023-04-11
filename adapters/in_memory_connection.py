
from adapters.base_connection import BaseConnection


class InMemoryConnection(BaseConnection):
    def commit(self):
        pass

    def rollback(self):
        pass
