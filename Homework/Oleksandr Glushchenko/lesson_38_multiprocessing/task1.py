"""
Task 1. Primes

We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.
Compare the results and performance of each of them.
"""
import math
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


nums = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# for num in nums:
#     print(is_prime(num))


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {"{:.2f}".format(end_time - start_time)} seconds.')
        return result
    return wrapper


@timing_decorator
def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(is_prime, numbers))


@timing_decorator
def filter_primes_processpool(numbers):
    with ProcessPoolExecutor(max_workers=4) as executor:  # max_workers param limits number of CPU cores usage
        return list(executor.map(is_prime, numbers))  # executor.map() returns iterator obj, so I wrapped it in list


@timing_decorator
def filter_primes_for_loop(numbers):
    res = []
    for num in numbers:
        res.append(is_prime(num))
    return res


if __name__ == '__main__':
    print(filter_primes_for_loop(nums))
    print(filter_primes_threadpool(nums))
    print(filter_primes_processpool(nums))  # is_prime func is a CPU-bound task, so ProcessPoolExecutor is way faster
