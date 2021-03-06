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


Dates
=====
utc_now:
--------
Returns current UTC time and sets the time zone info to UTC. Signature: ``utc_now()``

Example::

    import pysharedutils
    pysharedutils.utc_now()
    output.utc_now()
    # datetime.datetime(2016, 9, 21, 18, 56, 53, 863501, tzinfo=<UTC>)


Decorators
==========
singleton:
----------
Decorator that creates a singleton instance. If the method is called later a cached instance of the method is returned. Signature: ``@singleton``

Example::

    import pysharedutils

    @pysharedutils.singleton
    def some_method(self):
        return 'Something'

memoize:
--------
Decorator that caches a function's return value each time it is called. If called later with the same arguments, the cached value is returned, and the method is not reevaluated. Signature: ``@memoize``

Example::

    import pysharedutils

    @pysharedutils.memoize
    def some_method(self, arg1, arg2):
        # Perform some heavy computation
        return 'Something'

cached_property:
----------------
Decorator that caches the property on the instance. Computed only once per instance. Signature: ``@cached_property``

Example::

    import pysharedutils

    class SlowClass:

        @pysharedutils.cached_property
        def very_slow(self):
            time.sleep(1)
            return "Slow class"

    SlowClass().very_slow


Dicts
=====
ObjectDict:
-----------
Helper class that makes a dictionary behave like an object, with attribute-style access (read and write). Signature: ``ObjectDict(d)``

:attr:`d`
    A python dict object.

Example::

    import pysharedutils
    data = {
        'name': 'foo',
        'nesting': {
            'nested_key': 'val',
            'inner_nesting': 'inner_nesting_val'
        },
        'some_list': [
            {
                'foo': 'bar'
            }
        ]
    }
    output = pysharedutils.ObjectDict(data)
    output.name
    # 'foo'
    output.nesting.nested_key
    # 'val'
    output.some_list[0].foo
    # 'bar'
    # You can also set variables using dot syntax
    object_dict  = pysharedutils.ObjectDict(data)
    object_dict.gender = 'Male'
    object_dict.gender
    # 'Male'

MultiDict:
----------
Extends a python dict type by adding ``getlist`` method. Signature: ``MultiDict(dict)``

Example::

    import pysharedutils
    output = pysharedutils.MultiDict({'username': 'foobar'})
    output.getlist('username')
    # ['foobar']

compact_dict:
-------------
Creates a dict with all falsey values removed. Signature: ``compact_dict(obj)``

:attr:`obj`
    A dict who's falsey values has to be removed.

Example::

    import pysharedutils
    data = {
        'username': 'foobar',
        'name': '',
        'comment': {
            'line_1': 'abc',
            'line_2': '',
            'inner_nesting': {
                'key': 'value',
                'blank': None
            }
        },
        'location': [
            {
                'address_1': '',
                'city': 'Baton Rouge',
                'inner_nesting': {
                    'key': 'value',
                    'blank': None
                }
            }
        ]
    }
    pysharedutils.compact_dict(data)
    # {'username': 'foobar', 'comment': {'line_1': 'abc', 'inner_nesting': {'key': 'value'}}, 'location': [{'city': 'Baton Rouge', 'inner_nesting': {'key': 'value'}}]}

merge_dicts:
------------
Merges all of the given dicts together. Signature: ``compact_dict(*dicts)``

Example::

    import pysharedutils
    d1 = {'a': 'apple'}
    d2 = {'b': 'ball'}
    pysharedutils.merge_dicts(d1, d2)
    # {'a': 'apple', 'b': 'ball'}

snake_case_dict_keys:
---------------------
Maps the keys of the dict from camel case to snake case. Signature: ``snake_case_dict_keys(obj)``

Example::

    import pysharedutils
    pysharedutils.snake_case_dict_keys({'camelCase': 'camel_case'})
    # {'camel_case': 'camel_case'}

camel_case_dict_keys:
---------------------
Maps the keys of the dict from snake case to camel case. Signature: ``camel_case_dict_keys(obj, upper=False)``

:attr:`obj`
    A python dict object.

:attr:`upper`
    A bool, default False. If set to True will convert the keys to upper camel case else will conver the keys to lower camel case.

Example::

    import pysharedutils
    pysharedutils.camel_case_dict_keys({'snake_case': 'snake_case'})
    # {'snakeCase': 'snake_case'}

    pysharedutils.camel_case_dict_keys({'snake_case': 'snake_case'}, upper=True)
    # {'SnakeCase': 'snake_case'}

