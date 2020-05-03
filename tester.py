import os
import time

log_file_name = "tests_result.txt"


def test_task(path, task):
    all_files = []
    for address, directories, files in os.walk(path):
        for file in files:
            all_files.append(os.path.join(address, file))

    test_cases = [file for file in all_files if file.endswith('.in')]

    result_log = ''
    for test_case in test_cases:
        with open(test_case, 'r') as case_input:
            lines = [line.strip() for line in case_input.readlines()]

            start_time = time.time()
            task_result = task(lines)
            end_time = time.time()

            is_test_success = False
            try:
                with open(test_case.replace('.in', '.out'), 'r') as case_output:
                    expected_result = case_output.read().strip()
                    is_test_success = task_result == expected_result
                    result_log += f'Test ({test_case}). {str(is_test_success).upper()} (' \
                        f'Task result: {task_result} ' \
                        f'Expected: {expected_result}. ' \
                        f'Time: {end_time - start_time})\n'
            except IOError:
                expected_result = "*Can't found test case output file*"
                result_log += f'Test ({test_case}). {is_test_success} ' \
                    f'Task result: {task_result} ' \
                    f'Expected: {expected_result}. ' \
                    f'Time: {end_time - start_time})\n'

    try:
        print(result_log)
        with open(os.path.join(path, log_file_name), 'w') as log:
            log.write(result_log)
    except IOError as e:
        print(f"Can't write log to file. Error: {str(e)}")
