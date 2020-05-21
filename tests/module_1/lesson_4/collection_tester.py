import time


class CollectionTester:
    def __init__(self, collection) -> None:
        self.__collection = collection

    def add(self, str_array):
        hard_code_item = 123
        item_count = int(str_array[0])

        start_time = time.perf_counter()
        for index in range(item_count):
            self.__collection.add(hard_code_item)
        end_time = time.perf_counter()

        return f'Time: {(end_time - start_time):.6f}'

    def get(self, str_array):
        pass

    def remove(self, str_array):
        pass

    def insert(self, str_array):
        pass
