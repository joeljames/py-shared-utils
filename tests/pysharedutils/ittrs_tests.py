from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestIttrs:

    def test_is_iterable_true(self):
        output = pysharedutils.is_iterable([])
        assert_true(output)

    def test_is_terable_false(self):
        output = pysharedutils.is_iterable(1)
        assert_false(output)
