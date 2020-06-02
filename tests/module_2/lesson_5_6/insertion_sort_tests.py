from tester import test_task
from module_2.lesson_5_6.insertion_sort import insertion_sort

if __name__ == "__main__":
    task = insertion_sort

    test_task("0_random", task, "insertion_random_tests_result.txt")
    test_task("1_digits", task, "insertion_digits_tests_result.txt")
    test_task("2_sorted", task, "insertion_sorted_tests_result.txt")
    test_task("3_revers", task, "insertion_revers_tests_result.txt")
