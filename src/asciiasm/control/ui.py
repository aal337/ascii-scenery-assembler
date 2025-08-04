"""todo"""

from pathlib import Path
from unicurses import move, addstr, refresh, getstr
from ..editor import canvas, sprites
from ..files import load, save

class Session:
    sprites: dict[str, sprites.Sprite]

    def __init__(self, scr) -> None:
        self.canvas = canvas.Canvas()
        self.scr = scr

    def take_input(self) -> str:
        move(self.scr.getmaxy() - 1, 0)
        addstr("Enter command: ")
        refresh()
        command = getstr().decode("utf-8")
        return command

    def display_canvas(self):
        for line in self.canvas.serialise().split("\n"):
            addstr(line + "\n")

    def execute(self, command: str) -> None:
        command_words = command.split(" ")
        match " ".join(command_words[:2]):
            case "place sprite":
                self.canvas.add_sprite(self.sprites[command_words[2]])
            case "save canvas":
                save.save_image(self.canvas, Path(command_words[2]))
            case "load sprite":
                sprite = load.load_sprite(Path(command_words[2]))
                self.sprites[sprite.name] = sprite
