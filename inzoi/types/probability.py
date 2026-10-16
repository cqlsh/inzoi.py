"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from typing import override

from ..errors import InvalidValueError

class Probability:
    """Represents the probability that something happens, from ``0.0`` (never) to ``1.0`` (always).

    The game uses it to decide whether an execute command fires.

    .. container:: operations

        .. describe:: x == y

            Checks if two probabilities are equal.

        .. describe:: x != y

            Checks if two probabilities are not equal.

        .. describe:: x < y

            Checks if a probability is lower than another.

        .. describe:: x <= y

            Checks if a probability is lower than or equal to another.

        .. describe:: x > y

            Checks if a probability is higher than another.

        .. describe:: x >= y

            Checks if a probability is higher than or equal to another.

        .. describe:: hash(x)

            Returns the probability's hash.

        .. describe:: float(x)

            Returns the raw probability.

    Parameters
    -----------
    value: :class:`float`
        The probability. Must be between ``0.0`` and ``1.0``.
    """

    __slots__ = ['_value']

    def __init__(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise InvalidValueError(f'probabilities must be between 0.0 and 1.0, received {value!r}')
        self._value: float = value

    @override
    def __repr__(self) -> str:
        return f'<Probability value={self._value!r}>'

    def __float__(self) -> float:
        return float(self._value)

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Probability):
            return NotImplemented
        return self._value == other._value

    @override
    def __hash__(self) -> int:
        return hash(self._value)

    def __lt__(self, other: Probability) -> bool:
        if type(other) is not Probability:
            return NotImplemented
        return self._value < other._value

    def __le__(self, other: Probability) -> bool:
        if type(other) is not Probability:
            return NotImplemented
        return self._value <= other._value

    def __gt__(self, other: Probability) -> bool:
        if type(other) is not Probability:
            return NotImplemented
        return self._value > other._value

    def __ge__(self, other: Probability) -> bool:
        if type(other) is not Probability:
            return NotImplemented
        return self._value >= other._value

    @property
    def value(self) -> float:
        """:class:`float`: Returns the raw probability."""
        return self._value

__all__ = ['Probability']