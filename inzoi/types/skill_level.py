"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from typing import override

from ..errors import InvalidValueError

class SkillLevel:
    """Represents the level of a skill.

    .. container:: operations

        .. describe:: x == y

            Checks if two skill levels are equal.

        .. describe:: x != y

            Checks if two skill levels are not equal.

        .. describe:: x < y

            Checks if a skill level is lower than another.

        .. describe:: x <= y

            Checks if a skill level is lower than or equal to another.

        .. describe:: x > y

            Checks if a skill level is higher than another.

        .. describe:: x >= y

            Checks if a skill level is higher than or equal to another.

        .. describe:: hash(x)

            Returns the skill level's hash.

        .. describe:: int(x)

            Returns the raw skill level.

    .. note::

        The highest level of each skill has not been confirmed yet.

    Parameters
    -----------
    value: :class:`int`
        The raw skill level. Must not be negative.
    """

    __slots__ = ['_value']

    def __init__(self, value: int) -> None:
        if value < 0:
            raise InvalidValueError(f'skill levels cannot be negative, received {value}')
        self._value: int = value

    @override
    def __repr__(self) -> str:
        return f'<SkillLevel value={self._value}>'

    def __int__(self) -> int:
        return self._value

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SkillLevel):
            return NotImplemented
        return self._value == other._value

    @override
    def __hash__(self) -> int:
        return hash(self._value)

    def __lt__(self, other: SkillLevel) -> bool:
        if type(other) is not SkillLevel:
            return NotImplemented
        return self._value < other._value

    def __le__(self, other: SkillLevel) -> bool:
        if type(other) is not SkillLevel:
            return NotImplemented
        return self._value <= other._value

    def __gt__(self, other: SkillLevel) -> bool:
        if type(other) is not SkillLevel:
            return NotImplemented
        return self._value > other._value

    def __ge__(self, other: SkillLevel) -> bool:
        if type(other) is not SkillLevel:
            return NotImplemented
        return self._value >= other._value

    @property
    def value(self) -> int:
        """:class:`int`: Returns the raw skill level."""
        return self._value

__all__ = ['SkillLevel']