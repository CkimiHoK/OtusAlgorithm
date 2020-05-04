from tester import test_task
from module_1.lesson_1.tickets import lucky_tickets_binom, lucky_tickets_map

if __name__ == "__main__":
    # task = lucky_tickets_map
    # test_task("2_tickets", task, "test_result_map.txt")

    task = lucky_tickets_binom
    test_task("2_tickets", task, "test_result_binomial.txt")
