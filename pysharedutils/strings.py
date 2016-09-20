import re

__all__ = [
    'camel_to_snake_case',
    'snake_to_camel_case',
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


def snake_to_camel_case(word):
    """
    :param word: A string that needs to be converted to camel case.

    Convert words to CamelCase.
    Example:
        >>> snake_to_camel_case('snake_case')
        'snakeCase'
    """
    word = re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), word)
    return word[0].lower() + word[1:]
