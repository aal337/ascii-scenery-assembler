"""todo"""

import unicurses
from .commands import Command
from ..editor import canvas

class Session:
    def __init__(self) -> None:
        # unicurses things todo
        self.canvas = canvas.Canvas()

    def take_input(self, command: str) -> Command:
        return Command(command)

    def display_canvas(self):
        
