#
# Copyright 2018 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""Test the app factory for Kokudaka."""

from unittest import TestCase
from unittest.mock import patch

from kokudaka import create_app


class CreateAppTest(TestCase):
    """Test Cases for create_app app factory."""

    def test_create_app(self):
        """Assert testing is false without passing test config."""
        self.assertFalse(create_app().testing)

    def test_create_test_app(self):
        """Assert that testing is true with test config."""
        self.assertTrue(
            create_app(
                {
                    'TESTING': True
                }
            ).testing
        )
