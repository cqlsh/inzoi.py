"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .ident import Ident

class BuffId(Ident):
    """Represents the identifier of a buff, as defined in the game's ``Buff.json``.

    .. note::

        A complete list of the game's buff identifiers is not available yet. Consider passing
        the identifier in as a parameter from the Mod Kit.
    """

    __slots__ = ()

__all__ = ['BuffId']