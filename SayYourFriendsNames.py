# SayYourFriendsNames.py - lets everybody print their friend's name on the screen
# Ask the user for their name
name = input("Can I know ur name please :")
# Keep printing names until we want to quit
while name != "":
    # Print friend's name 
    for x in range(1):
        # Print their name followed by a space, not a new line
        print(name, end = " ")
    print()   # After the for loop, skip down to the next line
    # Ask for another name, or quit
    name = input("Type your friend's name , or just hit [ENTER] to quit: ")
print("Thanks for telling ur all friends names!")

