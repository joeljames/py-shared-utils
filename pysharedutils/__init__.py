from pysharedutils.attrs import *  # NOQA
from pysharedutils.dicts import *  # NOQA
from pysharedutils.encodings import *  # NOQA
from pysharedutils.ittrs import *  # NOQA
from pysharedutils.lists import *  # NOQA
from pysharedutils.strings import *  # NOQA


__version__ = '0.0.0'
__version_info__ = tuple(__version__.split('.'))
__short_version__ = __version__


__all__ = [
    # Atrrs
    'get_object_by_source',
    # Dicts
    'MultiDict',
    'compact_dict',
    'merge_dicts',
    # Encodings
    'force_bytes',
    'force_str',
    # Ittrs
    'is_iterable',
    # Lists
    'compact_list',
    'force_list',
    'flatten_list',
    # Strings
    'camel_to_snake_case',
    'snake_to_camel_case',
    'equals',
]
