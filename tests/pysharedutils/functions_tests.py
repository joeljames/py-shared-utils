from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestCachedProprty:

    class CachedPropertyExampleClass:
        num = 0

        @pysharedutils.cached_property
        def increment(self):
            self.num += 1
            return self.num

    def test_cached_property(self):
        example_class = self.CachedPropertyExampleClass()
        example_class.increment
        example_class.increment
        assert_equal(example_class.increment, 1)
