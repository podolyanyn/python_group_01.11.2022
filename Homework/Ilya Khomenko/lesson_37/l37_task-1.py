import threading



class Counter(threading.Thread):
    count = 0
    r = 100000


    def start(self):
        for _ in range(Counter.r):
            Counter.count +=1



thr1 = Counter()
thr2 = Counter()

thr1.start()
thr2.start()

thr1.join()
thr2.join()

print(thr1.count,thr2.count)