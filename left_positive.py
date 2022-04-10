def get_positive_numbers(string_of_numbers: str) -> [int]:
    '''
    The function filters numbers, and return only positive numbers.
    For example:
        input: '-5, 5, -4, 4, -3, 3'.
        return: [5, 4, 3].
    :param string_of_numbers: string of numbers, split by ','.
    :return: list of int, of the positive numbers.
    '''
    list_of_numbers = string_of_numbers.split(',')
    return [int(number) for number in list_of_numbers if int(number) > 0]


def main():
    string_of_numbers = input("Please, enter the list of numbers. format: {x, x, ... ,x}:\n")
    print(get_positive_numbers(string_of_numbers))


if __name__ == '__main__':
    main()
