# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Tests for pyvo.utils.url
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from pyvo.utils.url import url_sibling


def test_url():
    url = "http://example.org/tap/capabilities"
    siblingified = url_sibling(url, "tables")

    assert siblingified == "http://example.org/tap/tables"
