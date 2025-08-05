"""Main entry point for application."""

import sys
from unicurses import initscr, endwin, refresh, clear
from asciiasm.control import ui


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
    except Exception as e:
        endwin()
        raise e


if __name__ == "__main__":
    main()
