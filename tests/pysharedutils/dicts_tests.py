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
