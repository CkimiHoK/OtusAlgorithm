from tester import test_task
from module_2.lesson_5_6.heap_sort import heap_sort

if __name__ == "__main__":
    task = heap_sort

    test_task("0_random", task, "heap_random_tests_result.txt")
    test_task("1_digits", task, "heap_digits_tests_result.txt")
    test_task("2_sorted", task, "heap_sorted_tests_result.txt")
    test_task("3_revers", task, "heap_revers_tests_result.txt")
