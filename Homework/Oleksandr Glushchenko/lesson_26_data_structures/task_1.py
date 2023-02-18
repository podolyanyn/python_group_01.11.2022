"""
Task 1

Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
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

    def __repr__(self):
        return self._items

    def __str__(self):
        return str(self.__repr__())


if __name__ == '__main__':
    def reverse_sequence(sequence: iter) -> None:
        stack = Stack()
        for item in sequence:
            stack.push(item)
        print(stack._items[::-1])


    seq1 = [1, 2, 3, 4, 5]
    seq2 = 'hello'
    seq3 = (5, 4, 3, 2, 1)

    reverse_sequence(seq1)
    reverse_sequence(seq2)
    reverse_sequence(seq3)
