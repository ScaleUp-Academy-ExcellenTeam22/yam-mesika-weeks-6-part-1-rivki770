def my_filter(function, iterable) -> []:
    '''
    function that filters a collection according to a condition function.
    For example:
        function = n < 0.
        iterable = [-2, -1, 0, 1, 2].
        return (-2, -1).
    :param function: condition function.
    :param iterable: collection of items.
    :return: list of items that meet the condition.
    '''
    return [iter for iter in iterable if function(iter)]


def main():
    numbers = [-2, -1, 0, 1, 2]

    negative_numbers = my_filter(lambda n: n < 0, numbers)
    print(tuple(negative_numbers))

    positive_numbers = my_filter(lambda n: n > 0, numbers)
    print(tuple(positive_numbers))


if __name__ == '__main__':
    main()
    