from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math as m

NUMBERS = [
    2,                 # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,                 # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,                 # prime
]


def prime(n):
    for i in range(2, int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":

    # Processes - 37 s
    start = time.time()
    with ProcessPoolExecutor(len(NUMBERS)) as executor:
        results = executor.map(prime, NUMBERS)
    end = time.time()
    for num, res in zip(NUMBERS, results):
        print(num, res)
    tm = end - start
    print(tm)

    # Threads - 61 s
    start = time.time()
    with ThreadPoolExecutor(len(NUMBERS)) as executor:
        results = executor.map(prime, NUMBERS)
    end = time.time()
    for num, res in zip(NUMBERS, results):
        print(num, res)
    tm = end - start
    print(tm)
