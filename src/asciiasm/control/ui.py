"""todo"""

from unicurses import move, addstr, refresh, getstr
from .commands import Command
from ..editor import canvas

class Session:

    def __init__(self, scr) -> None:
        self.canvas = canvas.Canvas()
        self.scr = scr

    def take_input(self) -> Command:
        move(self.scr.getmaxy() - 1, 0)
        addstr("Enter command: ")
        refresh()
        command = getstr().decode("utf-8")
        return Command(command)

    def display_canvas(self):
        for line in self.canvas.serialise().split("\n"):
            addstr(line + "\n")

    def execute(self, command: Command) -> None:
        command.command_func(*command.args)
        
