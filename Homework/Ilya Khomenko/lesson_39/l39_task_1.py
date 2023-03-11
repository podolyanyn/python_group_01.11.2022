import asyncio
from functools import wraps
import time
import multiprocessing


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper





async def fib(num):
    r = []
    first = 1
    second = 1
    for n in num:
        r.append(first)
        first, second = second, first + second
        await asyncio.sleep(0)
    return r




async def fac(num):
    res = []
    for n in num:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)
        await asyncio.sleep(0)
    return res

async def square(num):
    r = []
    for n in num:
        r.append(n**2)
        await asyncio.sleep(0)
    return r

async def cube(num):
    r = []
    for n in num:
        r.append(n**3)
        await asyncio.sleep(0)
    return r



def fib_1(nums):
    r = []
    first = 1
    second = 1
    for n in nums:
        r.append(first)
        first, second = second, first + second
    return r

def fac_1(num):
    res = []
    for n in num:
        for i in range(n-1, 1, -1):
            n *= i
        res.append(n)

    return res

def square_1(num):
    return [(n**2) for n in num]

def cube_1(num):
    return [(n**3) for n in num]


def fib_2(num):
    r = []
    first = 1
    second = 1
    for n in num:
        r.append(first)
        first, second = second, first + second
    return r

def fac_2(num):
    r = []
    f = 1
    for i in range(2,num+1):
        f *=i
        r.append(f)
    return r


def square_2(num):
    return [(n**2) for n in num]

def cube_2(num):
    return [(n**3) for n in num]


@timeit
async def main():
    output = await asyncio.gather(fac(numbers),fib(numbers),square(numbers),cube(numbers))



@timeit
def main_1():
    output = [fac_1(numbers),fib_1(numbers),square_1(numbers),cube_1(numbers)]


funcs = [fac_2, fib_2, square_2, cube_2]

@timeit
def main_2():
    with multiprocessing.Pool(4) as pool:
        results = [pool.apply_async(fn, (numbers,)) for fn in funcs]

if __name__ == '__main__':
    numbers = [_ for _ in range(1, 9000)]
    #Asynchronous 
    asyncio.run(main())
    #Synchronous
    main_1()
    #Pool
    main_2() 


#Якщо задати список довжиною в 9000 цифр то перевагу отримує асинхронний варіант віна зайняв 0.00 секунд
# в той час як синхронний цілих 50 секунд  а Pool зайняв всього 0.03 секунди отже вожна зробити висновок що для обчислення великих значеннях краще використовувати паралельність