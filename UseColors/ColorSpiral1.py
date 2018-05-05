# ColorSpiral1.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6 Totalsides for some cool shapes!
Totalsides = 3
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x%Totalsides])
    t.forward(x * 3/Totalsides + x)
    t.left(360/Totalsides + 1)
    t.width(x*Totalsides/200)