get_dict_properties:
---------------------
Get multiple key value from a dict in one call. Signature: ``get_dict_properties(obj, *args)``

:attr:`obj`
    A python dict object.

:attr:`strict`
    A bool, if set to False will ignore ``AttributeError`` when trying to get non-existing propert on the object.

:attr:`*args`
    Property names which has to be fetched from the dict.
    You can also use dot separated names to get properties from nested dicts. See example below.

Example::

    import pysharedutils
    d = {
        'first_name': 'Foo',
        'last_name': 'Bar',
        'comment': {
            'message': 'some text',
            'user': {
                'username': 'foo.bar.com'
            }
        }
    }
    pysharedutils.get_dict_properties(
      d,
      False,
      'first_name',
      'zipcode',
      'comment.message',
      'comment.location',
      'comment.user.username'
    )
    # {'first_name': 'Foo', 'comment.user.username': 'foo.bar.com', 'zipcode': None, 'comment.location': None, 'comment.message': 'some text'}

map_dict_keys:
--------------
Maps the keys of a dict with the map keys. Signature: ``map_dict_keys(obj, map_obj)``

:attr:`obj`
    A python dict object who's keys has to be mapped.

:attr:`map_obj`
    A map dict specifying the key and the new key.

Example::

    import pysharedutils
    obj = {
        'first_name': 'Joe',
        'user': {
            'contact': {
                'email': 'joe@example.com',
                'address': {
                    'line_1': 'address line 1'
                }
            }
        }
    }
    map_obj = {
        'first_name': 'given_name',
        'user.contact.email': 'user.contact.contact_email',
        'user.contact.address.line_1': 'user.contact.address_1',
    }
    pysharedutils.map_dict_keys(obj, map_obj)
    # {'user': {'contact': {'contact_email': 'joe@example.com', 'address': {'address_1': 'address line 1'}}}, 'given_name': 'Joe'}

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


Functions
=========
import_by_path:
---------------
Imports a class or module by path(dot syntax). Raise ImportError if the import failed. Signature: ``import_by_path(path)``

:attr:`path`
    The path to the class that has to be imported.

Example::

    import pysharedutils
    pysharedutils.import_by_path('pysharedutils.functions.import_by_path')

    # <function import_by_path at 0x103d2d5f0>


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

force_list:
-----------
Force the given object to be a list, wrapping single objects. Signature: ``force_list(obj)``

:attr:`obj`
    A obj which has to be converted to list.

Example::

    import pysharedutils
    pysharedutils.force_list('name')
    # ['name']


flatten_list:
-------------
Creates an a flattened list. Signature: ``flatten_list(arr)``

:attr:`arr`
    A list which has to be flattened.

Example::

    import pysharedutils
    pysharedutils.flatten_list([1, [2, [3, [4]], 5]])
    # [1, 2, 3, 4, 5]

list_intersection:
------------------
Return the intersection of the two lists. Signature: ``list_intersection(arr1, arr2)``

:attr:`arr1`
    A list that has to be intersected.

:attr:`arr2`
    A list that has to be intersected.

Example::

    import pysharedutils
    pysharedutils.list_intersection([1, 2], [1])
    # [1]

list_find:
-----------
Iterates over elements of collection, returning the first element predicate returns truthy for. Signature: ``list_find(predicate, coll, from_index=0)``

:attr:`predicate`
    The function invoked per iteration.

:attr:`coll`
    The collection to inspect.

:attr:`from_index` Default(0)
    The index to search from.

Example::

    import pysharedutils
    def predicate(value):
        if value > 40:
            return True
    pysharedutils.list_find(predicate, [1, 2, 41, 80])
    # 41


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
Converts a snake case word to camel case. Signature: ``snake_to_camel_case(word, upper=False)``

:attr:`word`
    A string that needs to be converted to camel case.

:attr:`upper`
    A bool, default False. If set to True will convert the word to upper camel case else will conver the word to lower camel case.


Example::

    import pysharedutils
    pysharedutils.snake_to_camel_case('snake_case')
    # 'snakeCase'
    pysharedutils.snake_to_camel_case('snake_case', upper=True)
    # 'SnakeCase'

equals:
-------
Returns True if the two strings are equal, False otherwise. The time taken is independent of the number of characters that match. For the sake of simplicity, this function executes in constant time only when the two strings have the same length. It short-circuits when they have different lengths. Signature: ``equals(val1, val2)``

:attr:`val1`
    A string that has to be compared.

:attr:`val2`
    A string that has to be compared.

Example::

    import pysharedutils
    pysharedutils.equals('some_value', 'some_value')
    # True
