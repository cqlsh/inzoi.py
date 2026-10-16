"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from math import isfinite
from typing import TYPE_CHECKING, override

from ..errors import InvalidValueError

if TYPE_CHECKING:
    from typing import Self

class Value:
    """Represents a numeric value of a specific type.

    Values of different types cannot be mixed with each other. This class is not meant to be
    used directly, use :class:`Experience` or a subclass of :class:`Currency` instead.

    .. container:: operations

        .. describe:: x == y

            Checks if two values are equal.

        .. describe:: x != y

            Checks if two values are not equal.

        .. describe:: x < y

            Checks if a value is less than another.

        .. describe:: x <= y

            Checks if a value is less than or equal to another.

        .. describe:: x > y

            Checks if a value is greater than another.

        .. describe:: x >= y

            Checks if a value is greater than or equal to another.

        .. describe:: x + y

            Returns the sum of two values of the same type.

        .. describe:: x - y

            Returns the difference of two values of the same type.

        .. describe:: x * n

            Returns the value multiplied by a number.

        .. describe:: x / n

            Returns the value divided by a number.

        .. describe:: -x

            Returns the negated value.

        .. describe:: hash(x)

            Returns the value's hash.

        .. describe:: bool(x)

            Checks if the value is not zero.

        .. describe:: str(x)

            Returns the raw amount as a string.

    Parameters
    -----------
    amount: :class:`float`
        The raw amount of the value.
    """

    __slots__ = ['_amount']

    def __init__(self, amount: float) -> None:
        if not isfinite(amount):
            raise InvalidValueError(f'{self.__class__.__name__} needs a finite amount, received {amount!r}')
        self._amount: float = amount

    @override
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} amount={self._amount!r}>'

    @override
    def __str__(self) -> str:
        amount = self._amount
        whole = int(amount)
        if whole == amount:
            return str(whole)
        return str(amount)

    def __bool__(self) -> bool:
        return self._amount != 0

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Value) or type(other) is not type(self):
            return NotImplemented
        return self._amount == other._amount

    @override
    def __hash__(self) -> int:
        return hash((self.__class__, self._amount))

    def __lt__(self, other: Self) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._amount < other._amount

    def __le__(self, other: Self) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._amount <= other._amount

    def __gt__(self, other: Self) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._amount > other._amount

    def __ge__(self, other: Self) -> bool:
        if type(other) is not type(self):
            return NotImplemented
        return self._amount >= other._amount

    def __add__(self, other: Self) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        return type(self)(self._amount + other._amount)

    def __sub__(self, other: Self) -> Self:
        if type(other) is not type(self):
            return NotImplemented
        return type(self)(self._amount - other._amount)

    def __mul__(self, factor: float) -> Self:
        return type(self)(self._amount * factor)

    def __rmul__(self, factor: float) -> Self:
        return type(self)(self._amount * factor)

    def __truediv__(self, divisor: float) -> Self:
        return type(self)(self._amount / divisor)

    def __neg__(self) -> Self:
        return type(self)(-self._amount)

    @property
    def amount(self) -> float:
        """:class:`float`: Returns the raw amount of the value."""
        return self._amount

__all__ = ['Value']