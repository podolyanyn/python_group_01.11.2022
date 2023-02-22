from stack import Stack

open_symbols = ["[", "{", "("]
close_symbols = ["]", "}", ")"]


def is_balanced(sequence):
    my_stack = Stack()
    for char in sequence:
        if char in open_symbols:
            my_stack.push(char)
        elif char in close_symbols:
            index = close_symbols.index(char)
            if my_stack.size() > 0 and open_symbols[index] == my_stack.peek():
                my_stack.pop()
            else:
                return "Unbalanced"
    if my_stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(is_balanced("{[()]}"))
print(is_balanced("{[]]]])"))
