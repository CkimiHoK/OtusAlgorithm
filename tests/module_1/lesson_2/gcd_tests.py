from tester import test_task
from module_1.lesson_2.gcd import gcd_by_subtracting, gcd_by_remains, gcd_by_binary_operations

if __name__ == "__main__":
    task = gcd_by_binary_operations
    test_task("2_GCD", task, "gcd_by_binary_operations_tests_result.txt")

    task = gcd_by_remains
    test_task("2_GCD", task, "gcd_by_remains_tests_result.txt")

    task = gcd_by_subtracting
    test_task("2_GCD", task, "gcd_by_subtracting_tests_result.txt")
