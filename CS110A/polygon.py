import turtle
screen = turtle.Screen()

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

sideLength = 200
number = int(input('Number of sides:'))
turnAngle = 360 / number
for i in range(number):
    turtle.forward(sideLength)
    turtle.left(turnAngle)

screen.exitonclick()
