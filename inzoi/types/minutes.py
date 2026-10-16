"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .duration import Duration

class Minutes(Duration):
    """Represents a duration measured in in-game minutes."""

    __slots__ = ()

    _MINUTES_PER_UNIT = 1

__all__ = ['Minutes']