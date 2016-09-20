import collections

__all__ = [
    'get_object_by_source',
]


def get_object_by_source(obj, source, allow_blank_source=False):
    """
    :param obj: A python object or a python dict.
    :param source: The source name which has to be extracted from
        the object. You can use dot syntax to specify nested source.
    :param allow_blank_source: A bool, if set to `True` it catches
        `AttributeError` and returns `None` if the source
        does not exist on the obj.

    Tries to get the object by source.
    Similar to Python's `getattr(obj, source)`, but takes a dot separated
    string for source to get source from nested obj, instead of a single
    source field. Also, supports getting source form obj where obj is a
    dict type.

    Example:
        >>> obj = get_object_by_source(
            object,
            source='user.username')
    """
    try:
        if isinstance(obj, collections.Mapping):
            if '.' in source:
                for source in source.split('.'):
                    obj = obj.get(source)
            else:
                obj = obj.get(source)
        else:
            if '.' in source:
                for source in source.split('.'):
                    obj = getattr(obj, source)
            else:
                obj = getattr(obj, source)
    except AttributeError:
        if not allow_blank_source:
            raise
        obj = None
    return obj
