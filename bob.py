def start():
    print("You wake up in a dark, square room. In the middle of the room there is a box. There are four doors and one is on each side of the room.")
    print("You can go North, East, South, or West. You can also open the mysterious box.")
    print("1. Go North")
    print("2. Go East")
    print("3. Go South")
    print("4. Go West")
    print("5. Open the box")
    choice = input("What do you choose? ") 
    def northRoom():
        print("You enter the north room and the walls are covered in blue paint. There is an ethereal looking light beaming in the center of the floor.")
        print("Will you go back to the door? Option - 1")
        print("Or will you go to light? Option - 2")
        roomOne = input ("What do you choose? ")
        if roomOne == "1":
            start()
        elif roomOne == "2":
            print ("You were burnt to a crisp lol. Would you like to respawn?")
            print ("Yes? or No?")
            roomone = input("what you choose? ")
            if roomone =="Yes":
                start()
            elif roomone =="No":
                exit() 
        else:
            print ("Stop that. Pick 1 or 2.")
    def eastRoom():
        print("You walk into a yellow room.")
        print("A bad feeling starts to grow in the pit of your stomach. Then you look up and see it!")
        print("A giant but harmless looking spider is crawling on the ceiling.")
        print("Will you run out of the room? Option - 1")
        print("Or will you stay and fight? Option - 2")
        roomTwo = input ("what do you choose? ")
        if roomTwo == "1":
            start()
        elif roomTwo =="2":
            print ("You became Sally's lunch. Would you like to respawn?")
            print ("Yes? or No?")
            roomtwo = input("what you  choose? ")
            if roomtwo =="Yes":
                start()
            elif roomtwo =="No":
                exit()
        else:
            print("I told you last time! Pick 1 or 2! *Le sigh*")
        
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
##def southRoom():
##
##def westRoom():
##
##def bomb():

start()
