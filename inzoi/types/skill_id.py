"""
inzoi.py License

Copyright (c) 2026-present cqlsh

This file is part of inzoi.py. You may use it and share it unchanged, but you may
not distribute changed versions of it. See the LICENSE file for the full terms.
"""

from __future__ import annotations

from .ident import Ident

class SkillId(Ident):
    """Represents the identifier of a skill.

    Parts of the game also call this identifier the skill name.

    .. note::

        A complete list of the game's skill identifiers is not available yet. Consider passing
        the identifier in as a parameter from the Mod Kit.
    """

    __slots__ = ()

__all__ = ['SkillId']