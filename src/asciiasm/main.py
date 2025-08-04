"""Main entry point for application."""

import sys
from unicurses import *
from .editor import canvas, sprites
from .control import commands, ui
from .files import load, save


def main():
    """Run the main application control flow."""
    stdscr = initscr()
    try:
        session = ui.Session(stdscr)
        while True:
            command = session.take_input()
            session.execute(command)
    except KeyboardInterrupt:
        endwin()
        sys.exit(0)


if __name__ == "__main__":
    main()
