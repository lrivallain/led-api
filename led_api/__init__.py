"""LED API.

.. moduleauthor:: Ludovic Rivallain <ludovic.rivallain+ledapi -> gmail.com>

"""

import sys

if sys.version_info < (3, 6):
    raise Exception('LED API requires Python versions 3.6 or later.')

__all__ = [
    'utils',
]
