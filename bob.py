def start():
    print("You wake up in a dark, square room. In the middle of the room is a box, and there are four doors, one on each side of the room.")
    print("You can go north, east, south, or west. You can also open the box.")
    print("1. Go north")
    print("2. Go east")
    print("3. Go south")
    print("4. Go west")
    print("5. Open the box")
    choice = input("What do you choose? ")
    if choice == "1":
        northroom()
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
##def northRoom():
##
##def eastRoom():
##
##def southRoom():
##
##def westRoom():
##
##def bomb():

start()
