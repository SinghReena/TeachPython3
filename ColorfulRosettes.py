# ColorfulRosettes.py
import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
t.width(3)
# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?", 6))
for x in range(number_of_circles):
    t.pencolor('red')
    t.circle(100)
    t.pencolor('yellow')
    t.circle(75)
    t.pencolor('green')
    t.circle(50)
    t.pencolor('blue')
    t.circle(25)
    t.pencolor('purple')
    t.circle(15)
    t.left(360/number_of_circles)

