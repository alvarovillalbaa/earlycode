import random

# import re when we need dataframes
# leave a space at the end of the strings when user input is needed

type = input("Do you want to play against the computer? (Yes/No/Other) ")
tries = int(input("How many tries to win? "))
maxNumber = int(input("Introduce the maximum number: "))


def guessVsComputer():
    randomNumber = random.randint(1, maxNumber)
    guess = 0  # To display the 'guess' at all moment
    tried = 0
    while guess != randomNumber:
        while tried < tries:
            guess = int(input(f"Guess a number between 1 and {maxNumber}: "))
            if guess < randomNumber:
                print("Sorry, too low. Guess again.\n")
            elif guess > maxNumber:
                print(f"Introduce a number between 1 and {maxNumber}")
            else:
                print("Sorry, too high. Guess again.\n")
            tried += 1
        if tried == tries:
            print("Sorry, you are out of guesses.\n")
        break
    print(f"Yay, congrats! You've guessed the number {randomNumber}.\n")


def guessVsPlayer():
    number = int(input("Introduce a number. Make sure the opponent doesn't see it!"))
    guess = 0
    tried = 0
    while guess != number:
        while tried < tries:
            guess = int(input(f"Guess a number between 1 and {maxNumber}: "))
            if guess < number:
                print("Sorry, too low. Guess again.\n")
            elif guess > maxNumber:
                print(
                    "Introduce a number between 1 and {maxNumber}!\n"
                )  # Why doesn't this work???
            else:
                print("Sorry, too high. Guess again.\n")

            tried += 1
        if tried == tries:
            print("Sorry, your opponent won.\n")
        break
    print(f"Yay, congrats! You've guessed the number {number}.\n")


def computerGuess():
    number = int(
        input(
            "Introduce a number. Don't worry, the computer won't know which one is it. "
        )
    )
    randomGuess = random.randint(1, maxNumber)
    tried = 0
    while randomGuess != number:
        while tried < tries:
            if randomGuess < number:
                print("The computer missed! Too low.")
                randomGuess += 1
            else:
                print("The computer missed! Too high.")
                randomGuess -= 1
        if tried == tries:
            print("Yay, congrats! The computer couldn't guess your number.\n")
        break
    print(f"Sorry! The computer guessed your number {number}.\n")


def main():
    typeComparison = type.lower()
    if typeComparison == "yes":
        guessVsComputer()
    elif typeComparison == "no":
        guessVsPlayer()
    elif typeComparison == "other":
        computerGuess()
    else:
        print("Please introduce a correct type of game! Yes/No/Other")
    exit()


main()
