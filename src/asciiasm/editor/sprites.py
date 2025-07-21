"""Provide sprite utility.
Filling whitespace recognition and stripping of surrounding whitespace.
"""

import numpy as np

class Sprite:
    """Represent a sprite that can be placed on a canvas."""

    name: str
    height: int
    width: int

    def __init__(self, text: str):
        pass

    def serialise(self) -> str:
        """Return a string representation of the sprite."""
        return ""
