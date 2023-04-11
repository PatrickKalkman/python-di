from abc import ABC, abstractmethod


class BaseConnection(ABC):
    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()
