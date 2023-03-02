import asyncio
import time
import multiprocessing


async def factorial1(nums):
    res = []
    for n in nums:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
        await asyncio.sleep(0)
    return res


async def fibonacci1(nums):
    res = []
    first = 1
    second = 1
    for n in nums:
        res.append(first)
        first, second = second, first + second
        await asyncio.sleep(0)
    return res


async def square1(nums):
    res = []
    for n in nums:
        res.append(n ** 2)
        await asyncio.sleep(0)
    return res


async def cubic1(nums):
    res = []
    for n in nums:
        res.append(n ** 3)
        await asyncio.sleep(0)
    return res


async def main1():
    res = await asyncio.gather(factorial1(numbers), fibonacci1(numbers), square1(numbers), cubic1(numbers))
    # print(res)

# -------------------------------------------------

def factorial2(nums):
    res = []
    for n in nums:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
    return res


def fibonacci2(nums):
    res = []
    first = 1
    second = 1
    for n in nums:
        res.append(first)
        first, second = second, first + second
    return res


def square2(nums):
    res = []
    for n in nums:
        res.append(n ** 2)
    return res


def cubic2(nums):
    res = []
    for n in nums:
        res.append(n ** 3)
    return res


def main2():
    res = [factorial2(numbers), fibonacci2(numbers), square2(numbers), cubic2(numbers)]
    # print(res)

# ------------------------------------------------------------------

def factorial3(nums):
    res = []
    for n in nums:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
    return res


def fibonacci3(nums):
    res = []
    first = 1
    second = 1
    for n in nums:
        res.append(first)
        first, second = second, first + second
    return res


def square3(nums):
    res = []
    for n in nums:
        res.append(n ** 2)
    return res


def cubic3(nums):
    res = []
    for n in nums:
        res.append(n ** 3)
    return res


funcs = [fibonacci3, factorial3, square3, cubic3]


def main3_1():
    start = time.time()
    with multiprocessing.Pool(4) as pool:
        results = [pool.apply_async(fn, (numbers,)) for fn in funcs]
        # print([result.get() for result in results])
    print(time.time() - start)


if __name__ == '__main__':

    numbers = [n for n in range(1, 900)]

    print('Asynchronous execution')
    start = time.perf_counter()
    asyncio.run(main1())
    print(time.perf_counter() - start)

    print('\nSynchronous execution')
    start = time.perf_counter()
    main2()
    print(time.perf_counter() - start)

    print('\nPool of processes')
    start = time.perf_counter()
    main3_1()
    print(time.perf_counter() - start)

# Висновок: ефективність в даному випадку сильно залежить від розміру списку, який ми передаємо.
# Оскільки ми робимо обчислення, то синхронний та асинхронний код майже не відрізняються по часу виконання.
# Хоча на дуже малих значеннях синхронний працює швидше.
# Починаючи з довжини списку у 800 паралельність показує свою ефективність і далі розрив стає дуже помітний.
