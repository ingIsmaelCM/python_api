from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    async def get(self):
        pass

    @abstractmethod
    async def find(self, key, value):
        pass

    @abstractmethod
    async def find_by_id(self, value_id):
        pass

    @abstractmethod
    async def create(self, data):
        pass

    