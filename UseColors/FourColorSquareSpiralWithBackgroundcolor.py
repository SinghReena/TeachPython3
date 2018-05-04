#FourColorSquareSpiralWithBackgroundcolor.py

import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["brown", "green", "red","dark blue"]
for x in range(100):
    t.pencolor(colors [x%4])
    t.forward(2*x)
    t.left(91)
