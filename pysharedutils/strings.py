import six

__all__ = [
    'force_str',
]


def force_str(value, encoding='utf-8'):
    """
    Forces the value to a str instance, decoding if necessary.
    """
    if six.PY3:
        if isinstance(value, bytes):
            return str(value, encoding)
    return value
