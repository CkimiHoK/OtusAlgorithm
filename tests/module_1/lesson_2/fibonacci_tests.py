from tester import test_task
from module_1.lesson_2.fibonacci import fibonacci_by_recursion, fibonacci_by_iterations, fibonacci_by_golden_sec, \
    fibonacci_by_matrix, fibonacci_by_matrix_refactoring

if __name__ == "__main__":
    task = fibonacci_by_recursion
    test_task("4_Fibo", task, "fibonacci_by_recursion_tests_result.txt")

    task = fibonacci_by_iterations
    test_task("4_Fibo", task, "fibonacci_by_iterations_tests_result.txt")

    task = fibonacci_by_golden_sec
    test_task("4_Fibo", task, "fibonacci_by_golden_sec_tests_result.txt")

    task = fibonacci_by_matrix
    test_task("4_Fibo", task, "fibonacci_by_matrix_tests_result.txt")

    task = fibonacci_by_matrix_refactoring
    test_task("4_Fibo", task, "fibonacci_by_matrix_ref_tests_result.txt")
