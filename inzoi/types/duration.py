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
    from typing import ClassVar, Final, Self

_ROUNDING_TOLERANCE: Final = 1e-9

class Duration:
    """Represents a span of in-game time.

    Durations of different units can be mixed and compared with each other. The game measures
    them in whole in-game minutes. A plain :class:`Duration` counts in minutes as well, consider
    using :class:`Minutes` or :class:`Hours` to make the unit visible.

    .. container:: operations

        .. describe:: x == y

            Checks if two durations are equally long.

        .. describe:: x != y

            Checks if two durations are not equally long.

        .. describe:: x < y

            Checks if a duration is shorter than another.

        .. describe:: x <= y

            Checks if a duration is shorter than or as long as another.

        .. describe:: x > y

            Checks if a duration is longer than another.

        .. describe:: x >= y

            Checks if a duration is longer than or as long as another.

        .. describe:: x + y

            Returns the sum of two durations in the unit of the left operand.

        .. describe:: x - y

            Returns the difference of two durations in the unit of the left operand.

        .. describe:: x * n

            Returns the duration multiplied by a number.

        .. describe:: x / n

            Returns the duration divided by a number. Only works if the result is a whole number
            of minutes.

        .. describe:: x // n

            Returns the duration divided by a number, rounded down to whole minutes.

        .. describe:: hash(x)

            Returns the duration's hash.

        .. describe:: bool(x)

            Checks if the duration is longer than zero.

    .. note::

        The game's buff commands are the only documented place that takes a duration so far,
        and they count in in-game minutes.

    Parameters
    -----------
    amount: :class:`float`
        The length of the duration in its unit. Must not be negative and must add up to whole
        in-game minutes.
    """

    __slots__ = ['_minutes']

    _MINUTES_PER_UNIT: ClassVar[int] = 1

    def __init__(self, amount: float) -> None:
        if not isfinite(amount) or amount < 0:
            raise InvalidValueError(f'{self.__class__.__name__} needs a finite amount of zero or more, received {amount!r}')
        self._minutes: int = self._to_whole_minutes(amount * self._MINUTES_PER_UNIT)

    @override
    def __repr__(self) -> str:
        amount = self._minutes / self._MINUTES_PER_UNIT
        return f'<{self.__class__.__name__} amount={int(amount) if amount.is_integer() else amount}>'

    def __bool__(self) -> bool:
        return self._minutes != 0

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Duration):
            return NotImplemented
        return self._minutes == other._minutes

    @override
    def __hash__(self) -> int:
        return hash(self._minutes)

    def __lt__(self, other: Duration) -> bool:
        try:
            return self._minutes < other._minutes
        except AttributeError:
            return NotImplemented

    def __le__(self, other: Duration) -> bool:
        try:
            return self._minutes <= other._minutes
        except AttributeError:
            return NotImplemented

    def __gt__(self, other: Duration) -> bool:
        try:
            return self._minutes > other._minutes
        except AttributeError:
            return NotImplemented

    def __ge__(self, other: Duration) -> bool:
        try:
            return self._minutes >= other._minutes
        except AttributeError:
            return NotImplemented

    def __add__(self, other: Duration) -> Self:
        try:
            minutes = other._minutes
        except AttributeError:
            return NotImplemented
        return self._from_minutes(self._minutes + minutes)

    def __sub__(self, other: Duration) -> Self:
        try:
            minutes = other._minutes
        except AttributeError:
            return NotImplemented
        return self._from_minutes(self._minutes - minutes)

    def __mul__(self, factor: float) -> Self:
        return self._from_minutes(self._to_whole_minutes(self._minutes * factor))

    def __rmul__(self, factor: float) -> Self:
        return self._from_minutes(self._to_whole_minutes(self._minutes * factor))

    def __truediv__(self, divisor: float) -> Self:
        return self._from_minutes(self._to_whole_minutes(self._minutes / divisor))

    def __floordiv__(self, divisor: int) -> Self:
        return self._from_minutes(self._minutes // divisor)

    @property
    def amount(self) -> float:
        """:class:`float`: Returns the length of the duration in its unit."""
        return self._minutes / self._MINUTES_PER_UNIT

    @property
    def minutes(self) -> int:
        """:class:`int`: Returns the length of the duration in in-game minutes."""
        return self._minutes

    @classmethod
    def _from_minutes(cls, minutes: int) -> Self:
        if minutes < 0:
            raise InvalidValueError(f'{cls.__name__} cannot be negative, received {minutes} minutes')
        duration = object.__new__(cls)
        duration._minutes = minutes
        return duration

    def _to_whole_minutes(self, minutes: float) -> int:
        if not isfinite(minutes):
            raise InvalidValueError(f'{self.__class__.__name__} needs a finite length, received {minutes!r} minutes')
        whole = round(minutes)
        if abs(minutes - whole) > _ROUNDING_TOLERANCE:
            raise InvalidValueError(
                f'{self.__class__.__name__} needs to add up to whole in-game minutes, received {minutes!r} minutes'
            )
        return whole

__all__ = ['Duration']
