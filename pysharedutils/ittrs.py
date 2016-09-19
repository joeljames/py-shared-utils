__all__ = [
    'is_iterable',
]


def is_iterable(obj):
    '''
    True if an object is iterable, else False
    '''
    return hasattr(obj, '__iter__')
