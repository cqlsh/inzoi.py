"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

class InzoiException(Exception):
    """Base exception class for inzoi.py

    Ideally speaking, this could be caught to handle any exceptions raised from this library.
    """

    pass

class InvalidValueError(InzoiException, ValueError):
    """Exception that's raised when a value is invalid, e.g. ``Minutes(-5)``.

    This inherits from :exc:`InzoiException` and :exc:`ValueError`.
    """

    pass

class GameUnavailableError(InzoiException):
    """Exception that's raised when a mod tries to access the game from outside of it.

    Mods only run inside the game after they have been built. Use :mod:`inzoi.testing` to run
    a mod outside of the game.
    """

    pass

class ModDefinitionError(InzoiException):
    """Exception that's raised when a mod is defined incorrectly.

    This is raised while the mod is being read, before it is built. Common causes are a missing
    ``version``, a handler parameter that cannot be filled in or two handlers that share the same
    name in Lua.
    """

    pass

__all__ = (
    'InzoiException',
    'InvalidValueError',
    'GameUnavailableError',
    'ModDefinitionError'
)