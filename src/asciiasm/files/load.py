"""Provide sprite loading utility."""

from os import listdir
from pathlib import Path
from asciiasm.editor.sprites import Sprite
from asciiasm.editor.canvas import Canvas


def load_sprite(file_path: Path) -> Sprite:
    """Load a sprite from a text file."""
    with open(file_path, encoding="UTF-8") as f:
        sprite = Sprite(file_path, f.read())
    return sprite


def load_canvas(dir_path: Path) -> Canvas:
    """Load a canvas and continue where user left off."""
    canvas = Canvas()
    for file_name in listdir(dir_path):
        canvas.add_sprite(load_sprite(dir_path / file_name))
    return canvas
