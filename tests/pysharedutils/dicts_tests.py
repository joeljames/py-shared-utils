from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestMultiDict:

    def test_multi_dict(self):
        output = pysharedutils.MultiDict({'username': 'foobar'})
        assert_equal(output.getlist('username'), ['foobar'])


class TestCompactDict:

    def test_compact_dict(self):
        output = pysharedutils.compact_dict({'username': 'foobar', 'name': ''})
        assert_equal(output, {'username': 'foobar'})


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
