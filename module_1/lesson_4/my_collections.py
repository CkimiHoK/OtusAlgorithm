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
    def __init__(self):
        self.__array = []
        self.__size = 0

    def get_size(self):
        return self.__array.__len__()

    def add(self, item):
        self.__resize()
        self.__array[self.get_size() - 1] = item

    def get(self, index):
        if 0 < index < self.get_size():
            return self.__array[index]

    def remove(self, index):
        pass

    def insert(self, item, index):
        pass

    def __resize(self):
        new_array = [None for _ in range(self.get_size() + 1)]
        for index in range(self.get_size()):
            new_array[index] = self.__array[index]
        self.__array = new_array


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
