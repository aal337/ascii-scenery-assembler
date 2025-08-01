"""todo"""

from unicurses import *
from .commands import Command
from ..editor import canvas

class Session:

    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.canvas = canvas.Canvas()

    def take_input(self, command: str) -> Command:
        return Command(command)

    def display_canvas(self):
        pass

    def execute(self, command: Command) -> None:
        pass
        
