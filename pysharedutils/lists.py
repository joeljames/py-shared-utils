__all__ = [
    'compact_list',
]


def compact_list(arr):
    """
    :param arr: A list who's falsey values has to be removed.

    Creates an list with all falsey values removed.
    """
    return [value for value in arr if value]
