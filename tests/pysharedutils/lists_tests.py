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


class TestListIntersection:

    def test_list_intersection(self):
        output = pysharedutils.list_intersection([1, 2, 3], [1])
        assert_equal(output, [1])

    def test_list_intersection_with_arr2_gt_lenght(self):
        output = pysharedutils.list_intersection([1], [9, 6, 1])
        assert_equal(output, [1])

    def test_list_intersection_with_no_intersection(self):
        output = pysharedutils.list_intersection([], [2, 1])
        assert_equal(output, [])


class TestListFind:

    def test_list_find(self):
        def predicate(value):
            if value > 40:
                return True
        output = pysharedutils.list_find([1, 2, 41, 80], predicate)
        assert_equal(output, 41)

    def test_list_find_with_from_index(self):
        def predicate(value):
            if value > 40:
                return True
        output = pysharedutils.list_find([1, 2, 41, 80], predicate, 3)
        assert_equal(output, 80)
