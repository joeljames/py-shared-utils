import six

__all__ = [
    'force_bytes',
    'force_str',
]


def force_bytes(value, encoding='utf-8', strings_only=True, errors='strict'):
    """
    :param value: A value which has to be converted into bytes.
    :param encoding: The encoding type. Defaults to `utf-8`
    :param strings_only: A bool, if set to True will ignore
        decoding values which are `None` or `int`
    :param errors: The error level when encoding. Defaults to `strict`

    Forces the value to a str instance, decoding if necessary.
    """
    if isinstance(value, bytes):
        if encoding == 'utf-8':
            return value
        else:
            return value.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and (value is None or isinstance(value, int)):
        return value
    else:
        return value.encode(encoding, errors)


def force_str(value, encoding='utf-8'):
    """
    :param value: A value which has to be converted to a string.

    Forces the value to a str instance, decoding if necessary.
    """
    if six.PY3:
        if isinstance(value, bytes):
            return str(value, encoding)
    return value
