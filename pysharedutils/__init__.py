from pysharedutils.attrs import (
    get_object_by_source,
)

from pysharedutils.ittrs import (
    is_iterable,
)

from pysharedutils.strings import (
    force_str,
)


__version__ = '0.0.0'
__version_info__ = tuple(__version__.split('.'))
__short_version__ = __version__


__all__ = [
    'get_object_by_source',
    'is_iterable',
    'force_str',
]
