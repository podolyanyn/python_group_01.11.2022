class Stack:
    def __init__(self):
        self.__items = []

    def __repr__(self):
        return self.__items

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

    def get_from_stack(self, element):
        if element not in self.__items:
            raise ValueError(f"{element} is not in the list!")
        return element


my_stack = Stack()
my_stack.push("a")
my_stack.push("b")
my_stack.push("c")
print(my_stack.get_from_stack("b"))
print(my_stack.get_from_stack("a"))
# print(my_stack.get_from_stack("o"))


class Queue:
    def __init__(self):
        self.__items = []

    def __repr__(self):
        return self.__items

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if len(self.__items) < 1:
            return 'Queue is empty!'
        return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return self.__items == []

    def get_from_queue(self, element):
        if element not in self.__items:
            raise ValueError(f"{element} is not in the list!")
        return element


my_queue = Queue()
my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")
print(my_queue.get_from_queue("b"))
print(my_queue.get_from_queue("a"))
# print(my_queue.get_from_queue("o"))
