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
            northRoom()
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
            roomtwo = input("What do you choose? ")
            if roomtwo =="Yes":
?                start()
            elif roomtwo =="No":
                exit()
        else:
             print("I told you last time! Pick 1 or 2! *Le sigh*")
             eastRoom() 
        

    def southRoom():
        print("When you walk into the room you notice a mess of green vines tangled against the cracked stone walls.")
        print("You look to your left and see an old wooden door that is about to come off the hinges.")
        print("You look to your right and see a strong metal door.")
        print("What will your choose?")
        print("Go into the room on the left? Option - 1")
        print("Or will you go to the room on the right? Option - 2")
        roomThree = input("What do you chose?")      
        if roomThree == "1":
            print("When you open the wooden door a giant venus flytrap lunges out and swallows you whole.")
            print("Would you like to respawn?")
            print("Yes? or No?")
            roomthree = input("What do you choose? ")
            if roomthree =="Yes":
                start()
            elif roomthree =="No":
                exit()
        elif roomThree == "2":
            print("When you open the metal door the wooden door springs open and a giant venus flytrap trys swalow you whole.")
            print("Luckily, you chose the metal door and the venus flytrap could not reach you")
            print("You look around the room and find a key and a sword.")
            


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
##def westRoom():
##
##def bomb():

start()
