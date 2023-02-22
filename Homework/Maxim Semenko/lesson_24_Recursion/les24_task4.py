def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) == 1:
        return input_str
    return reverse(input_str[1:]) + reverse(input_str[0])