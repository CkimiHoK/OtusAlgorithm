from tester import test_task
from module_1.lesson_4.collection_inserter import insert

if __name__ == "__main__":
    task = insert
    test_task("4_insert", task, "collection_inserter_tests_result.txt")
