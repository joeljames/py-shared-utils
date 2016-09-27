from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestImportByPath:

    def test_import_by_path(self):
        output = pysharedutils.import_by_path(
            'pysharedutils.functions.import_by_path'
        )
        assert_equal(output, pysharedutils.import_by_path)
