class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) < 1:
            return 'Stack is empty!'
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return self.__items == []

    def peek(self):
        return self.__items[-1]

    def __repr__(self):
        return self.__items
