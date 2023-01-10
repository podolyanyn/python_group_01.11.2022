# task_1

def with_index(iterable, start=0):
    index = start
    for element in iterable:
        yield index, element
        index += 1


class WithIndex:

    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.iterable):
                raise StopIteration
        index = self.start
        self.start += 1
        return index, self.iterable[index]


lst = [1, 2, 3, 4]

windex = WithIndex(lst, 1)

# for num in windex:
#     print(num)

# task_2


def in_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


class InRange:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current


inrange = in_range(0, 20, 10)
# inrange = InRange(0, 20, 10)


# for i in inrange:
    # print(i)
# print(type(inrange))

# task_3


class BetterRange:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __getitem__(self, item):
        b = list(BetterRange(self.start, self.end, self.step))
        return b[item]

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current


better = BetterRange(1, 20)


print(better[0])

# for i in better:
    # print(i)