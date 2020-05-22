from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import FactorArray

if __name__ == "__main__":
    tester = CollectionTester(FactorArray())

    task = tester.add
    test_task("1_add", task, "factor_adder_tests_result.txt")

    task = tester.get
    test_task("2_get", task, "factor_getter_tests_result.txt")

    task = tester.remove
    test_task("3_remove", task, "factor_remover_tests_result.txt")

    task = tester.insert
    test_task("4_insert", task, "factor_inserter_tests_result.txt")
