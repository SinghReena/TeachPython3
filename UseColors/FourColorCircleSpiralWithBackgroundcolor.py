#FourColorCircleSpiralWithBackgroundcolor.py

import turtle
t=turtle.Pen()
turtle.bgcolor("pink")
t.speed(0)
colors = ["brown", "green", "red","dark blue"]
for x in range(100):
    t.pencolor(colors [x%4])
    t.circle(2*x)
    t.left(95)
