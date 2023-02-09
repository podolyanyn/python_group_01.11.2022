#Task-1
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
    for item in iterable:
        yield (start, item)
        start += 1


x = ['a','b','c']
print(list(with_index(x,0)))

#Task-2
def in_range(start, step=None, end=None):
    if step == None and end == None:
        start, step, end = 0, 1, start
        while start < end:
            yield start
            start += step
    elif end == None:
        start, step, end = start, 1, step
        while start < end:
            yield start
            start += step
    while start < end:
        yield start
        start += step

l = []
for i in in_range(1, 10, 200):
    l.append(i)


print(l)


#Task-3
class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high
        self.my = []

    def __iter__(self):
        return self

    def __next__(self): 
        self.current += 1
        if self.current < self.high:
            self.my.append(self.current)
            return self.my
        raise StopIteration      

    def __getitem__(self, ind):
        
        cls = type(self)

        if isinstance(ind, str):
            if ind in self._comp:
                return cls({ind:self._comp[ind]})
            else:
                raise KeyError(f'No such index: {ind}')
     
        elif isinstance(ind, int): 
            return cls(self._to_dict([self._comp_map[ind]]))
        
        elif isinstance(ind, slice):
            return cls(self._to_dict(self._comp_map[ind]))
                
        else:
            raise TypeError(f"{cls.__name__} indices must be integers, slices or strings")




for c in Counter(3,9):
    data = c

print(data)
print(data[0])










