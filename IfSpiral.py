#IfSpiral.py

answer = input("Do you want to see a spiral? yes/no:")
if answer == 'yes':
    print("Working...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("Okay, we're done!")
