from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestStrings:

    def test_force_str(self):
        output = pysharedutils.force_str(b'some_value')
        assert_equal(output, 'some_value')

    def test_force_str_with_str(self):
        output = pysharedutils.force_str('some_value')
        assert_equal(output, 'some_value')
