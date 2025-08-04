"""Main entry point for application."""

import sys
from unicurses import initscr, endwin, refresh, clear
from asciiasm.editor import canvas, sprites
from asciiasm.control import ui
from asciiasm.files import load, save


def main():
    """Run the main application control flow."""
    stdscr = initscr()
    try:
        clear()
        refresh()
        session = ui.Session(stdscr)
        while True:
            command = session.take_input()
            session.execute(command)
            session.display_canvas()
    except KeyboardInterrupt:
        endwin()
        sys.exit(0)


if __name__ == "__main__":
    main()
