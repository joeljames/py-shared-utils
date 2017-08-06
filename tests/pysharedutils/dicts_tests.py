from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestObjectDict:

    def test_object_dict_access(self):
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
        assert_equal(output.name, 'foo')
        assert_equal(output.nesting.nested_key, 'val')
        assert_equal(output.nesting.inner_nesting, 'inner_nesting_val')
        assert_equal(output.some_list[0].foo, 'bar')

    def test_object_dict_write(self):
        object_dict = pysharedutils.ObjectDict({})
        object_dict.name = 'foo'
        assert_equal(object_dict.name, 'foo')

    def test_object_dict_methods(self):
        object_dict = pysharedutils.ObjectDict({'name': 'foo'})
        assert_equal(object_dict.get('name'), 'foo')
        assert_equal(object_dict.pop('missing', 'default'), 'default')


class TestMultiDict:

    def test_multi_dict(self):
        output = pysharedutils.MultiDict({'username': 'foobar'})
        assert_equal(output.getlist('username'), ['foobar'])


class TestCompactDict:

    def test_compact_dict(self):
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
            ],
            'roles': ['admin', 'client'],
        }
        expected_output = {
            'username': 'foobar',
            'comment': {
                'line_1': 'abc',
                'inner_nesting': {
                    'key': 'value',
                }
            },
            'location': [
                {
                    'city': 'Baton Rouge',
                    'inner_nesting': {
                        'key': 'value'
                    }
                }
            ],
            'roles': ['admin', 'client'],
        }
        output = pysharedutils.compact_dict(data)
        assert_equal(output, expected_output)


class TestMergeDicts:

    def test_merge_dicts(self):
        d1 = {'a': 'apple'}
        d2 = {'b': 'ball'}
        d3 = {'c': 'cat'}
        output = pysharedutils.merge_dicts(d1, d2, d3, None, [])
        assert_equal(
            output,
            {'a': 'apple', 'b': 'ball', 'c': 'cat'}
        )


class TestSnakeCaseDictKeys:

    def test_simple_snake_case_dict_keys(self):
        output = pysharedutils.snake_case_dict_keys(
            {'camelCase': 'some value'}
        )
        assert_equal(
            output,
            {'camel_case': 'some value'}
        )

    def test_nested_snake_case_dict_keys(self):
        obj = {
            1: 'int key',
            (1, 2): 'tuple key',
            'snake_case': '',
            'user': {
                'userName': 'foo',
                'comments': [
                    {
                        'someComent': 'abc',
                        'someNestedDict': {
                            'camelCase': 'a'
                        }
                    }
                ]
            }
        }
        expected_output = {
            1: 'int key',
            (1, 2): 'tuple key',
            'snake_case': '',
            'user': {
                'user_name': 'foo',
                'comments': [
                    {
                        'some_coment': 'abc',
                        'some_nested_dict': {
                            'camel_case': 'a'
                        }
                    }
                ]
            }
        }
        output = pysharedutils.snake_case_dict_keys(obj)
        assert_equal(
            output,
            expected_output
        )


class TestCamelCaseDictKeys:

    def test_simple_camel_case_dict_keys(self):
        output = pysharedutils.camel_case_dict_keys(
            {'snake_case': 'some value'}
        )
        assert_equal(
            output,
            {'snakeCase': 'some value'}
        )

    def test_nested_camel_case_dict_keys(self):
        obj = {
            1: 'int key',
            (1, 2): 'tuple key',
            'camelCase': '',
            'user': {
                'user_name': 'foo',
                'comments': [
                    {
                        'some_coment': 'abc',
                        'some_nested_dict': {
                            'camel_case': 'a'
                        }
                    }
                ]
            }
        }
        expected_output = {
            1: 'int key',
            (1, 2): 'tuple key',
            'camelCase': '',
            'user': {
                'userName': 'foo',
                'comments': [
                    {
                        'someComent': 'abc',
                        'someNestedDict': {
                            'camelCase': 'a'
                        }
                    }
                ]
            }
        }
        output = pysharedutils.camel_case_dict_keys(obj)
        assert_equal(
            output,
            expected_output
        )

    def test_simple_upper_camel_case_dict_keys(self):
        output = pysharedutils.camel_case_dict_keys(
            {'snake_case': 'some value'}, upper=True
        )
        assert_equal(
            output,
            {'SnakeCase': 'some value'}
        )

    def test_nested_upper_camel_case_dict_keys(self):
        obj = {
            1: 'int key',
            (1, 2): 'tuple key',
            'camelCase': '',
            'user': {
                'user_name': 'foo',
                'comments': [
                    {
                        'some_coment': 'abc',
                        'some_nested_dict': {
                            'camel_case': 'a'
                        }
                    }
                ]
            }
        }
        expected_output = {
            1: 'int key',
            (1, 2): 'tuple key',
            'CamelCase': '',
            'User': {
                'UserName': 'foo',
                'Comments': [
                    {
                        'SomeComent': 'abc',
                        'SomeNestedDict': {
                            'CamelCase': 'a'
                        }
                    }
                ]
            }
        }
        output = pysharedutils.camel_case_dict_keys(obj, upper=True)
        assert_equal(
            output,
            expected_output
        )

