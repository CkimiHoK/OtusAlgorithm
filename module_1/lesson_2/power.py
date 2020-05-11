def power_by_iterations(str_array):
    """ Calculate power of number by using usually iterations """
    base = float(str_array[0])
    power = int(str_array[1])

    result = 1.0
    for _ in range(power):
        result *= base
    return str(round(result, 11))


def power_by_exponent_of_two(str_array):
    """ Calculate power of number by using exponents of 'two' """
    base = float(str_array[0])
    power = int(str_array[1])

    result = 1.0
    if power != 0:
        used_power = 1
        calc_value = base
        while used_power * 2 <= power:
            used_power *= 2
            calc_value *= calc_value

        result = calc_value
        for _ in range(power - used_power):
            result *= base

    return str(round(result, 11))


def power_by_binary_decomposition(str_array):
    """ Calculate power of number by binary decomposition of the exponent """
    base = float(str_array[0])
    power = int(str_array[1])

    result = 1.0
    while power > 1:
        if power % 2 == 1:
            result *= base
        base *= base
        power //= 2

    if power > 0:
        result *= base

    return str(round(result, 11))
