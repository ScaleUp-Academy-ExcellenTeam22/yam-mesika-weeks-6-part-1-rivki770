def full_names(first_names: [str], last_names: [str], min_len=0) -> [str]:
    '''
    Function that connects names using 2 lists, of first names and last names.
    It returns the names above a given length.
    For example:
        first_names = ['avi', 'moshe', 'yaakov'].
        last_names = ['cohen', 'levi', 'mizrahi'].
        nim_len = 10.
        return: ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
                              'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'].
    :param first_names: list of first names.
    :param last_names: list of last names.
    :param min_len: minimum length for full name.
    :return: list of the full names.
    '''
    first_names = [name[:1].upper() + name[1:] for name in first_names]
    last_names = [name[:1].upper() + name[1:] for name in last_names]
    return [first_name + " " + last_name for first_name in first_names for last_name in last_names
            if len(first_name + " " + last_name) >= min_len]


def main():
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names))
    print(full_names(first_names, last_names, 10))


if __name__ == '__main__':
    main()
