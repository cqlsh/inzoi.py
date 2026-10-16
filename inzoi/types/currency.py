"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from ..errors import InvalidValueError, ModDefinitionError
from .value import Value

if TYPE_CHECKING:
    from typing import ClassVar, Self

class Currency(Value):
    """Represents an amount of a currency.

    Every currency is its own type, identified by the id the game uses for it. Amounts are always
    whole numbers, and currencies of different types cannot be mixed with each other.

    This class is not meant to be used directly. Use :class:`Mew` for the game's own currency, or
    subclass it and pass the id of the currency as a class argument.

    Example
    --------

    .. code-block:: python3

        class FishCoin(inzoi.Currency, id='FishCoin'):
            pass

    .. container:: operations

        .. describe:: x // n

            Returns the amount divided by a number, rounded down.

    All operations of :class:`Value` are supported as well. Dividing with ``/`` only works if the
    result is a whole number.

    .. note::

        Whether and how mods can add currencies of their own has not been confirmed yet.

    Attributes
    -----------
    id: :class:`str`
        The id of the currency in the game.

    Parameters
    -----------
    amount: :class:`int`
        The amount of the currency. Negative amounts take currency away.
    """

    __slots__ = ()

    id: ClassVar[str]

    def __init__(self, amount: int) -> None:
        if type(self) is Currency:
            raise ModDefinitionError(
                "Currency can't be used directly, use inzoi.Mew or define one like class FishCoin(Currency, id='FishCoin')"
            )
        super().__init__(amount)
        whole = int(amount)
        if whole != amount:
            raise InvalidValueError(f'{self.__class__.__name__} needs a whole amount, received {amount!r}')
        self._amount = whole

    @override
    def __init_subclass__(cls, *, id: str | None = None) -> None:
        super().__init_subclass__()
        if id is None or not id.strip():
            raise ModDefinitionError(
                f"{cls.__name__} needs the id of its currency, like class {cls.__name__}(Currency, id='{cls.__name__}')"
            )
        cls.id = id

    def __floordiv__(self, divisor: int) -> Self:
        return type(self)(int(self._amount) // divisor)

    @property
    @override
    def amount(self) -> int:
        """:class:`int`: Returns the raw amount of the currency."""
        return int(self._amount)

__all__ = ['Currency']