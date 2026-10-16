"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .ident import Ident

class BuffTag(Ident):
    """Represents a buff tag.

    Buffs can carry tags, which makes it possible to check for or remove every buff with the
    same tag at once instead of one specific buff.

    .. note::

        A complete list of the game's buff tags is not available yet.
    """

    __slots__ = ()

__all__ = ['BuffTag']