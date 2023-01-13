def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    Traceback (most recent call last):
        ...
    ValueError: input string must be digit string
    """
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string[0])
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])
