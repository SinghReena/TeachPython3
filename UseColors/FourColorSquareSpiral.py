#FourColorSquareSpiral.py

import turtle
t=turtle.Pen() 
t.speed(0)
colors = ["brown", "green", "black","dark blue"]
for x in range(100):
    t.pencolor(colors [x%4])
    t.forward(2*x)
    t.left(51)