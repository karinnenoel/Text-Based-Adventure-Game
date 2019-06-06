def start():
    print("You wake up in a dark, square room. The only things you have are a sword, some water, and some food. In the middle of the room there is a box. There are four doors and one is on each side of the room.")
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
            roomone = input("What do you choose?")
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
                start()
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
            print("The room is empty and there is no exit.")
            print("You take a step and stand in the metal doorway.")
            print("Then you ready your sword and you chop off the venus flytrap's head.")
            Roomthree = input("Would you like to go back to the main room? Yes? or No?. ")
            if Roomthree =="Yes":
                start()
            elif Roomthree =="No":
                exit()
        else:
            print("Choose from the options I give you! Oi vey! Why must you be so difficult?")
        
    
    def westRoom():
        print("you walk into a room you have a good felling")
        print("a man is right infront of you how like like a docter")
        print("the man did not see you")
        print("do you talk to the man 1")
        print("do you attack the man 2")
        print("do you back to door 3")
        RoomFour =input("what do you choose?")
        if RoomFour == "1":
            print("the man look at you")
            print("with out a sound the man attack you")
            print("do you run 1")
            print("do you fight 2")
            print("you try to talk to him 3")
            manroom = input("what do you do")
            if manroom == "1":
                print ("you die")
                print ("do you want to keep going yes or no")
                manroomone = input ("what do you do")
                if manroomone == "yes":
                    start()
                elif manroomone == "no":
                    exit()
                else:
                    ("no more")
                    westRoom()
            elif manroom == "2":
                print ("you die")
                print ("do you want to keep going yes or no")
                manroomone = input ("what do you do")
                if manroomone == "yes":
                    start()
                elif manroomone == "no":
                    exit()
                else:
                    ("no more")
                    westRoom()
            elif manroom == "3":
                print ("you die")
                print ("do you want to keep going yes or no")
                manroomone = input ("what do you do")
                if manroomone == "yes":
                    start()
                elif manroomone == "no":
                    exit()
                else:
                    ("no more")
                    westRoom()

            else:
                print("stop that no more")
                dathManroom = input ("yes or no")
                if deathManroom == "yes":
                    start()
                elif deathManroom == "no":
                    exit()
                else:
                    print("stop that")
                    westRoom()
        elif RoomFour == "2":
            print("you die")
            print("1 to go back")
            print("2 to stop")
            manroomone = input ("what do you do")
            if manroomone == "yes":
                start()
            elif manroomone == "no":
                exit()
            else:
                print ("no more")
                westRoom()
        elif RoomFour == "3":
            print ("ok")
            start()
        else:
            print ("stop that")
            westRoom()
