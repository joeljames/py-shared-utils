from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestSingleton:
    num = 0

    @pysharedutils.singleton
    def singleton_usage_method(self):
        self.num += 1
        return self.num

    def setup(self):
        self.num = 0

    def test_singelton(self):
        self.singleton_usage_method()
        assert_equal(self.singleton_usage_method(), 1)


class TestMemoize:
    num = 0

    @pysharedutils.memoize
    def memoize_usage_method(self, some_arg):
        self.num += 1
        return self.num

    def setup(self):
        self.num = 0

    def test_singelton_with_same_argument(self):
        self.memoize_usage_method(20)
        assert_equal(self.memoize_usage_method(20), 1)

    def test_singelton_with_different_argument(self):
        self.memoize_usage_method(20)
        assert_equal(self.memoize_usage_method(30), 2)


class TestCachedProperty:

    class CachedPropertyExampleClass:
        num = 0

        @pysharedutils.cached_property
        def increment(self):
            self.num += 1
            return self.num

    def setup(self):
        self.num = 0

    def test_cached_property(self):
        example_class = self.CachedPropertyExampleClass()
        example_class.increment
        example_class.increment
        assert_equal(example_class.increment, 1)
