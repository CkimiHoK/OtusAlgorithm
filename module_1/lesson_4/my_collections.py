from abc import ABC, abstractmethod


class IArray(ABC):
    def __init__(self):
        self.array = []
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, item):
        if self.size >= self.array.__len__():  # resize internal array if need
            self.resize()
        self.array[self.size] = item
        self.size += 1

    def get(self, index):
        if 0 <= index < self.get_size():
            return self.array[index]
        else:
            raise IndexError

    def remove(self, index):
        if 0 <= index < self.get_size():
            item = self.array[index]  # get item
            for i in range(index, self.size - 1):  # move elements to the left
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None  # drop last element
            self.size -= 1
            return item
        else:
            raise IndexError

    def insert(self, item, index):
        if self.size >= self.array.__len__():  # resize internal array if need
            self.resize()
        if 0 <= index < self.get_size() or index == 0:
            for i in range(self.size, index, -1):  # move elements to the right
                self.array[i] = self.array[i - 1]
            self.array[index] = item  # insert element
            self.size += 1
        else:
            raise IndexError

    @abstractmethod
    def resize(self):
        pass


class SingleArray(IArray):
    def resize(self):
        new_array = [None for _ in range(self.get_size() + 1)]  # increment by 1
        for index in range(self.get_size()):
            new_array[index] = self.array[index]
        self.array = new_array


class VectorArray(IArray):
    def __init__(self, vector=10):
        super().__init__()
        self.vector = vector

    def resize(self):
        new_array = [None for _ in range(self.get_size() + self.vector)]  # increment by vector size
        for index in range(self.get_size()):
            new_array[index] = self.array[index]
        self.array = new_array


class FactorArray(IArray):
    def __init__(self, multiplier=2):
        super().__init__()
        self.array = [None]  # we need to initiate array at least 1 element
        self.multiplier = multiplier

    def resize(self):
        new_array = [None for _ in range(self.get_size() * self.multiplier)]  # multiply by self.multiplier size
        for index in range(self.get_size()):
            new_array[index] = self.array[index]
        self.array = new_array


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

    def resize(self):
        pass


class StandartArrayWrapper(IArray):
    def get_size(self):
        return len(self.array)

    def add(self, item):
        self.array.append(item)

    def get(self, index):
        return self.array[index]

    def remove(self, index):
        return self.array.pop(index)

    def insert(self, item, index):
        self.array.insert(index, item)

    def resize(self):
        pass  # not need to realize this method
