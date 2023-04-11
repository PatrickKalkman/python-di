from typing import TypeVar, Generic, Optional
from abc import ABC, abstractmethod

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    """A base class for repositories"""

    @abstractmethod
    def add(self, item: T):
        """Add a new item to a repository"""
        raise NotImplementedError()

    @abstractmethod
    def update(self, item: T):
        """Update an existing item in the repository"""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item_id: int):
        """Delete an existing item from a repository"""
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, item_id: int) -> Optional[T]:
        """Retrieve an item by its id"""
        raise NotImplementedError()
