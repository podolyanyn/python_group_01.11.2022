# #############################################
# # All tasks should be solved using recursion
# #############################################


# Task 1
from typing import Union
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    Traceback (most recent call last):
    ValueError: This function works only with exp > 0.
    """
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError('This function works only with exp > 0.')
    else:
        exp -= 1
        return x * to_power(x, exp)


# Task 2

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    if len(looking_str) == 1:
        return True
    elif looking_str[0] != looking_str[-1]:
        return False
    index += 1
    return is_palindrome(looking_str[index:-1], index)


# Task 3

def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    Traceback (most recent call last):
    ValueError: This function works only with postive integers
    """
    if a < 0 or n < 0:
        raise ValueError("This function works only with postive integers")
    elif n == 1:
        return a
    return a * mult(n, 1)


# Task 4

def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) == 1:
        return input_str[0]
    return input_str[-1] + reverse(input_str[:-1])


# Task 5

def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    Traceback (most recent call last):
    ValueError: input string must be digit string
    """
    try:
        int(digit_string)
        if len(digit_string) == 1:
            return int(digit_string)
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])
    except ValueError:
        raise ValueError('input string must be digit string')
