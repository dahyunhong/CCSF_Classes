import turtle


def get_n_sides():
    number = int(input('Enter the number between 3 and 24 inclusive: '))
    while number < 3 or number > 24:
        number = int(input('Enter the number between 3 and 24 inclusive: '))
    return number


def draw_polygon(n_side):
    draw = turtle.Turtle()
    sideLength = 200
    turnAngle = 360 / n_side
    for i in range(n_side):
        draw.forward(sideLength)
        draw.left(turnAngle)


def main():
    screen = turtle.Screen()
    num = get_n_sides()
    draw_polygon(num)
    screen.exitonclick()


main()
