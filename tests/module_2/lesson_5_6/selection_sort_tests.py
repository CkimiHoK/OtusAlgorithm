from tester import test_task
from module_2.lesson_5_6.selection_sort import selection_sort

if __name__ == "__main__":
    task = selection_sort

    test_task("0_random", task, "selection_random_tests_result.txt")
    test_task("1_digits", task, "selection_digits_tests_result.txt")
    test_task("2_sorted", task, "selection_sorted_tests_result.txt")
    test_task("3_revers", task, "selection_revers_tests_result.txt")
