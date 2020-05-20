from tester import test_task
from module_1.lesson_4.collection_adder import add

if __name__ == "__main__":
    task = add
    test_task("1_add", task, "collection_adder_tests_result.txt")
