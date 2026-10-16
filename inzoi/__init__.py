"""
inZOI Mod Framework
~~~~~~~~~~~~~~~~~~~

Write inZOI mods in Python and turn them into the Lua the game understands.

:copyright: (c) 2026-present cqlsh
:license: inzoi.py License, see LICENSE for more details.
"""

from __future__ import annotations

__title__ = 'inzoi'
__author__ = 'cqlsh'
__license__ = 'inzoi.py License'
__copyright__ = 'Copyright 2026-present cqlsh'
__version__ = '0.1.0a0'

import logging
from typing import Literal, NamedTuple

from .errors import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final']
    serial: int

version_info: VersionInfo = VersionInfo(major=0, minor=1, micro=0, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, Literal, NamedTuple, VersionInfo