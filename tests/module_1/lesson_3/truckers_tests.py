from tester import test_task
from module_1.lesson_3.truckers import get_figures_moves

if __name__ == "__main__":
    task = get_figures_moves
    test_task("4_truckers", task, "truckers_tests_result.txt")
