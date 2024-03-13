from configparser import MissingSectionHeaderError
import random
import string
from words import words

# Once we've created a python library in the same folder, we can easily access it
# Should integrate pygame to draw the hanged stickman

tries = 9
underscore = "_"
print(
    "This is Hangman! You've got 9 oportunities to guess the word! Try to fill the blanks. \n"
)


def hangman(words):
    word = random.choice(words).upper()
    misses = 0
    letter = " "
    i = 0
    n = 0
    while misses < tries:
        while i in word:  # Looping through evrey letter in the word
            if letter.upper() == word[i]:
                underscore = letter.upper()
                n += 1
        if n == 0:
            print("Sorry, you've missed! Try again.")
        else:
            print("Congrats! You've guessed one letter!")


def main():
    hangman(words)


main()
