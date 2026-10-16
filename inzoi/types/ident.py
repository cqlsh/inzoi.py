"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from typing import override

from ..errors import InvalidValueError

class Ident:
    """Represents an identifier the game uses to refer to something, such as a buff or a skill.

    Identifiers of different types are never equal, even if their raw identifiers match. This
    class is not meant to be used directly, use one of its subclasses such as :class:`BuffId`
    or :class:`SkillId` instead.

    .. container:: operations

        .. describe:: x == y

            Checks if two identifiers are equal.

        .. describe:: x != y

            Checks if two identifiers are not equal.

        .. describe:: hash(x)

            Returns the identifier's hash.

        .. describe:: str(x)

            Returns the raw identifier.

    Parameters
    -----------
    id: :class:`str`
        The raw identifier. Must not be empty.
    """

    __slots__ = ['_id']

    def __init__(self, id: str) -> None:
        if not id.strip():
            raise InvalidValueError(f'{self.__class__.__name__} needs an id, received {id!r}')
        self._id: str = id

    @override
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id={self._id!r}>'

    @override
    def __str__(self) -> str:
        return self._id

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ident) or type(other) is not type(self):
            return NotImplemented
        return self._id == other._id

    @override
    def __hash__(self) -> int:
        return hash((self.__class__, self._id))

    @property
    def id(self) -> str:
        """:class:`str`: Returns the raw identifier."""
        return self._id

__all__ = ['Ident']