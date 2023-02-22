import multiprocessing
import threading
import time, socket, json, requests, math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


start = time.perf_counter()
# task_1


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


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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
        return list(executor.map(isprime, numbers))


@timing_decorator
def filter_primes_processpool(numbers):
    with ProcessPoolExecutor(max_workers=4) as executor:  # max_workers param limits number of CPU cores usage
        return list(executor.map(isprime, numbers))  # executor.map() returns iterator obj, so I wrapped it in list


@timing_decorator
def filter_primes_for_loop(numbers):
    res = []
    for num in numbers:
        res.append(isprime(num))
    return res


if __name__ == '__main__':
    print(filter_primes_for_loop(nums))
    print(filter_primes_threadpool(nums))
    print(filter_primes_processpool(nums))  # is_prime func is a CPU-bound task, so ProcessPoolExecutor is way faster


# task_2

"""payload = {'subreddit': 'Python'}
url = "https://api.pushshift.io/reddit/comment/search/"


def get_comments(url, payload):
    r = requests.get(url, params=payload)
    comments = []
    time = []
    for data in range(len(r.json()["data"])):
        comment = r.json()["data"][data]["body"]
        date = r.json()["data"][data]["utc_datetime_str"]
        comments.append(comment)
        time.append(date)

    my_dict = {keys: values for (keys, values) in zip(time, comments)}
    sorted_dict = {keys: values for keys, values in sorted(my_dict.items())}

    with open("comments.json", "w") as com:
        json.dump(sorted_dict, com, indent=2)


if __name__ == '__main__':
    multiprocessing.freeze_support() # це потрібно для того аби запустити мультипроцесорність на Windows
# на Ubuntu можна обійтися без цього рядка
    with ProcessPoolExecutor() as executor:
        executor.submit(get_comments, url, payload)

finish = time.perf_counter()
print(str(finish-start))"""

# task_3

# HOST = 'localhost'
# PORT = 65432
# ADDR = (HOST, PORT)
#
#
# def handle_client(conn, addr):
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
#
#
# if __name__ == '__main__':
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind(ADDR)
#         s.listen()
#         while True:
#             conn, addr = s.accept()
#             process = multiprocessing.Process(target=handle_client, args=(conn, addr))
#             process.start()



