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
            ]
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
            ]
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
