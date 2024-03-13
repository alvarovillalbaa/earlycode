import pygame
import random

pygame.init()

HEIGHT, WIDTH = 500, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (229, 128, 128)
GREY = (177, 182, 175)
BLUE = (131, 197, 230)

button_font = pygame.font.SysFont("comicsans", 20)
guess_font = pygame.font.SysFont("arial", 25)
lost_font = pygame.font.SysFont("comicsans", 50)
word = " "
buttons = []  # To create variables even though they're empty or have 0 value
guessed = []
pics = [
    pygame.image.load("PICS/hangman0.png"),
    pygame.image.load("PICS/hangman1.png"),
    pygame.image.load("PICS/hangman2.png"),
    pygame.image.load("PICS/hangman3.png"),
    pygame.image.load("PICS/hangman4.png"),
    pygame.image.load("PICS/hangman5.png"),
    pygame.image.load("PICS/hangman6.png"),
]

limbs = 0


def redraw_game_window():
    # Why redefining???
    global guessed
    global pics
    global limbs

    WINDOW.fill(GREY)
    # Defining the buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(
                WINDOW, BLACK, (buttons[i][1], buttons[i][2], buttons[i][3])
            )
            pygame.draw.circle(
                WINDOW, buttons[i][0], buttons[i][1], buttons[i][2], buttons[i][3] - 2
            )
