import time


def timer(function, *parameters):
    '''
    The function calculates the time it takes for another function to operate with the parameters.
    :param function: function for which we will test the time.
    :param parameters: parameters to move to function.
    :return: The time take to function to work with a parameters.
    '''
    time_start = time.time()
    function(parameters)
    return time.time() - time_start


def main():
    print(timer(print, "Hello"), 'seconds.')
    print(timer(zip, [1, 2, 3], [4, 5, 6]), 'seconds.')


if __name__ == '__main__':
    main()
