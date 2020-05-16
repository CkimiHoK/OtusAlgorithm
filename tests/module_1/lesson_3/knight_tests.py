from tester import test_task
from module_1.lesson_3.knight import get_knight_moves

if __name__ == "__main__":
    task = get_knight_moves
    test_task("2_knight", task, "knight_tests_result.txt")
