import random

inventory = [''] #this has to have something otherwise it'll run the for loop in the def 0 times.
quit = False


def bob(chance):    
    global inventory
    global quit
    num = random.randrange(0,100)
    if chance == "dungeon":
        for elem in inventory: # elem goes through all elements
            if elem == 'Luckcharm':
                if num <5:
                    quit = True
                    print("You fall down a hole and are never seen again")
                elif num <25:
                    quit = True
                    print("You are suddenly teleported in a field of grass. You escape")
                else:
                    print("nothing happened")
            else:
                if num <10:
                    quit = True
                    print("You fall down a hole and are never seen again")
                else:
                    print("nothing happened")

room = 1
while quit == False:
    
        if room == 1:
            print("You're in a dull looking cell, it appears run down as parts of the iron bars look to be destroyed enough to squeez through, you can move (e)ast.")
            choice = input()
            bob("dungeon")
            if choice.lower() == 'e':  
                room = 2
            else:
                print("that's not an option.")
        if room == 2:
            print("You're in room 2, you can move west or south.")
            choice = input()
            bob("dungeon")
            if choice.lower() == 'w':
                room = 1
            elif choice.lower() == 's':
                room = 3
            else:
                print("that's not an option.")
        if room == 3:
            print("You're in room 3, you can move North, South or East.")
            choice = input()
            bob("dungeon")
            if choice.lower() == 'n':
                room = 2
            elif choice.lower() == 's':
                room = 4
            else:
                print("that's not an option.")
        if room == 4:
            print("You're in room 4 you can move north.")
            print("In your vision you see something, when you walk up to it you see that it looks like some type of charm")
            choice = input()
            bob("dungeon")
            if choice.lower() == 'n':
                room = 3
            if choice.lower() == 'p':
                inventory.append("Luckcharm")
                print("You pick up the charm")
            else:
                print("that's not an option")