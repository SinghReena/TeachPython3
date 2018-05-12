# SayNamesMultipleTimes.py - lets everybody print their name on the screen
# Ask the user for their name
name = input("Can I know your name please: ")
# Keep printing names until we want to quit
while name != "":
    # Print their name 35 times
    for x in range(35):
        # Print their name followed by a space, not a new line
        print(name, end = " ")
    print()   # After the for loop, skip down to the next line
    # Ask for another name, or quit
    name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for printing names 35 times!")

