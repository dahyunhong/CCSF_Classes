import turtle

screen = turtle.Screen()

turtle.speed(10)
turtle.color('blue')
sideLength = 10
turtle.right(90)

for i in range(25):
    turtle.forward(sideLength*i)
    turtle.left(90)

screen.exitonclick()
