def start():
    print("You wake up in a dark, square room. In the middle of the room is a box, and there are four doors, one on each side of the room.")
    print("You can go north, east, south, or west. You can also open the box.")
    print("1. Go north")
    print("2. Go east")
    print("3. Go south")
    print("4. Go west")
    print("5. Open the box")
    choice = input("What do you choose? ")
    start 
    def northRoom():
        print("youer in a blue room with a powerful light coming in")
        print("go back to door is 1")
        print("go to light 2")
        roomone = input ("what do you choose? ")
        if roomone == "1":
            start()
        elif roomone == "2":
            print ("you die and go back to start")
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
