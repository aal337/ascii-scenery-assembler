"""Save a canvas."""

from pathlib import Path
from asciiasm.editor.canvas import Canvas


def save_image(canvas: Canvas, path: Path):
    """Saves rendered canvas to a file."""
    with open(path, encoding="UTF-8") as f:
        f.write(canvas.serialise())
