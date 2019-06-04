def start():
    print("You wake up in a dark, square room. In the middle of the room there is a box. There are four doors and one is on each side of the room.")
    print("You can go North, East, South, or West. You can also open the mysterious box.")
    print("1. Go North")
    print("2. Go East")
    print("3. Go South")
    print("4. Go West")
    print("5. Open the box")
    choice = input("What do you choose? ")
    start 
    def northRoom():
        print("You enter the north room. There is an ethereal looking light beaming in the center of the floor.")
        print("Will you go back to the door? Option - 1")
        print("Or will you go to light? Option - 2")
        roomone = input ("What do you choose? ")
        if roomone == "1":
            start()
        elif roomone == "2":
            print ("You were burnt to a crisp lol. Would you like to respawn?")
            print ("Yes? or No?") ## add way to optionally restart the game via user input yes = start no = kill program
            start()
        else:
            print ("stop that")
    if choice == "1":
        northRoom()
    elif choice == "2":
        eastRoom()
    elif choice == "3":
        southRoom()
    elif choice == "4":
        westRoom()
    elif choice == "5":
        bomb()
    else:
        print("No, that's not a valid choice.")



##
##def eastRoom():
##
##def southRoom():
##
##def westRoom():
##
##def bomb():

start()
