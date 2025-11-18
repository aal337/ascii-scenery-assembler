"""Main entry point for application."""

import sys
from unicurses import initscr, endwin, refresh, clear
from asciiasm.control import ui


def main():
    """Run the main application control flow."""
    stdscr = initscr()
    session = ui.Session(stdscr)
    try:
        clear()
        refresh()
        while True:
            command = session.take_input()
            session.execute(command)
            session.display_canvas()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        endwin()
        print(*session.command_log, sep="\n")


if __name__ == "__main__":
    main()
