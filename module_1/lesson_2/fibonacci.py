def fibonacci_by_recursion(str_array):
    """ Calculate fibonacci number in N position by recursion method """
    import sys
    sys.setrecursionlimit(500000000)

    position = int(str_array[0])

    def get_fibonacci_num(n):  # work to test-08 (next stack overflow)
        return 1 if n <= 2 else get_fibonacci_num(n - 1) + get_fibonacci_num(n - 2)

    def get_next_num(first=1, second=1, cur_position=3):  # work to test-09 (next stack overflow)
        if position <= 2:
            return 1
        if cur_position >= position:
            return first + second
        else:
            cur_position += 1
            return get_next_num(second, first+second, cur_position)

    # result = get_fibonacci_num(position)
    result = get_next_num()
    return str(result)


def fibonacci_by_iterations(str_array):
    """ Calculate fibonacci number in N position by usually iterations """
    position = int(str_array[0])

    a, b = 1, 1
    for _ in range(3, position + 1):
        a, b = b, a + b
    return str(b)


def fibonacci_by_golden_sec(str_array):
    """ Calculate fibonacci number in N position by golden section method """
    position = int(str_array[0])

    if position <= 2:
        return 1

    phi = (1 + (5**0.5)) / 2
    result = (phi ** position - ((1 - phi) ** position)) / (5 ** 0.5)

    return str(int(round(result)))


def fibonacci_by_matrix(str_array):
    """ Calculate fibonacci number in N position by matrix multiply """
    position = int(str_array[0])

    def multiplier(a, b):
        """ Multiplier for 2x2 matrix """
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0],
                 a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    def matrix_power(power):
        """ Raising the matrix to a power """
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = [[1, 0], [0, 1]]

        while power:  # Use binary decomposition
            if power % 2 == 1:
                result_matrix = multiplier(result_matrix, base_matrix)
            base_matrix = multiplier(base_matrix, base_matrix)
            power //= 2
        return result_matrix

    result = matrix_power(position)[1][0]
    return str(result)
