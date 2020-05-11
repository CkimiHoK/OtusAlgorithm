from tester import test_task
from module_1.lesson_2.power import power_by_iterations, power_by_exponent_of_two, power_by_binary_decomposition

if __name__ == "__main__":
    task = power_by_iterations
    test_task("3_Power", task, "power_by_iterations_tests_result.txt")

    task = power_by_exponent_of_two
    test_task("3_Power", task, "power_by_exponent_of_two_tests_result.txt")

    task = power_by_binary_decomposition
    test_task("3_Power", task, "power_by_binary_decomposition_tests_result.txt")
