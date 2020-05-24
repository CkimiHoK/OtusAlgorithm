from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import SingleArray

if __name__ == "__main__":
    tester = CollectionTester(SingleArray())
    task = tester.add
    test_task("1_add", task, "single_adder_tests_result.txt")

    tester = CollectionTester(SingleArray())
    task = tester.get
    test_task("2_get", task, "single_getter_tests_result.txt")

    tester = CollectionTester(SingleArray())
    task = tester.remove
    test_task("3_remove", task, "single_remover_tests_result.txt")

    tester = CollectionTester(SingleArray())
    task = tester.insert
    test_task("4_insert", task, "single_inserter_tests_result.txt")
