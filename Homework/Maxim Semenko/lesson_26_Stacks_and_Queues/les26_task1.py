from stack import Stack


def reverse_sequence(sequence):
    my_stack = Stack()
    for char in sequence:
        my_stack.push(char)
    reversed_sequence = ''
    for i in range(my_stack.size()):
        reversed_sequence += my_stack.pop()
    return reversed_sequence


print(reverse_sequence('paparazzi'))
