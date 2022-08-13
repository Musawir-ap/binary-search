import random
import time


def naive_search(l, target):
    for i in range(len(l)):
        if i == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2
    if target == midpoint:
        return midpoint
    elif target < midpoint:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > midpoint
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for i in range(len(sorted_list)):
        naive_search(sorted_list, i)
    end = time.time()
    print('naive search : ', (end - start), 's')

    start = time.time()
    for i in range(len(sorted_list)):
        binary_search(sorted_list, i)
    end = time.time()
    print('binary search : ', (end - start), 's')
