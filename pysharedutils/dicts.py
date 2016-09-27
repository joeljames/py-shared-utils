import six
import collections

from pysharedutils.strings import (
    camel_to_snake_case,
    snake_to_camel_case
)

__all__ = [
    'ObjectDict',
    'MultiDict',
    'compact_dict',
    'merge_dicts',
    'snake_case_dict_keys',
    'camel_case_dict_keys',
]


def _wrap(val):
    if isinstance(val, collections.Mapping):
        return ObjectDict(val)
    if isinstance(val, list):
        return [_wrap(element) for element in val]
    return val


class ObjectDict(object):
    """
    Helper class that makes a dictionary behave like an object,
    with attribute-style access (read and write).

    Example:
        >>> o = ObjectDict({'a': 1, 'b': 2})
        >>> o.a
        1
        >>> o.c
        AttributeError: No such attribute: c
    """

    def __init__(self, d):
        # assign the inner dict manually to prevent __setattr__ from firing
        # if not it will result in RuntimeError:
        # maximum recursion depth exceeded
        super(ObjectDict, self).__setattr__('_d', d)

    def __contains__(self, key):
        return key in self._d

    def __nonzero__(self):
        return bool(self._d)
    __bool__ = __nonzero__

    def __eq__(self, other):
        if isinstance(other, ObjectDict):
            return other._d == self._d
        return other == self._d

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        r = repr(self._d)
        if len(r) > 60:
            r = r[:60] + '...}'
        return r

    def __iter__(self):
        return iter(self._d)

    def __len__(self, d):
        return len(self._d)

    def __getstate__(self):
        return (self._d, )

    def __dir__(self):
        return list(self._d.keys())

    def __getattr__(self, name):
        if name in self._d:
            return _wrap(self._d[name])
        else:
            raise AttributeError(
                'No such attribute: %s' % (name)
            )

    def __setattr__(self, name, value):
        self._d[name] = value

    def __delattr__(self, name):
        if name in self._d:
            del self._d[name]
        else:
            raise AttributeError(
                'No such attribute: %s' % (name)
            )

    def __getitem__(self, key):
        return _wrap(self._d[key])

    def __setitem__(self, key, value):
        self._d[key] = value

    def __delitem__(self, key):
        del self._d[key]

    def to_dict(self):
        return self._d


class MultiDict(dict):

    def getlist(self, key):
        return self[key] if type(self[key]) == list else [self[key]]

    def __repr__(self):
        return type(self).__name__ + '(' + dict.__repr__(self) + ')'


def compact_dict(obj):
    """
    :param obj: A dict who's falsey values has to be removed.

    Creates an dict with all falsey values removed.
    """
    output = {}
    for key, value in six.iteritems(obj):
        element = None
        if isinstance(value, collections.Mapping):
            element = compact_dict(value)
        elif isinstance(value, list):
            arr = []
            for i in value:
                element = compact_dict(i)
                arr.append(element)
            element = arr
        elif value:
            element = value
        if element:
            output[key] = element
    return output


def merge_dicts(*dicts):
    """
    Merges all of the given dicts together without mutations.
    """
    result = {}
    for d in dicts:
        if isinstance(d, collections.Mapping):
            result = dict(result, **d)
    return result


def snake_case_dict_keys(obj):
    """
    :param obj: A dict who's keys has to
        be converted from camel case to snake case.

    Maps the keys of the dict from camelCase to snake_case.
    Example:
        >>> snake_case_dict_keys({'camelCase': 'camel_case'})
        {'camel_case': 'camel_case'}
    """
    output = {}
    for k, v in six.iteritems(obj):
        if isinstance(v, list):
            value_list = v
            arr = []
            for value in value_list:
                if isinstance(value, dict):
                    value = snake_case_dict_keys(value)
                arr.append(value)
            element = arr
        elif isinstance(v, dict):
            element = snake_case_dict_keys(v)
        else:
            element = v

        if isinstance(k, six.string_types):
            key = camel_to_snake_case(k)
        else:
            key = k

        output[key] = element
    return output


def camel_case_dict_keys(obj):
    """
    :param obj: A dict who's keys has to
        be converted from snake case to camel case.

    Maps the keys of the dict from snake case to camel case.
    Example:
        >>> camel_case_dict_keys({'snake_case': 'snake_case'})
        {'snakeCase': 'snake_case'}
    """
    output = {}
    for k, v in six.iteritems(obj):
        if isinstance(v, list):
            value_list = v
            arr = []
            for value in value_list:
                if isinstance(value, dict):
                    value = camel_case_dict_keys(value)
                arr.append(value)
            element = arr
        elif isinstance(v, dict):
            element = camel_case_dict_keys(v)
        else:
            element = v

        if isinstance(k, six.string_types):
            key = snake_to_camel_case(k)
        else:
            key = k

        output[key] = element
    return output
