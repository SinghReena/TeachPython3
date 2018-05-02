#FourColorRectangle.py

import turtle

diffcolors=[ 'orange','red', 'purple', 'yellow']
        
t=turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(diffcolors[x%4])
    t.width(x/100+1)
    t.forward(x)        
    t.left(90)
