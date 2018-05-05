#ColorSquareSpiral2.py
import turtle
t=turtle.Pen()
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green']
for x in range(700):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)


