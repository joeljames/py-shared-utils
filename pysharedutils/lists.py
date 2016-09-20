__all__ = [
    'compact_list',
    'force_list',
]


def compact_list(arr):
    """
    :param arr: A list who's falsey values has to be removed.

    Creates an list with all falsey values removed.
    """
    return [value for value in arr if value]


def force_list(obj):
    """
    :param obj: A obj which has to be converted to list.

    Force the given object to be a list, wrapping single objects.
    """
    if obj is None:
        return []
    elif isinstance(obj, str) or not hasattr(obj, '__iter__'):
        return [obj]
    else:
        return list(obj)
