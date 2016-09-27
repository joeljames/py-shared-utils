from functools import wraps

__all__ = [
    'singleton',
    'memoize',
    'cached_property',
]


def singleton(func):
    """
    Decorator that creates a singleton instance.
    If the method is called later a cached instance of the method is returned.
    """
    cache = {}

    @wraps(func)
    def getinstance(*args, **kwargs):
        if func not in cache:
            cache[func] = func(*args, **kwargs)
        return cache[func]
    return getinstance


def memoize(func):
    """
    Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned,
    and the method is not reevaluated..
    """
    cache = func.cache = {}

    @wraps(func)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return memoizer


class cached_property(object):
    """
    Decorator that caches the property on the instance.
    Computed only once per instance.
    """

    def __init__(self, func, name=None):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

    def __get__(self, instance, cls=None):
        if instance is None:
            return self
        res = instance.__dict__[self.name] = self.func(instance)
        return res
