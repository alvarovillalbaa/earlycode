import random


def play():
    wins = int(input("Define a score to win: "))
    computerWins = 0
    playerWins = 0

    while computerWins < wins and playerWins < wins:

        user = input(
            "What's your choice?'r' for rock, 'p' for paper, 's' for scissors. "
        )
        computer = random.choice(["r", "p", "s"])

        if user == computer:
            print("It's a tie.\n")

        elif win(user, computer):  # passed if True is met
            playerWins += 1
            print("You win!\n")

        else:
            computerWins += 1
            print("You lost...\n")

    if computerWins == wins:
        print("You lost the game...\n")
    elif playerWins == wins:
        print("You won the game!\n")


# r > s, s > p, p > r
# Function return doesn't print. We would need to print the whole function
# Functions need parameteres when prototyped into another one with variables to be passed
# We don't use return to give back a value because it automatically ends the function


def win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True  # Booleans are mostly used for if been executed


play()
