"""
Task 2

Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."
"""

from task_1 import Stack


def are_brackets_balanced(sequence: iter) -> bool:
    stack = Stack()
    opening_brackets = ['(', '{', '[']

    for bracket in sequence:
        if bracket in opening_brackets:
            stack.push(bracket)
        else:
            if stack.is_empty():
                return False
            current_bracket = stack.pop()
            if current_bracket == '(':
                if bracket != ')':
                    return False
            if current_bracket == '[':
                if bracket != ']':
                    return False
            if current_bracket == '{':
                if bracket != '}':
                    return False

    return True


test1 = '()()()'
test2 = ''  # no brackets == balanced
test3 = '(())'
test4 = '((])'
test5 = ']()'
test6 = '[{()}]'

assert are_brackets_balanced(test1) is True
assert are_brackets_balanced(test2) is True
assert are_brackets_balanced(test3) is True
assert are_brackets_balanced(test4) is False
assert are_brackets_balanced(test5) is False
assert are_brackets_balanced(test6) is True

