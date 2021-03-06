# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
URL utils
"""
from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from six.moves.urllib.parse import urlparse, urlunparse
from os.path import split as pathsplit, join as pathjoin


def url_sibling(url, sibling):
    """
    Replaces the last path element in an url

    Parameters
    ----------
    url : str
        The url for which the last path element should be replaced
    sibling : str
        The replace value
    """
    parsed = urlparse(url)
    newpath_segments = pathsplit(parsed.path)[:-1] + (sibling,)
    newpath = pathjoin(*newpath_segments)
    return urlunparse(list(parsed[:2]) + [newpath] + list(parsed[3:]))
