import time

def pair_with_sum(_array, _sum):
    """
    Given a sorted array of integers and a sum, returns a pair of numbers that have the requested sum, if any.
    :param _array: A sorted array of integers
    :param _sum: The sum of the pair we want to find
    :return: A tuple with a pair that have the requested sum or the string 'No pair is found' if no pair is found.
    """

    # If the given sum is smaller of the sum of the two first items or bigger of the sum of the two last items
    # there is no need to search further, there is no pair with the given sum
    if _sum < _array[0] + _array[1] or _sum > _array[-1] + _array[-2]:
        return 'No pair is found'

    # initialize i and j to point to the first and last item respectively.
    i, j = 0, len(_array)-1

    while i < j:
        my_sum = _array[i] + _array[j]

        if my_sum == _sum:
            return _array[i], _array[j]
        elif my_sum < _sum:
            i += 1
        else:
            j -= 1
    else:
        return 'No pair is found'



if __name__ == "__main__":
    given_array = [3, 3, 4, 6, 7, 10, 12, 23, 23, 32]

    start_timer = time.time()

    print(pair_with_sum(given_array, 42))

    stop_timer = time.time()

    print('\nElapsed time: ', stop_timer - start_timer)