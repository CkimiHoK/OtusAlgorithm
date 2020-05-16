from tester import test_task
from module_1.lesson_3.king import get_king_moves

if __name__ == "__main__":
    task = get_king_moves
    test_task("1_king", task, "king_tests_result.txt")
