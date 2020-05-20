from tester import test_task
from module_1.lesson_4.collection_remover import remove

if __name__ == "__main__":
    task = remove
    test_task("3_remove", task, "collection_remover_tests_result.txt")
