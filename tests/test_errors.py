"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

import pytest

from inzoi import errors
from inzoi.errors import InvalidValueError, InzoiException, ModDefinitionError

class TestErrors:
    """Checks the promises our exceptions make to everyone who catches them."""

    __slots__ = ()

    @pytest.mark.parametrize('name', errors.__all__)
    def test_every_exception_is_an_inzoi_exception(self, name: str) -> None:
        """Catching InzoiException has to catch everything inzoi.py raises."""
        assert issubclass(getattr(errors, name), InzoiException)

    def test_all_lists_every_exception(self) -> None:
        """A new exception that someone forgot to add to __all__ should not slip through."""
        defined = {
            name
            for name, value in vars(errors).items()
            if isinstance(value, type) and issubclass(value, BaseException) and value.__module__ == errors.__name__
        }
        assert defined == set(errors.__all__)

    def test_inzoi_exception_is_a_regular_exception(self) -> None:
        """A plain ``except Exception`` still catches our exceptions."""
        assert issubclass(InzoiException, Exception)

    def test_invalid_value_error_is_a_value_error(self) -> None:
        """Code that only knows about ValueError still catches a bad game value."""
        with pytest.raises(ValueError):
            raise InvalidValueError('minutes cannot be negative')

    def test_message_is_kept(self) -> None:
        """People see exactly the message we wrote."""
        assert str(ModDefinitionError('missing version')) == 'missing version'