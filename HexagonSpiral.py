#HexagonSpiral.py

import turtle

diffcolors=['green', 'yellow', 'orange','red', 'purple', 'blue']
        
t=turtle.Pen()
turtle.bgcolor('white')

for x in range(360):
    t.pencolor(diffcolors[x%6])
    t.width(x/100+1)
    t.forward(x)        
    t.left(59)
