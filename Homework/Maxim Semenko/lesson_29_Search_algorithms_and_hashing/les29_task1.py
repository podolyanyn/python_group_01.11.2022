import timeit

def recursive_binary_search(array, low, high, item):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            return recursive_binary_search(array, low, mid - 1, item)
        else:
            return recursive_binary_search(array, mid + 1, high, item)
    else:
        return False


def fibonacci_search(array, item):
    size = len(array)
    start = -1
    found = False
    f0 = 0
    f1 = 1
    f2 = 1
    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while f2 > 1:
        index = min(start + f0, size - 1)
        if array[index] < item:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > item:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            found = True
            return found
    if f1 and array[size - 1] == item:
        return size - 1
    return found


if __name__ == "__main__":
    rec_bin_timer = timeit.timeit(
        stmt="recursive_binary_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 0, 7, 6)",
        number=100000,
        setup="from __main__ import recursive_binary_search"
    )
    print(rec_bin_timer)

    fib_timer = timeit.timeit(
        stmt="fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100000,
        setup="from __main__ import fibonacci_search"
    )
    print(fib_timer)