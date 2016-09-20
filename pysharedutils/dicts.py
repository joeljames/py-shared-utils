import six
import collections

__all__ = [
    'MultiDict',
    'compact_dict',
    'merge_dicts',
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
