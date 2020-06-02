def bubble_sort(str_array):
    """ Sort array with bubble algorithm. """
    count = int(str_array[0])
    collection = [int(element) for element in str(str_array[1]).split(' ')]

    for i in range(count):
        swap_exists = False
        for j in range(count - i - 1):
            if collection[j] > collection[j + 1]:
                swap_exists = True
                collection[j],  collection[j + 1] = collection[j + 1],  collection[j]

        if not swap_exists:
            break

    return ' '.join(map(str, collection))
