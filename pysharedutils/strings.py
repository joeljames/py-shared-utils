import re

__all__ = [
    'camel_to_snake_case',
    'snake_to_camel_case',
    'equals',
]


def camel_to_snake_case(word):
    """
    :param word: A string that needs to be converted to snake case.

    Converts a camelcase word to snake case.
    Example:
        >>> camel_to_snake_case('camelCase')
        'camel_case'
    """
    word = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', word)
    word = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', word)
    word = word.replace('-', '_')
    return word.lower()


def snake_to_camel_case(word, upper=False):
    """
    :param word: A string that needs to be converted to camel case.
    :param upper: Whether or not to return UpperCamelCase instead of lowerCamelCase

    Convert words to CamelCase.
    Example:
        >>> snake_to_camel_case('snake_case')
        'snakeCase'
    Example:
        >>> snake_to_camel_case('snake_case', upper=True)
        'SnakeCase'
    """
    word = re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), word)
    if upper:
        return word
    else:
        return word[0].lower() + word[1:]


def equals(val1, val2):
    """
    :param val1: A string that has to be compared.
    :param val2: A string that has to be compared.

    Returns True if the two strings are equal, False otherwise.
    The time taken is independent of the number of characters that match.
    For the sake of simplicity, this function executes in constant time only
    when the two strings have the same length. It short-circuits when they
    have different lengths.
    """
    if len(val1) != len(val2):
        return False
    result = 0
    for x, y in zip(val1, val2):
        result |= ord(x) ^ ord(y)
    return result == 0
