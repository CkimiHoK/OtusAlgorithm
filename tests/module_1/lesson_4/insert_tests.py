from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import SingleArray, VectorArray, FactorArray, MatrixArray

if __name__ == "__main__":
    task = CollectionTester(SingleArray()).insert
    test_task("4_insert", task, "single_inserter_tests_result.txt")

    task = CollectionTester(VectorArray()).insert
    test_task("4_insert", task, "vector_inserter_tests_result.txt")

    task = CollectionTester(FactorArray()).insert
    test_task("4_insert", task, "factor_inserter_tests_result.txt")

    task = CollectionTester(MatrixArray()).insert
    test_task("4_insert", task, "matrix_inserter_tests_result.txt")
