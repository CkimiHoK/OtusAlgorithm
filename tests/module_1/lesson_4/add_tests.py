from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import SingleArray, VectorArray, FactorArray, MatrixArray

if __name__ == "__main__":
    task = CollectionTester(SingleArray()).add
    test_task("1_add", task, "single_adder_tests_result.txt")

    task = CollectionTester(VectorArray()).add
    test_task("1_add", task, "vector_adder_tests_result.txt")

    task = CollectionTester(FactorArray()).add
    test_task("1_add", task, "factor_adder_tests_result.txt")

    task = CollectionTester(MatrixArray()).add
    test_task("1_add", task, "matrix_adder_tests_result.txt")
