import math
import random
import turtle  # module containing turtles with some built-in functionalities
import time

# We almost always implement OOP when creating windowed games. It sets the standards with self definitions(ALWAYS)

WIDTH, HEIGHT = 500, 500

turtles = int(input("Introduce the number of turtles.\n"))

turtle.screensize(WIDTH, HEIGHT)


class Racer(object):
    # We usually use a __init__ object to initialise the object
    def __init__(self, color, position):
        self.position = position
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape("turtle")
        self.turt.color(color)
        self.turt.penup()  # To draw while they move
        self.turt.setpos(position)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.position = (self.position[0], self.position[1] + r)
        self.turt.pendown()
        self.turt.forward(r)  # moves the turtle forwards

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.position)


def setUpFile(name, colors):
    file = open(name, "w")
    for color in colors:
        file.write(color + " 0 \n")
    file.close()


def startGame():
    turtleList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", "grey", "yellow", "orange"]
    start = -(WIDTH / 2) + 20  # Why +20???
    for t in range(turtles):
        newPositionX = start + t * (WIDTH) // turtles
        turtleList.append(racer(colors[t], (newPositionX, -230)))
        turtleList[t].turt.showturtle()

    run = True
    while run:
        for t in turtleList:
            t.move()

        maxColor = []
        maxDistance = 0
        for t in turtleList:
            if t.position[1] > 230 and t.position[1] > maxDistance:
                maxDistance = t.position[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.position[1] > 230 and t.position[1] == maxDistance:
                maxDistance = t.position[1]
                maxColor.append(t.color)

        if len(maxColor) > 0:
            run = False
            print("The winner is: ")
            for WINDOW in maxColor:
                print(WINDOW)

    oldScore = []
    file = open("turtles.txt", "r")
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])

    file.close()

    file = open("scores.txt", "w")

    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + " " + str(entry[1]) + "\n")

    file.close()


start = input("Would you like to play")
startGame()

while True:
    print("-----------------------------------")
    start = input("Would you like to play again")
    startGame()
