"""Provide sprite loading utility."""

from pathlib import Path
from asciiasm.editor.sprites import Sprite


def load_sprite(file_path: Path) -> Sprite:
    """Load a sprite from a text file."""
    with open(file_path, encoding="UTF-8") as f:
        sprite = Sprite(f.read())
    return sprite
