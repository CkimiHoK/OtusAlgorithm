def gcd_by_subtracting(str_array):
    """ Calculate GCD using Euclidean algorithm by subtracting """
    a = int(str_array[0])
    b = int(str_array[1])
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return str(a)


def gcd_by_remains(str_array):
    """ Calculate GCD using Euclidean algorithm by remains """
    a = int(str_array[0])
    b = int(str_array[1])
    while b != 0:
        a, b = b, a % b
    return str(a)


def gcd_by_binary_operations(str_array):
    """ Calculate GCD using Binary algorithm """
    a = int(str_array[0])
    b = int(str_array[1])

    if a == 0:
        return b
    elif b == 0:
        return a

    result = 1
    while a != b:
        if a & 1 and b & 1:  # both - odd
            if a > b:
                a, b = (a - b) >> 1, b
            else:
                a, b = (b - a) >> 1, a
        elif a & 1:  # only a - odd
            b >>= 1
        elif b & 1:  # only b - odd
            a >>= 1
        else:  # both - even
            a, b, result = a >> 1, b >> 1, result << 1

    result *= a
    return str(result)
