__all__ = [
    'cached_property',
]


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
