import six
import collections

from pysharedutils.strings import camel_to_snake_case

__all__ = [
    'MultiDict',
    'compact_dict',
    'merge_dicts',
    'snake_case_dict',
]


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
    return {key: value for key, value in six.iteritems(obj) if value}


def merge_dicts(*dicts):
    """
    Merges all of the given dicts together without mutations.
    """
    result = {}
    for d in dicts:
        if isinstance(d, collections.Mapping):
            result = dict(result, **d)
    return result


def snake_case_dict(obj):
    """
    :param obj: A dict who's keys has to
        be converted from camel case to snake case.

    Maps the keys of the dict from camelCase to snake_case.
    Example:
        >>> snake_case_dict({'camelCase': 'camel_case'})
        {'camel_case': 'camel_case'}
    """
    output = {}
    for k, v in six.iteritems(obj):
        if isinstance(v, list):
            value_list = v
            arr = []
            for value in value_list:
                if isinstance(value, dict):
                    value = snake_case_dict(value)
                arr.append(value)
            element = arr
        elif isinstance(v, dict):
            element = snake_case_dict(v)
        else:
            element = v

        if isinstance(k, six.string_types):
            key = camel_to_snake_case(k)
        else:
            key = k

        output[key] = element
    return output
