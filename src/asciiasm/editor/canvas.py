"""Provide canvas editing and rendering utility."""

from pathlib import Path
from .sprites import Sprite

class Canvas:
    """Canvas on which sprites are placed."""

    sprites: list[Sprite]

    def serialise(self) -> str:
        """Return a string representation of the canvas."""
        return ""

    def files(self) -> dict[Path, Sprite]:
        """Return a list of files to save as work progress."""
        return {Path(""): Sprite("")}

    def add_sprite(self, sprite: Sprite):
        """Add a sprite to the canvas."""
        self.sprites.append(sprite)
