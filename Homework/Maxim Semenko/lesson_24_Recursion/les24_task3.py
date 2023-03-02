def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    Traceback (most recent call last):
        ...
    ValueError: This function works only with positive integers
    """
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if n < 1:
        return 0
    return a + mult(a, n - 1)