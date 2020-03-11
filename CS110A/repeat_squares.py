import turtle
screen = turtle.Screen()

turtle.hideturtle()
turtle.speed(0)

sideLength = 4
turtle.penup()
turtle.goto(-4, 4)
turtle.pendown()
turtle.setheading(90)

for i in range(1, 101):
    for j in range(4):
        turtle.forward(i*sideLength)
        turtle.left(90)


screen.exitonclick()
