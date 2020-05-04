def lucky_tickets_binom(n_str_value):
    """ Count lucky tickets by using binomial coefficient """

    def get_factorial(num, count):
        """ Calculates the factorial via recursion. count - added the feature to restrict factorial size """
        return 1 if num <= 1 or count < 1 else num * get_factorial(num - 1, count - 1)

    def calc_binomial_coeff(n, k):
        """ Calculate binomial coefficient. Reduced numerator by k factorial """
        return get_factorial(n, n - k) // get_factorial(n - k, n - k)

    n_size = int(n_str_value[0])  # Convert string value of N to int

    lucky_tickets_count = 0  # Will contain the final number of lucky tickets
    multiplier = 1
    for series_position in range(n_size):
        n_first = n_size * 2
        k_first = series_position
        n_second = n_size * 11 - series_position * 10 - 1
        k_second = n_size * 9 - series_position * 10
        lucky_tickets_count += calc_binomial_coeff(n_first, k_first) * calc_binomial_coeff(n_second, k_second) * multiplier
        multiplier = -multiplier

    return str(lucky_tickets_count)  # Return string representation


# BAD SOLUTION (too many memory used)
def lucky_tickets_map(n_str_value):
    """ Count lucky tickers by dictionary with unique sums """
    n_size = int(n_str_value[0])  # Convert string value of N to int
    all_tickets = [ticket for ticket in range(10 ** n_size)]  # Generate all tickets numbers from 0 to N

    def get_digits_sum(ticket_number):
        """ Calculate sum of number's digits """
        result = 0
        while ticket_number > 0:
            result += ticket_number % 10
            ticket_number = ticket_number // 10
        return result

    sum_variants = {}  # Dictionary will contain all unique sums (key) with number count (value)
    for ticket in all_tickets:
        digits_sum = get_digits_sum(ticket)
        sum_variants.setdefault(digits_sum, 0)
        sum_variants[digits_sum] += 1

    lucky_tickets_count = 0
    for digits_sum, count in sum_variants.items():
        lucky_tickets_count += count ** 2

    return str(lucky_tickets_count)
