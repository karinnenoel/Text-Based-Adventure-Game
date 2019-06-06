import time
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
            roomone = input("What do you choose? ")
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
        roomTwo = input ("What do you choose? ")
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
        roomThree = input("What do you chose? ")      
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
        print("You walk into the room and you get a good feeling.")
        print("A man is right in front of you. He looks like a doctor.")
        print("The man did not see you.")
        print("Do you talk to the man? Option - 1")
        print("Do you attack the man? Option - 2")
        print("Or do you sneak back to the main room? Option - 3")
    RoomFour =input("What do you choose? ")
    if RoomFour == "1":
        print("The man turns around and looks at you.")
        print("Without a sound the man attacks you.")
        print("Do you run Option? - 1")
        print("Do you fight Option? - 2")
        print("Or do you try to talk to him? Option - 3")
        manroom = input("What do you do? ")
        if manroom == "1":
            print ("He manages to chase you down. Then he kills you.")
            print ("Do you want to keep going? Yes? or No?")
            manroomone = input ("What do you do? ")
        if manroomone == "Yes":
                start()
        elif manroomone == "No":
                exit()
        else:
            ("Choose a valid option.")
            westRoom()
        if manroom == "2":
                print ("He notices you reach for your sword but he kills you before you can grab it.")
                print ("Do you want to keep going? Yes? or No?")
                manroomone = input ("What do you do? ")
                if manroomone == "Yes":
                    start()
                elif manroomone == "No":
                    exit()
                else:
                    print("Please choose a valid option my d00de.")
                    westRoom()
        elif RoomFour == "2":
            print("You swing your sword to hard and you also miss. Then you loose balance and trip. The man sees that you were going to attack so he kills you.")
            print("Would you like to respawn?")
            print("Yes? or No?")
            manroomone = input ("What do you do? ")
            if manroomone == "Yes":
                start()
            elif manroomone == "No":
                exit()
            else:
                print ("Choose a valid option.")
                westRoom()
        elif RoomFour == "3":
            print ("He does not have time for your small talk. He kills you.")
            print("Would you like to respawn?")
            print("Yes? or No?")
            maiguy = input ("What would you like to do?")
            if maiguy == "Yes":
             start()
            elif maiguy == "No":
                exit()
            else:
             print ("Please choose a valid option.")
            westRoom()

    def bomb():
        print("You open the box.")
        print("Then you feel it")
        print("A loud sound can be heard and now you see it")
        print("Past versions of you are opening the box")
        print("You cry out but it to late the loop has begun. You will be stuck here forever watching yourself open the same box.")
        print("The End.")
        time.sleep(60)
        start()
    
        
        
                   
                   
                

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









start()









