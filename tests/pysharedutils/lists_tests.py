from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestCompactList:

    def test_compact_list(self):
        output = pysharedutils.compact_list([False, 1, 'One', '', {}])
        assert_equal(output, [1, 'One'])
