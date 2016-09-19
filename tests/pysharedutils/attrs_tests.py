from nose.tools import *  # flake8: noqa
from mock import *  # flake8: noqa

import pysharedutils


class TestAttrs:

    def test_get_object_by_source_with_obj(self):
        user = Mock(name='user', username='foo.bar.com')
        output = pysharedutils.get_object_by_source(
            user,
            source='username'
        )
        assert_equal(output, 'foo.bar.com')

    def test_get_object_by_source_with_dict(self):
        user = {'username': 'foo.bar.com'}
        output = pysharedutils.get_object_by_source(
            user,
            source='username'
        )
        assert_equal(output, 'foo.bar.com')

    def test_get_object_by_source_with_obj_and_dot_syntax(self):
        user = Mock(name='user', username='foo.bar.com')
        comment = Mock(name='comment', user=user)
        output = pysharedutils.get_object_by_source(
            comment,
            source='user.username'
        )
        assert_equal(output, 'foo.bar.com')

    def test_get_object_by_source_with_dict_and_dot_syntax(self):
        user = {'username': 'foo.bar.com'}
        comment = {'user': user}
        output = pysharedutils.get_object_by_source(
            comment,
            source='user.username'
        )
        assert_equal(output, 'foo.bar.com')
