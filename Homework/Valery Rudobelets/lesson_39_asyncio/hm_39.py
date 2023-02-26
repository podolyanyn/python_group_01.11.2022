import asyncio, aiohttp, multiprocessing, time, json


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {"{:.2f}".format(end_time - start_time)} seconds.')
        return result
    return wrapper

# task_1


"""async def fibonacci(n):
    if n < 2:
        return n
    return await fibonacci(n-1) + await fibonacci(n-2)


async def factorial(n):
    if n < 2:
        return 1
    return n * await factorial(n-1)


async def squares(n):
    return n ** 2


async def cubes(n):
    return n ** 3


async def calculate_all(n):
    fib = await fibonacci(n)
    fact = await factorial(n)
    sq = await squares(n)
    cube = await cubes(n)
    return fib, fact, sq, cube


@timing_decorator
async def main():
    tasks = []
    for i in range(1, 11):
        tasks.append(asyncio.create_task(calculate_all(i)))
    results = await asyncio.gather(*tasks)
    fib_list = []
    fact_list = []
    sq_list = []
    cube_list = []
    for result in results:
        fib_list.append(result[0])
        fact_list.append(result[1])
        sq_list.append(result[2])
        cube_list.append(result[3])
    print(f"Fibonacci: {fib_list}")
    print(f"Factorial: {fact_list}")
    print(f"Squares: {sq_list}")
    print(f"Cubes: {cube_list}")

if __name__ == '__main__':
    asyncio.run(main())"""


"""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


if __name__ == '__main__':
    @timing_decorator
    def run_all():
        multiprocessing.freeze_support()

        with multiprocessing.Pool(processes=4) as pool:
            results_fibonacci = pool.map(fibonacci, range(1, 11))
            results_factorial = pool.map(factorial, range(1, 11))
            results_square = pool.map(square, range(1, 11))
            results_cube = pool.map(cube, range(1, 11))

        print("Fibonacci: ", results_fibonacci)
        print("Factorial: ", results_factorial)
        print("Squares: ", results_square)
        print("Cubes: ", results_cube)


    run_all()"""

# task_2

"""@timing_decorator
async def get_comments_async(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=payload) as response:
            data = await response.json()
            comments = []
            time = []
            for comment in data['data']:
                comments.append(comment['body'])
                time.append(comment['utc_datetime_str'])
            my_dict = {key: value for key, value in zip(time, comments)}
            sorted_dict = {key: value for key, value in sorted(my_dict.items())}
            with open("comments.json", "w") as com:
                json.dump(sorted_dict, com, indent=2)


payload = {'subreddit': 'Python'}
url = "https://api.pushshift.io/reddit/comment/search/"

asyncio.run(get_comments_async(url, payload))"""


# task_3

"""HOST = 'localhost'
PORT = 65432


async def handle_client(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()


async def run_server(host, port):
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()

asyncio.run(run_server(HOST, PORT))"""
