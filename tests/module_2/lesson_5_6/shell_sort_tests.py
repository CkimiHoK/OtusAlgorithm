from tester import test_task
from module_2.lesson_5_6.shell_sort import shell_sort

if __name__ == "__main__":
    task = shell_sort

    test_task("0_random", task, "shell_random_tests_result.txt")
    test_task("1_digits", task, "shell_digits_tests_result.txt")
    test_task("2_sorted", task, "shell_sorted_tests_result.txt")
    test_task("3_revers", task, "shell_revers_tests_result.txt")
