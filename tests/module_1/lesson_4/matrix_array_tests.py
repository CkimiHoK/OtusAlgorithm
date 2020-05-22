from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import MatrixArray

if __name__ == "__main__":
    tester = CollectionTester(MatrixArray())

    task = tester.add
    test_task("1_add", task, "matrix_adder_tests_result.txt")

    task = tester.get
    test_task("2_get", task, "matrix_getter_tests_result.txt")

    task = tester.remove
    test_task("3_remove", task, "matrix_remover_tests_result.txt")

    task = tester.insert
    test_task("4_insert", task, "matrix_inserter_tests_result.txt")
