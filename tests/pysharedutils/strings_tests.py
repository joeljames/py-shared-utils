from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestCamelToSnakeCase:

    def test_camel_to_snake_case_regular(self):
        word = pysharedutils.camel_to_snake_case('camelCase')
        assert_equal(word, 'camel_case')

    def test_camel_to_snake_case_with_numbers(self):
        word = pysharedutils.camel_to_snake_case('camel2SnakeCase')
        assert_equal(word, 'camel2_snake_case')

    def test_camel_to_snake_case_with_abbreviation(self):
        word = pysharedutils.camel_to_snake_case('HTTPGet')
        assert_equal(word, 'http_get')

    def test_camel_to_snake_case_with_lower_camel_case(self):
        word = pysharedutils.camel_to_snake_case('getHTTP')
        assert_equal(word, 'get_http')

    def test_camel_to_snake_case_with_underscore(self):
        word = pysharedutils.camel_to_snake_case('_camelCase')
        assert_equal(word, '_camel_case')


class TestSnakeCaseToCamel:

    def test_snake_to_camel_case(self):
        output = pysharedutils.snake_to_camel_case('snake_case')
        assert_equal(output, 'snakeCase')
