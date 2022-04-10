def get_letters() -> [str]:
    '''
    Function that returns a list of letters from a to z and A to Z.
    :return: list list of letters from a to z and A to Z.
    '''
    return [chr(letter) for letter in range(ord('a'), ord('z') + 1)] +\
           [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]


def main():
    print(get_letters())


if __name__ == '__main__':
    main()