class TestGetDictProperties:

    def test_simple_get_dict_properties(self):
        d = {
            'first_name': 'Foo',
            'last_name': 'Bar'
        }
        output = pysharedutils.get_dict_properties(
            d, False, 'first_name'
        )
        assert_equal(
            output,
            {'first_name': 'Foo'}
        )

    def test_get_dict_properties_with_non_existing_property(self):
        d = {
            'first_name': 'Foo',
            'last_name': 'Bar'
        }
        output = pysharedutils.get_dict_properties(
            d, False, 'first_name', 'zipcode'
        )
        assert_equal(
            output,
            {'first_name': 'Foo', 'zipcode': None}
        )

    def test_get_dict_properties_with_nested_dict(self):
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
        output = pysharedutils.get_dict_properties(
            d,
            False,
            'first_name',
            'zipcode',
            'comment.message',
            'comment.location',
            'comment.user.username'
        )
        expected_output = {
            'first_name': 'Foo',
            'zipcode': None,
            'comment.message': 'some text',
            'comment.location': None,
            'comment.user.username': 'foo.bar.com'
        }
        assert_equal(output, expected_output)

    @raises(AttributeError)
    def test_get_dict_properties_with_strict_and_invalid_property(self):
        d = {
            'comment': {
                'message': 'some text',
            }
        }
        pysharedutils.get_dict_properties(
            d,
            True,
            'comment.user.username'
        )

    def test_get_dict_properties_without_strict_and_invalid_property(self):
        d = {
            'comment': {
                'message': 'some text',
            }
        }
        output = pysharedutils.get_dict_properties(
            d,
            False,
            'comment.user.username'
        )
        assert_equal(output, {'comment.user.username': None})


class TestMapDictKeys:

    def test_map_dict_keys(self):
        obj = {
            'first_name': 'Joe',
            'middle_name': 'P',
            'last_name': 'Smith'
        }
        map_obj = {
            'first_name': 'given_name',
            'last_name': 'surname',
            'mis_spelled_key': 'mis_spelled_value'
        }
        output = pysharedutils.map_dict_keys(obj, map_obj)
        expected_output = {
            'given_name': 'Joe',
            'middle_name': 'P',
            'surname': 'Smith'
        }
        assert_equal(output, expected_output)

    def test_map_dict_keys_with_one_level(self):
        obj = {
            'first_name': 'Joe',
            'user': {
                'username': 'joe@example.com'
            }
        }
        map_obj = {
            'first_name': 'given_name',
            'user.username': 'user.email',
        }
        expected_output = {
            'given_name': 'Joe',
            'user': {
                'email': 'joe@example.com'
            }
        }
        output = pysharedutils.map_dict_keys(obj, map_obj)
        assert_equal(output, expected_output)

    def test_map_dict_keys_with_two_level_nesting(self):
        obj = {
            'first_name': 'Joe',
            'user': {
                'contact': {
                    'email': 'joe@example.com'
                }
            }
        }
        map_obj = {
            'first_name': 'given_name',
            'user.contact.email': 'user.contact.contact_email',
        }
        expected_output = {
            'given_name': 'Joe',
            'user': {
                'contact': {
                    'contact_email': 'joe@example.com'
                }
            }
        }
        output = pysharedutils.map_dict_keys(obj, map_obj)
        assert_equal(output, expected_output)

    def test_map_dict_keys_with_three_level_nesting(self):
        obj = {
            'first_name': 'Joe',
            'user': {
                'contact': {
                    'email': 'joe@example.com',
                    'address': {
                        'line_1': 'adress line 1'
                    }
                }
            }
        }
        map_obj = {
            'first_name': 'given_name',
            'user.contact.email': 'user.contact.contact_email',
            'user.contact.address.line_1': 'user.contact.address.address_1',
        }
        expected_output = {
            'given_name': 'Joe',
            'user': {
                'contact': {
                    'contact_email': 'joe@example.com',
                    'address': {
                        'address_1': 'adress line 1'
                    }
                }
            }
        }
        output = pysharedutils.map_dict_keys(obj, map_obj)
        assert_equal(output, expected_output)
