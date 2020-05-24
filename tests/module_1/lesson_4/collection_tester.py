import time
from random import randint


class CollectionTester:
    def __init__(self, collection) -> None:
        self.__collection = collection

    def add(self, str_array):
        item_count = int(str_array[0])

        start_time = time.perf_counter()
        for index in range(item_count):
            self.__collection.add(index)  # added incremented elements
        end_time = time.perf_counter()

        return f'Time: {(end_time - start_time):.6f}'

    def get(self, str_array):
        self.add(str_array)  # fill collection
        hard_code_get_count = 1

        start_time = time.perf_counter()
        for _ in range(hard_code_get_count):
            index = randint(0, self.__collection.get_size() - 1)  # get random index to get element
            item = self.__collection.get(index)
        end_time = time.perf_counter()

        return f'Time: {(end_time - start_time):.6f}'

    def remove(self, str_array):
        self.add(str_array)  # fill collection
        hard_code_remove_count = 1

        start_time = time.perf_counter()
        for _ in range(hard_code_remove_count):
            index = self.__collection.get_size() // 2  # remove element from the middle of array
            item = self.__collection.remove(index)
        end_time = time.perf_counter()

        return f'Time: {(end_time - start_time):.6f}'

    def insert(self, str_array):
        item_count = int(str_array[0])

        start_time = time.perf_counter()
        for item in range(item_count):
            index = self.__collection.get_size() // 2  # insert element into the middle of array
            self.__collection.insert(item, index)
        end_time = time.perf_counter()

        return f'Time: {(end_time - start_time):.6f}'
