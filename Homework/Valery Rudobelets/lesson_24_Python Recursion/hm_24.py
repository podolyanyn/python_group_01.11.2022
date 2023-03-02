import pytest
from typing import Union, Optional

# task_1


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 1:
        return x
    elif exp == 0:
        return 1
    elif exp < 0:
        raise ValueError("This function works only with exp > 0")
    else:
        return x * to_power(x, exp-1)


# task_2

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1:
        return True
    else:
        return is_palindrome(looking_str[index]) == is_palindrome(looking_str[index-1])

# task_3

def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError("This function works only with positive integers")
    else:
        return a + mult(a, n-1)

# task_4


def reverse(input_str: str) -> str:
    if not input_str:
        return input_str
    return reverse(input_str[1:]) + input_str[0]

# task_5


def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    elif len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


# test


def test_to_power():
    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
    with pytest.raises(ValueError, match=r"This function works only with exp > 0"):
        to_power(2, -1)


def test_is_palindrome():
    assert is_palindrome("mom")
    assert is_palindrome("sassas")
    assert is_palindrome("o")


def test_mult():
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
    with pytest.raises(ValueError, match=r"This function works only with positive integers"):
        mult(2, -4)


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("o") == "o"


def test_sum_of_digits():
    assert sum_of_digits('26') == 8
    assert sum_of_digits('22') == 4
    with pytest.raises(ValueError, match=r"input string must be digit string"):
        sum_of_digits("test")

