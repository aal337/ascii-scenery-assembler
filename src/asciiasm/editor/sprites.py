"""Provide sprite utility.
Filling whitespace recognition and stripping of surrounding whitespace.
"""

import numpy as np

class Sprite:
    """Represent a sprite that can be placed on a canvas."""

    name: str
    height: int
    width: int
    positions: list[tuple[int, int]]
    grid: np.ndarray
    text: str

    def __init__(self, name: str, text: str) -> None:
        self.name = name
        self.text = text
        self.height = len(line_list := text.split("\n"))
        self.width = max(map(len, line_list))
        self.positions = []
        self.grid = np.array([[char for char in line] for line in line_list])

    def serialise(self) -> str:
        """Return a string representation of the sprite."""
        return self.text

    def transparentize_whitespace(self) -> None:
        """Strip outer whitespace and replace it with None."""
        def config(*args):
            return {"takes height": args[0], "j start": args[1], "j height": args[2], "sign": args[3]}
        orientations = {"left": {"takes height" True: "j start": 0, "j height": False, "sign": 1},
        "right": config(True, self.width, False, -1), "top": config(False, 0, True, 1), "bottom": config(False, self.height, True, -1)}
        for orientation, values in orientations.items():
            for i in range(self.height if values["takes height"] else self.width): # self.height, width of current line, width of current line
                j = values["j start"] # length of current line, 0, self.height
                while pointer := (self.grid[i][j] if not values["j height"] else self.grid[j][i]) in {" ", None}: # i,j , j,i , j,i
                    pointer = None # same
                    j += values["sign"] # -1 for right and bottom