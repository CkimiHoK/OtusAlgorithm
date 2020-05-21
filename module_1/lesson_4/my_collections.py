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


class SingleArray(IArray):
    def get_size(self):
        pass

    def add(self, item):
        pass

    def get(self, index):
        pass

    def remove(self, index):
        pass

    def insert(self, item, index):
        pass


class VectorArray(IArray):
    def get_size(self):
        pass

    def add(self, item):
        pass

    def get(self, index):
        pass

    def remove(self, index):
        pass

    def insert(self, item, index):
        pass


class FactorArray(IArray):
    def get_size(self):
        pass

    def add(self, item):
        pass

    def get(self, index):
        pass

    def remove(self, index):
        pass

    def insert(self, item, index):
        pass


class MatrixArray(IArray):
    def get_size(self):
        pass

    def add(self, item):
        pass

    def get(self, index):
        pass

    def remove(self, index):
        pass

    def insert(self, item, index):
        pass
