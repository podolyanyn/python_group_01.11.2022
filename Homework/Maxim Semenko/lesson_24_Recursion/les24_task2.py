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
    if len(looking_str) == 1 or len(looking_str) == 0:
        return True
    if looking_str[index] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])