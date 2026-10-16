"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from typing import override

class EntityId:
    """Represents the identifier of an entity in the game, such as a Zoi.

    This is the counterpart of the game's ``FB1EntityId``. Entity identifiers are created by the
    game and handed to your handlers through :class:`Interaction`, so you rarely need to create
    one yourself.

    .. container:: operations

        .. describe:: x == y

            Checks if two entity identifiers refer to the same entity.

        .. describe:: x != y

            Checks if two entity identifiers refer to different entities.

        .. describe:: hash(x)

            Returns the entity identifier's hash.

        .. describe:: int(x)

            Returns the raw entity identifier.

    Parameters
    -----------
    value: :class:`int`
        The raw entity identifier.
    """

    __slots__ = ['_value']

    def __init__(self, value: int) -> None:
        self._value: int = value

    @override
    def __repr__(self) -> str:
        return f'<EntityId value={self._value}>'

    def __int__(self) -> int:
        return self._value

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntityId):
            return NotImplemented
        return self._value == other._value

    @override
    def __hash__(self) -> int:
        return hash(self._value)

    @property
    def value(self) -> int:
        """:class:`int`: Returns the raw entity identifier."""
        return self._value

__all__ = ['EntityId']