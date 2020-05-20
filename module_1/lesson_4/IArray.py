from abc import ABC, abstractmethod


class IArray(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def insert(self, item, index):
        pass
