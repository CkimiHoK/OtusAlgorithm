from tester import test_task
from tests.module_1.lesson_4.collection_tester import CollectionTester
from module_1.lesson_4.my_collections import StandartArrayWrapper

if __name__ == "__main__":
    tester = CollectionTester(StandartArrayWrapper())
    task = tester.add
    test_task("1_add", task, "wrapper_adder_tests_result.txt")

    tester = CollectionTester(StandartArrayWrapper())
    task = tester.get
    test_task("2_get", task, "wrapper_getter_tests_result.txt")

    tester = CollectionTester(StandartArrayWrapper())
    task = tester.remove
    test_task("3_remove", task, "wrapper_remover_tests_result.txt")

    tester = CollectionTester(StandartArrayWrapper())
    task = tester.insert
    test_task("4_insert", task, "wrapper_inserter_tests_result.txt")
