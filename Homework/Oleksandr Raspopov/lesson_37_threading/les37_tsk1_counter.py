# A shared counter
# Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and
# for each time increments the value of the counter by 1.
# Create 2 instances of the thread and start them, then join them and check the result of the counter, it should be 200.000, right?
# Run it a couple of times and consider some different reasons why you get the answer that you get.


import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100_000

    def run(self):
        for _ in range(Counter.rounds):
            Counter.counter += 1

inst1 = Counter()
inst2 = Counter()

# title = 'Synchronous Version:'
# print(title)
# inst1.run()
# inst2.run()
# print(inst1.counter)
# print(inst2.counter)


title = 'Race conditions (GIL issue):'
print(title)
inst1.start()
inst2.start()
print(inst1.counter)
print(inst2.counter)


# title = 'Threading with .join() == Synchronous Version:'
# print(title)
# inst1.start()
# inst1.join()
# inst2.start()
# inst2.join()
# print(inst1.counter)
# print(inst2.counter)
