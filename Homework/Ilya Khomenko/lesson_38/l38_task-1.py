from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math

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


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return True


if __name__ == "__main__":
    #Process 26~27s
    start = time.time()
    with ProcessPoolExecutor(len(NUMBERS)) as executor:
        results = executor.map(isprime, NUMBERS)
    end = time.time()
    for num, res in zip(NUMBERS, results):
        print(num, res)
    tm = end - start
    print(tm)

    #Thread  28~48s
    start = time.time()
    with ThreadPoolExecutor(len(NUMBERS)) as executor:
        results = executor.map(isprime, NUMBERS)
    end = time.time()
    for num, res in zip(NUMBERS, results):
        print(num, res)
    tm = end - start
    print(tm)
