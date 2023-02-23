"""
Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message
"""


class Stack:
    def __init__(self):
        self._items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is already empty!')
        self.size -= 1
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def read_sequence(self, sequence: iter) -> None:
        for item in sequence:
            self.push(item)

    def get_from_stack(self, element):
        for index, item in enumerate(self._items):
            if item == element:
                return self._items.pop(index)
        raise ValueError(f'{element} is not in the stack!')

    def __repr__(self):
        return self._items

    def __str__(self):
        return str(self.__repr__())


seq1 = 'Hello'
stack = Stack()
stack.read_sequence(seq1)
print(f'Initial stack: {stack}')
print(f'Returned element from stack: {stack.get_from_stack("e")}')
print(f'Current stack: {stack}')


class Queue:
    def __init__(self):
        self._items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self._items.insert(0, item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Stack is already empty!')
        self.size -= 1
        return self._items.pop()

    def read_sequence(self, sequence: iter) -> None:
        for item in sequence:
            self.enqueue(item)

    def get_from_queue(self, element):
        for index, item in enumerate(self._items):
            if item == element:
                return self._items.pop(index)
        raise ValueError(f'{element} is not in the queue!')

    def __repr__(self):
        return self._items

    def __str__(self):
        return str(self.__repr__())


queue = Queue()
queue.read_sequence(seq1)
print(f'Initial queue: {queue}')
print(f'Returned element from queue: {queue.get_from_queue("e")}')
print(f'Current queue: {queue}')
