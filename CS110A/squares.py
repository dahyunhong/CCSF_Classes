import turtle
import math

screen = turtle.Screen()
screen.bgcolor("yellow")
ted = turtle.Turtle()
sideLength = 300

number = int(input("How many squares? "))

for i in range(number):
    for i in range(4):
        ted.forward(sideLength)
        ted.left(90)
    ted.forward(sideLength/2)
    sideLength = sideLength/math.sqrt(2)
    ted.left(45)


screen.exitonclick()
