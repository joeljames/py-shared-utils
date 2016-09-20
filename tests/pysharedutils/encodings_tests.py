from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestEncoding:

    def test_force_bytes_with_int(self):
        output = pysharedutils.force_bytes(123, strings_only=True)
        assert_equal(output, 123)

    def test_force_bytes(self):
        output = pysharedutils.force_bytes('foo')
        assert_true(isinstance(output, bytes))


class TestForceString:

    def test_force_str(self):
        output = pysharedutils.force_str(b'some_value')
        assert_equal(output, 'some_value')

    def test_force_str_with_str(self):
        output = pysharedutils.force_str('some_value')
        assert_equal(output, 'some_value')
