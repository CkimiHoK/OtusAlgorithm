from tester import test_task
from module_1.lesson_4.collection_getter import get

if __name__ == "__main__":
    task = get
    test_task("2_get", task, "collection_getter_tests_result.txt")
