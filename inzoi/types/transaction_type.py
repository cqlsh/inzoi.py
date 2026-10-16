"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .ident import Ident

class TransactionType(Ident):
    """Represents the type of a currency transaction.

    The game uses it to record why currency was added or taken away, for example ``ExpenseBuy``
    for a purchase.

    .. note::

        A complete list of the game's transaction types is not available yet.
    """

    __slots__ = ()

__all__ = ['TransactionType']