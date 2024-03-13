import curses
from curses import wrapper

# to initialize curses with the program and restores the terminal once we're finished


def main(stdscr):  # means the standard output of the screen
    curses.init_pair(
        1, curses.COLOR_GREEN, curses.COLOR_BLACK
    )  # 1 is the reference to this color definition
    curses.init_pair(
        2, curses.COLOR_RED, curses.COLOR_BLACK
    )  # First color is for foreground and second for background
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(1, 5, "Hello there!")  # To start one line down and in position [0]
    # stdscr.addstr(1, 5, "Hello there!") will concatenate with substitution
    stdscr.refresh()
    key = (
        stdscr.getkey()
    )  # So that it waits for the user to do something before closing the program
    print(key)


wrapper(main)
