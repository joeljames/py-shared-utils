import six
import collections
import copy

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
    'get_dict_properties',
    'map_dict_keys',
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
        if hasattr(self._d, name):
            return getattr(self._d, name)
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
        value = _compact_dict_value(value)
        if value:
            output[key] = value
    return output


def _compact_dict_value(value):
    if isinstance(value, six.string_types):
        return value
    elif isinstance(value, collections.Mapping):
        return compact_dict(value)
    elif isinstance(value, collections.Iterable):
        return list(map(_compact_dict_value, value))
    return value


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


def camel_case_dict_keys(obj, upper=False):
    """
    :param obj: A dict who's keys has to
        be converted from snake case to camel case.
    :param upper: Whether or not to return UpperCamelCase
        instead of lowerCamelCase
    Maps the keys of the dict from snake case to camel case.
    Example:
        >>> camel_case_dict_keys({'snake_case': 'snake_case'})
        {'snakeCase': 'snake_case'}
        >>> camel_case_dict_keys({'snake_case': 'snake_case'}, upper=True)
        {'SnakeCase': 'snake_case'}
    """
    output = {}
    for k, v in six.iteritems(obj):
        if isinstance(v, list):
            value_list = v
            arr = []
            for value in value_list:
                if isinstance(value, dict):
                    value = camel_case_dict_keys(value, upper=upper)
                arr.append(value)
            element = arr
        elif isinstance(v, dict):
            element = camel_case_dict_keys(v, upper=upper)
        else:
            element = v

        if isinstance(k, six.string_types):
            key = snake_to_camel_case(k, upper=upper)
        else:
            key = k

        output[key] = element
    return output


def get_dict_properties(obj, strict, *args):
    """
    :param obj: A python dict object.
    :param strict: A bool, if set to False will ignore `AttributeError` when
        trying to get non-existing propert on the object.
    :param *args: Property names which has to be fetched from the dict.
        You can also use dot separated names to get
        properties from nested dicts.

    Example:
        >>> d = {'first_name': 'Foo', 'last_name': 'Bar'}
        >>> get_dict_properties(d, 'first_name')
        {'first_name': 'Foo'}
    """
    output = {}

    for key in args:
        value = None
        if '.' in key:
            coppied_obj = copy.copy(obj)
            try:
                for source in key.split('.'):
                    coppied_obj = coppied_obj.get(source)
                value = coppied_obj
            except AttributeError:
                if strict is True:
                    raise
        else:
            value = obj.get(key)
        output[key] = value

    return output


def map_dict_keys(obj, map_obj):
    """
    :param obj: A python dict object who's keys has to be mapped..

    :param map_obj: A map dict specifying the key and the new key..

    Example:
        >>> obj = {'first_name': 'Foo', 'last_name': 'Bar'}
        >>> map_obj = {'first_name': 'given_name'}
        >>> map_dict_keys(obj, map_obj)
        {'given_name': 'Foo', 'last_name': 'Bar'}
    """
    for key, value in six.iteritems(map_obj):
        if '.' in key:
            map_key = value.rsplit('.', 1)[1]
            coppied_obj = copy.copy(obj)
            sources = key.split('.')
            sources_len = len(sources)
            for index, source in enumerate(sources):
                coppied_obj = coppied_obj.get(source)
                # Call the recursive `map_dict_keys` when you hit the
                # second last element in the source.
                if coppied_obj and index == (sources_len - 2):
                    # Create the map obj for the leaf obj
                    leaf_map_obj = {
                        sources[index + 1]: map_key
                    }
                    map_dict_keys(
                        coppied_obj,
                        leaf_map_obj
                    )
        else:
            map_key = value
            if key in obj:
                obj[map_key] = obj.pop(key)
    return obj
