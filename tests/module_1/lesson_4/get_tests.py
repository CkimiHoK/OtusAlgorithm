from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import SingleArray, VectorArray, FactorArray, MatrixArray

if __name__ == "__main__":
    task = CollectionTester(SingleArray()).get
    test_task("2_get", task, "single_getter_tests_result.txt")

    task = CollectionTester(VectorArray()).get
    test_task("2_get", task, "vector_getter_tests_result.txt")

    task = CollectionTester(FactorArray()).get
    test_task("2_get", task, "factor_getter_tests_result.txt")

    task = CollectionTester(MatrixArray()).get
    test_task("2_get", task, "matrix_getter_tests_result.txt")
