"""Main entry point for application."""

from unicurses import *
from .editor import canvas, sprites
from .control import commands, ui
from .files import load, save


def main():
    """Run the main application control flow."""
    main_canvas = canvas.Canvas()
    stdscr = initscr()
    # i know that i don't know if this will work
    session = ui.Session(stdscr)
    while True:
        command = session.take_input()
        session.execute(command)


if __name__ == "__main__":
    main()
