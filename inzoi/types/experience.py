"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .value import Value

class Experience(Value):
    """Represents experience points of a skill.

    The game keeps a separate amount of experience for every skill of a Zoi and stores it as a
    plain number, so fractional amounts are allowed.
    """

    __slots__ = ()

__all__ = ['Experience']