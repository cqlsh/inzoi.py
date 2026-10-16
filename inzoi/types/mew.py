"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .currency import Currency

class Mew(Currency, id='Mew'):
    """Represents an amount of Mew, a currency of the game.

    The official documentation uses Mew for everyday transactions such as purchases.
    """

    __slots__ = ()

__all__ = ['Mew']