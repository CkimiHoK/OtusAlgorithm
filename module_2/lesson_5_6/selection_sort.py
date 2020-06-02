def selection_sort(str_array):
    """ Sort array with selection algorithm. """
    count = int(str_array[0])
    collection = [int(element) for element in str(str_array[1]).split(' ')]

    for i in range(count):
        swap_exists = False
        index = i
        min_element = collection[index]
        for j in range(i + 1, count):
            if min_element > collection[j]:
                swap_exists = True
                index = j
                min_element = collection[index]

        if index != i:
            collection[i], collection[index] = collection[index], collection[i]

        if not swap_exists:
            break

    return ' '.join(map(str, collection))
