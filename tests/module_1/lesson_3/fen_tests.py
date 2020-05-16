from tester import test_task
from module_1.lesson_3.fen import convert_fen_to_bbd

if __name__ == "__main__":
    task = convert_fen_to_bbd
    test_task("3_fen", task, "fen_tests_result.txt")
