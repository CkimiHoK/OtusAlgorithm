from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import SingleArray, VectorArray, FactorArray, MatrixArray

if __name__ == "__main__":
    task = CollectionTester(SingleArray()).remove
    test_task("3_remove", task, "single_remover_tests_result.txt")

    task = CollectionTester(VectorArray()).remove
    test_task("3_remove", task, "vector_remover_tests_result.txt")

    task = CollectionTester(FactorArray()).remove
    test_task("3_remove", task, "factor_remover_tests_result.txt")

    task = CollectionTester(MatrixArray()).remove
    test_task("3_remove", task, "matrix_remover_tests_result.txt")
