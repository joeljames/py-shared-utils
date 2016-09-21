from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pytz
import pysharedutils


class TestUtcNow:

    def test_utc_now(self):
        output = pysharedutils.utc_now()
        assert_equal(output.tzinfo, pytz.UTC)
