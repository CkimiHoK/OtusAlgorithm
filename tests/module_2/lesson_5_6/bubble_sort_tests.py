from tester import test_task
from module_2.lesson_5_6.bubble_sort import bubble_sort

if __name__ == "__main__":
    task = bubble_sort

    test_task("0_random", task, "bubble_random_tests_result.txt")
    test_task("1_digits", task, "bubble_digits_tests_result.txt")
    test_task("2_sorted", task, "bubble_sorted_tests_result.txt")
    test_task("3_revers", task, "bubble_revers_tests_result.txt")
