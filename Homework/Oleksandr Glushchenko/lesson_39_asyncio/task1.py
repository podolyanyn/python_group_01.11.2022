"""
Task 1. Practice asynchronous code
Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using 'asyncio.gather' for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.
"""
import asyncio
import time
import multiprocessing


def async_timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = asyncio.run(func(*args, **kwargs))
        end_t = time.time()
        exec_t = (end_t - start_t) * 1000
        print(f'Asyncio execution time: {exec_t:.2f} ms')
        return result
    return wrapper


def mp_timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        end_t = time.time()
        exec_t = (end_t - start_t) * 1000
        print(f'Multiprocessing execution time: {exec_t:.2f} ms')
        return result
    return wrapper


# ASYNC VERSION
async def calculate_async(n: int) -> tuple:

    async def fibonacci(n):
        if n <= 1:
            return n
        return await fibonacci(n - 1) + await fibonacci(n - 2)

    async def factorial(n):
        if n == 0:
            return 1
        return n * await (factorial(n - 1))

    async def square(n):
        return n * n

    async def cubic(n):
        return n * n * n

    fib = await fibonacci(n)
    fact = await factorial(n)
    sq = await square(n)
    cub = await cubic(n)
    return fib, fact, sq, cub


@async_timing_decorator
async def main_async(number):
    tasks = []
    for i in range(1, number + 1):
        tasks.append(asyncio.ensure_future(calculate_async(i)))
    results = await asyncio.gather(*tasks)
    fib_list = [result[0] for result in results]
    fact_list = [result[1] for result in results]
    square_list = [result[2] for result in results]
    cubic_list = [result[3] for result in results]
    print(f'Fibonacci list: {fib_list}')
    print(f'Factorial list: {fact_list}')
    print(f'Square list: {square_list}')
    print(f'Cubic list: {cubic_list}')


# MULTIPROCESSING VERSION

def calculate_mp(n: int) -> tuple:
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def factorial(n):
        if n == 0:
            return 1
        return n * (factorial(n - 1))

    def square(n):
        return n * n

    def cubic(n):
        return n * n * n

    fib = fibonacci(n)
    fact = factorial(n)
    sq = square(n)
    cub = cubic(n)
    return fib, fact, sq, cub


@mp_timing_decorator
def main_mp(number):
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(calculate_mp, range(1, number + 1))
    pool.close()
    pool.join()
    fib_list = [result[0] for result in results]
    fact_list = [result[1] for result in results]
    square_list = [result[2] for result in results]
    cubic_list = [result[3] for result in results]
    print(f'Fibonacci list: {fib_list}')
    print(f'Factorial list: {fact_list}')
    print(f'Square list: {square_list}')
    print(f'Cubic list: {cubic_list}')


if __name__ == '__main__':
    main_async(10)
    main_mp(10)

# Async code is faster than multiprocessing code with a list containing 10 ints (or less),
# but starting from a list with ~ 30 ints, multiprocessing does a much better job, 'cause these operations are
# CPU bound (async is better for I/O bound tasks involving waiting)
