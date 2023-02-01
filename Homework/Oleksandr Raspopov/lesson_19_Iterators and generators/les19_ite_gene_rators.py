print('> > > Task 1 - custom enumerate:\n')
# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

class Enumerate:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            self.start += 1
            return self.start-1, self.iterable[self.index-1]
        else:
            raise StopIteration


def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=1)), '-> built-in enumerate()')
print(list(Enumerate(seasons, start=1)), '-> custom class Enumerate')
print(list(with_index(seasons, start=1)), '-> custom enumerate aka with_index()')


print('\n> > > Task 2 - custom range:\n')
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function


def in_range(start, stop, step=1):
    i = 0
    r = start + step * i
    if step > 0:
        while r < stop:
            yield r
            i += 1
            r = start + step * i
    elif step < 0:
        while r > stop:
            yield r
            i += 1
            r = start + step * i
    else:
        raise ValueError


print(list(range(0, 30, 5)), '-> built-in range()')
print(list(in_range(0, 30, 5)), '-> custom range aka in_range()')
print(list(range(-5, -30, -5)), '-> built-in range()')
print(list(in_range(-5, -30, -5)), '-> custom range aka in_range()')

print('\n> > > Task 3 - own iterable\n')
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
# Створіть власну реалізацію ітератора, який можна було б використовувати всередині циклу for-in.
# Також додайте логіку отримання елементів, використовуючи синтаксис квадратних дужок
# (тобто iterator[i], де iterator власне ітератор, i - індекс елемента колекції, на яку "натравлений" ітератор).


class OwnIterable:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.iterable):
            return self.iterable[self.index]
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.iterable[item]


my_tuple = (1, 2, 3, 4)

iter_tuple = OwnIterable(my_tuple)
print('Test of iter_tuple[1]:', iter_tuple[1])
for i in iter_tuple:
    print(i)




