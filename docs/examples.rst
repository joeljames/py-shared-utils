=========
Examples
=========
Some quick usage examples.

Getting started
===============
If you haven't installed pysharedutils, simply use pip to install it like so::

    $ pip install pysharedutils


Attrs
=====

get_object_by_source:
---------------------
Tries to get the object by source. Similar to Python's ``getattr(obj, source)``, but takes a dot separated string for source to get source from nested obj, instead of a single source field. Also, supports getting source form obj where obj is a dict type. Signature: ``get_object_by_source(obj, source, allow_blank_source=False)``

:attr:`obj`
    A python object or a python dict.

:attr:`source`
    The source name which has to be extracted from the object. You can use dot syntax to specify nested source.

:attr:`allow_blank_source` (Default: False)
    A bool, if set to `True` it catches ``AttributeError`` and returns ``None`` if the source does not exist on the obj.

Example with python object::

    class User:
        def __init__(self, email, username):
            self.email = email
            self.username = username

    import pysharedutils
    obj = User(email='foo.example.com', username='foobar')
    pysharedutils.get_object_by_source(obj=obj, source='email')
    # 'foo.example.com'


Example with python dict::

    obj = {'user': {'username': 'foobar', 'email': 'foo.example.com'}}

    import pysharedutils
    pysharedutils.get_object_by_source(obj=obj, source='user.username')
    # 'foobar'


Encodings
=========
force_bytes:
------------
Forces the value to a bytes instance. Signature: ``force_bytes(value, encoding='utf-8', strings_only=True, errors='strict')``

:attr:`value`
    A value which has to be converted to a bytes.

:attr:`encoding` (Default: 'utf-8')
    The encoding type.

:attr:`strings_only` (Default: True)
    A bool, if set to True will ignore decoding values which are `None` or `int`.

:attr:`errors` (Default: 'strict')
    The error level when encoding.

Example::

    import pysharedutils
    pysharedutils.force_bytes('some_string')
    # b'some_string'

force_str:
----------
Forces the value to a str instance, decoding if necessary. Signature: ``force_str(value, encoding='utf-8')``

:attr:`value`
    A value which has to be converted to a string.

:attr:`encoding` (Default: 'utf-8')
    The string encoding.

Example::

    import pysharedutils
    pysharedutils.force_str(b'some_byte_string')
    # 'some_byte_string'


Lists
=====
compact_list:
-------------
Creates an list with all falsey values removed. Signature: ``compact_list(arr)``

:attr:`arr`
    A list who's falsey values has to be removed.

Example::

    import pysharedutils
    pysharedutils.compact_list([False, 1, '', {}])
    # [1]


Strings
=======
camel_to_snake_case:
--------------------
Converts a camel case word to snake case. Signature: ``camel_to_snake_case(word)``

:attr:`word`
    A string that needs to be converted to snake case.


Example::

    import pysharedutils
    pysharedutils.camel_to_snake_case('camelCase')
    # 'camel_case'


snake_to_camel_case:
--------------------
Converts a snake case word to camel case. Signature: ``snake_to_camel_case(word)``

:attr:`word`
    A string that needs to be converted to camel case.


Example::

    import pysharedutils
    pysharedutils.snake_to_camel_case('snake_case')
    # 'snakeCase'
