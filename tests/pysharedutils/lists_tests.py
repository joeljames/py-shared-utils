from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestCompactList:

    def test_compact_list(self):
        output = pysharedutils.compact_list([False, 1, 'One', '', {}])
        assert_equal(output, [1, 'One'])


class TestForceList:

    def test_force_list_with_none(self):
        output = pysharedutils.force_list(None)
        assert_equal(output, [])

    def test_force_list_with_str(self):
        output = pysharedutils.force_list('abc')
        assert_equal(output, ['abc'])

    def test_force_list_with_obj(self):
        obj = Mock(name='obj')
        output = pysharedutils.force_list(obj)
        assert_equal(output, [obj])


class TestFlattenList:

    def test_flatten_list(self):
        arr = [1, [2, [3, [4]], 5]]
        output = pysharedutils.flatten_list(arr)
        assert_equal(output, [1, 2, 3, 4, 5])
