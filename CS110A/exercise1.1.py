
#A blue line segment from (20, 30) to 50 pixels, with small dots at each end.

#Draw a square.

#Draw a hexagon(Figure with six sides).

#An equilateral triangle with each side having length 100 pixels. (Note: The interior ­angles will each have measure 60°.)

import turtle

turtle.penup()
turtle.color('blue')
turtle.goto(20,30)
turtle.pendown()
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.penup()

turtle.forward(200)
turtle.pendown()
turtle.color('black')
for i in range(4):
  turtle.forward(100)
  turtle.left(90)
print(i)

turtle.penup()
turtle.forward(200)
turtle.pendown()

for i in range(6):
  turtle.forward(50)
  turtle.left(60)
  print(i)

turtle.penup()
turtle.forward(200)
turtle.pendown()

for i in range(3):
  turtle.forward(100)
  turtle.left(120)
  print(i)