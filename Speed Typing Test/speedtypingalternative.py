import curses
from curses import wrapper
import time
import random

# We refer to key as the user input through the keyboard
# to initialize curses with the program and restores the terminal once we're finished


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(
        "Welcome to the Speed Typing Test!"
    )  # To start one line down and in position [0]
    # stdscr.addstr(1, 5, "Hello there!") will concatenate with substitution
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:  # coloring the txt depending on if it's correct
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)  # Overlaying text


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []

    wpm = 0
    start_time = time.time()  # keeps track of the starting time
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(
            time.time() - start_time, 1
        )  # We use max here to avoid us giving a zero division problem
        wpm = round(
            (len(current_text) / (time_elapsed / 60)) / 5
        )  # Assuming an average 5 letter per word

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:  # turns a string into an argument
            stdscr.nodelay(False)
            break

        try:  # if not tried, program would crash
            key = stdscr.getkey()  # This waits for them to write something
        except:
            continue

        if ord(key) == 27:  # Creating some exit key(escape)
            break
        if key in (
            "KEY_BACKSPACE",
            "\b",
            "\x7f",
        ):  # Creating backspace key with all its possible formats
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(
            target_text
        ):  # To avoid being able to keep writing if it surpasses the length of the text
            current_text.append(key)


def main(stdscr):  # means the standard output of the screen
    curses.init_pair(
        1, curses.COLOR_GREEN, curses.COLOR_BLACK
    )  # 1 is the reference to this color definition
    curses.init_pair(
        2, curses.COLOR_RED, curses.COLOR_BLACK
    )  # First color is for foreground and second for background
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    # key = (stdscr.getkey() ) # So that it waits for the user to do something before closing the program
    # print(key)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to cntinue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


wrapper(main)
