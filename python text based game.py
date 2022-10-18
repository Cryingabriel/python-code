#Add gold into the game so that the player has to pay gold to enter the next area[Done.]
#Maybe make it so when the player dies they go back to the begining without anything that they got[Done ish? Needs more testing.]
#Add it so the players can quit the game hwen they want[Done]
#Make it so that players can see the amount of gold and health when they type g or h[Semi done, finish for all rooms.]
#Make it so that all input is lowercase so it's easier on me[It doesn't work so some reason, ask eli for help.]
#Add an inventory so that player can hold things when added later[Not implemented.]
#Add a sword that spawns in a room that boosts attack[Not implemented.]
#See if I can add healthpotions/aidkits in some later rooms to make beating the game easier[Might add or not. Depends on how hard I want to make the game.]
#Twick potions so that it's easier to die to monsters[Not done.]
#Add final boss for the game[Not implemented.]
#
import random
import time
#function definition
playerhealth=30
gold=0

def monster(biome):
  num = random.randrange(0, 100)
  if biome == "dungeon":
    if num <= 25:
      battlesystem("Zombie")
    elif num <= 45:#30% chance
      battlesystem("Skeleton")
    elif num <= 65:
      battlesystem("Spider")
    elif num <= 100:
      battlesystem("Goblin")
  elif biome == "mansion":
    if num <= 30:
      battlesystem("Scorpion")
    elif num <= 50:#30% chance
      battlesystem("Skeleton")
    elif num <= 79:
      battlesystem("Spider")
    elif num <= 100:
      battlesystem("Goblin")
  elif biome == "forest":
    if num <= 25:
      battlesystem("Mushroom")
    elif num <= 75:#30% chance
      battlesystem("Fairy")
    elif num <= 85:
      battlesystem("Troll")
    elif num <= 100:
      battlesystem("Goblin")
  elif biome == "outside":
    if num <= 25:
      battlesystem("Skeleton")
    elif num <= 75:#30% chance
      battlesystem("Ghost")
    elif num <= 85:
      battlesystem("Zombie")
    elif num <= 100:
      battlesystem("Slime")
#____________________________________________

def battlesystem(monster):
    potion = random.randrange(30,36)
    highpotion = random.randrange(50,55)
    fullpotion = 100
    global playerhealth
    global gold
    if monster == "Zombie":
        monsterhealth = 45
        print("a Zombie has spawned in")
        time.sleep(4)
    elif monster == "Skeleton":
        monsterhealth = 42
        print("a Skeleton has shot at you")
        time.sleep(4)
    elif monster == "Spider":
        monsterhealth = 37
        print("a Spider tried to trap you")
        time.sleep(4)
    elif monster == "Goblin":
        monsterhealth = 36
        print("a Goblin is trying to stab you")
        time.sleep(4)
    elif monster == "Scorpion":
        monsterhealth = 38
        print("A Scorpion is stinging you")
        time.sleep(4)
    elif monster == "Mushroom":
        monsterhealth =48
        print("a mushroom monster tries to poison you")
        time.sleep(4)
    elif monster == "Troll":
        monsterhealth =60
        print("a Troll is trying to squash you")
        time.sleep(4)
    elif monster == "Fairy":
        monsterhealth =39
        print("Fairies start biting at you")
        time.sleep(4)
    elif monster == "Ghost":
        monsterhealth =39
        print("Ghosts are trying take you away")
        time.sleep(4)
    elif monster == "Slime":
        monsterhealth =40
        print("slimes are trying to erode you")
        time.sleep(4)
        
    while monsterhealth>0 and playerhealth >0:
        if monster == "Zombie":
            monsterattack = random.randrange(11, 14)
        elif monster == "Skeleton":
            monsterattack = random.randrange(11,16)
        elif monster == "Spider":
            monsterattack = random.randrange(10,13)
        elif monster == "Goblin":
            monsterattack = random.randrange(13,17)
        elif monster == "Scorpion":
            monsterattack = random.randrange(12,19)
        elif monster == "Troll":
            monsterattack = random.randrange(18,26)
        elif monster == "Fairy":
            monsterattack = random.randrange(13,18)
        elif monster == "Mushroom":
            monsterattack = random.randrange(15,20)
        elif monster == "Ghost":
            monsterattack = random.randrange(17,18)
        elif monster == "Slime":
            monsterattack = random.randrange(19,24)
            
        print("The", monster, "attacks deal", monsterattack, "damage.")
        playerhealth = playerhealth - monsterattack
        time.sleep(3)
        print("your HP is at", playerhealth)
        
        playerattack = random.randrange(13,20)#I had to add 3 damage cause of Eli 
        time.sleep(3)
        print("you deal", playerattack, "damage.")
        time.sleep(3)
        monsterhealth= monsterhealth - playerattack
        time.sleep(3)
        print("the monsters HP is at", monsterhealth)
        time.sleep(3)
    if playerhealth <= 0:# this makes sure that when the player dies the game end
        print("you succumbed to your wounds as your vision slowly fades to black")
        room = 1
        playerhealth = 100
        gold = 0
        time.sleep(3)
        print("you slowly regain consciousness propt up against a familiar looking room")
        time.sleep(3)
    elif monsterhealth<= 0:
        print("you have won.")
        time.sleep(3)
        print("the", monster, "drops a red liqud. when you pick it up some of your wounds disapear.")
        time.sleep(4)
        num2 = random.randrange(0,100)
        monsterdrop = random.randrange(50,100)
        if num2 <=70:
            print("the potion gives you", potion, "health.")
            playerhealth = playerhealth + potion
            print("the", monster, "also drops", monsterdrop, "gold that could be used later.")
            gold = gold + monsterdrop
            print("you now have", gold, "gold")
        elif num2 <=95:
            print("the potion gives you", highpotion, "health.")
            playerhealth = playerhealth + highpotion
            print("the", monster, "also drops", monsterdrop, "gold that could be used later.")
            gold = gold + monsterdrop
            print("you now have", gold, "gold")
        elif num2 <= 100:
            print("the potion gives you", fullpotion, "health.")
            playerhealth = playerhealth + fullpotion
            print("the", monster, "also drops", monsterdrop, "gold that could be used later.")
            gold = gold + monsterdrop
            print("you now have", gold, "gold")
    if playerhealth > 100:
        playerhealth = 100
    time.sleep(2)
    print("your HP has been restored to", playerhealth)

    return playerhealth
#__________game below_______________________________________________________________ 
quit = False
opendoor = False
opendoor1 = False
opendoor2 = False
opendoor3 = False
choice1 = input("do you want to play a game? Yes/No")
if choice1 == 'y' or choice1 == 'Y' or choice1 == 'yes' or choice1 == 'Yes' or choice1 == 'YES':
    time.sleep(3)
    print("you slowly wake up with water driping down you're face, when you open your eyes your inside a cold, dark and damp room. You have no idea how you woke up in here, all you can recall is falling asleep in bed then waking here.through the darkness you can see a vague silhouette coming towards you.")
    room = 1
    time.sleep(8)
    while quit == False:
    
        if room == 1:
            monster("dungeon")
            time.sleep(3)
            print("Your in a dull looking cell, it appears run down as parts of the iron bars look to be destroyed enough to squeez through, you can move (e)ast")
            choice = input()
            if choice == 'e' or choice == 'East' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 2
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health")
            else:
                print("that's not an option")
        if room == 2:
            monster("dungeon")
            time.sleep(3)
            print("your in room 2, you can move west or south")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 1
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 3
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 3:
            monster("dungeon")
            time.sleep(3)
            n = random.randrange(100,300)
            print("your in room 3, you can move north, south or pay to open door to the east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'North' or choice == 'north' or choice == 'NORTH':
                room = 2
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 4
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST' and opendoor == True:
                room = 5
            elif choice == 'pay'and gold >= 450:
                gold -= 450
                opendoor = True
                time.sleep(3)
                print("taking you're gold t6he door magically dissapears before your eye's")
                time.sleep(2)
                print("you now have", gold, "gold")
            elif choice == 'pay' and gold != 450:
                print("you try to pay but realise too late that you don't have enough money and lost 100 gold")
                gold -= n
                time.sleep(3)
                print("you now have", gold, "gold")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 4:
            monster("dungeon")
            time.sleep(3)
            if opendoor == False:
                print("your in room 4, you can move north or pay to open door to the east")
            if opendoor == True:
                print("your in room 4 you can move north or east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North'  or choice == 'NORTH':
                room = 3
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 5:
            print("you enter the room, you find that it's a plain room with nothing in it exept a ladder which seems to lead 'up'.")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 3
            elif choice == 'up' or choice == 'Up' or choice == 'UP' or choice == 'u' or choice == 'U':
                room = 6
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 6:
            monster("mansion")
            time.sleep(3)
            print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west or go back down")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 7
            elif choice == 'd' or choice == 'D' or choice == 'down' or choice == 'Down' or choice == 'DOWN':
                room = 5
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room == 9
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 7:
            monster("mansion")
            time.sleep(3)
            print("your in room 7, you can move north or east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 8
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 6
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 8:
            monster("mansion")
            time.sleep(3)
            print("your in room 8, you can move south")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 7
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 9:
            monster("mansion")
            time.sleep(3)
            print("your in room 9, you can move east or north")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 10
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 6
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 10:
            monster("mansion")
            time.sleep(3)
            n = random.randrange(300,450)
            if opendoor1 == False:
                print("your in room 10, you can move west or pay to open the door leading east")
            if opendoor1 == True:
                print("your in room 10 you can move north or east")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 9
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST' and opendoor1 == True:
                room = 11
            elif choice == 'pay'and gold >= 700:
                gold -= 700
                opendoor1 = True
                time.sleep(3)
                print("taking you're gold t6he door magically dissapears before your eye's")
                time.sleep(2)
                print("you now have", gold, "gold")
            elif choice == 'pay' and gold != 700:
                print("you try to pay but realise too late that you don't have enough money and lost 100 gold")
                gold -= n
                time.sleep(3)
                print("you now have", gold, "gold")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 11:
            monster("outside")
            time.sleep(3)
            n = random.randrange(300,450)
            if opendoor3 == False:
                print("when you look around you find yourself surrounded by greenery of a abandoned garden.It's filled with overgrown vines and weeds all over with countless spiderwebs everywhere, you can move west, south or pay to open a door going east")
            if opendoor3 == True:
                print("your in room 11 you can move west, south or east")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 12
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST' and opendoor3 == True:
                room = 18
            elif choice == 'pay'and gold >= 1000:
                gold -= 1000
                opendoor3 = True
                time.sleep(3)
                print("taking you're gold t6he door magically dissapears before your eye's")
                time.sleep(2)
                print("you now have", gold, "gold")
            elif choice == 'pay' and gold != 1000:
                print("you try to pay but realise too late that you don't have enough money and lost 100 gold")
                gold -= n
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 15
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 12:
            monster("outside")
            time.sleep(3)
            print("your in room 12, you can move west or east")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 13
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 11
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 13:
            monster("outside")
            time.sleep(3)
            print("your in room 13, you can move north or east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 14
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 12
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 14:
            monster("outside")
            time.sleep(3)
            print("your in room 14, you can move south")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 13
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 15:
            monster("outside")
            time.sleep(3)
            print("your in room 15, you can move south or north")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 16
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 11
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 16:
            monster("outside")
            time.sleep(3)
            print("your in room 16, you can move north or west")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 17
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 15
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 17:
            monster("outside")
            time.sleep(3)
            print("your in room 17, you can move east")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 16
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 23
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 18:
            monster("forest")
            time.sleep(3)
            print("your in room 18, you can move west or east")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 11
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 19
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 19:
            monster("forest")
            time.sleep(3)
            print("your in room 19, you can move west, south or north")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 18
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 20
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 21
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 20:
            monster("forest")
            time.sleep(3)
            print("your in room 20, you can move south")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 19
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 21:
            monster("forest")
            n = fandom.randrange(450,1000)
            time.sleep(3)
            if opendoor2 == False:
                print("your in room 10, you can move west or pay to open the door leading east")
            if opendoor2 == True:
                print("your in room 10 you can move north or east")
            print("your in room 21, you can move north, east or open a door to the south")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 22
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 19
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH' and opendoor2 == True:
                room = 23
            elif choice == 'pay'and gold >= 700:
                gold -= 700
                opendoor2 = True
                time.sleep(3)
                print("taking you're gold t6he door magically dissapears before your eye's")
                time.sleep(2)
                print("you now have", gold, "gold")
            elif choice == 'pay' and gold != 1500:
                print("you try to pay but realise too late that you don't have enough money and lost 100 gold")
                gold -= n
                time.sleep(3)
                print("you now have", gold, "gold")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 22:
            monster("forest")
            time.sleep(3)
            print("your in room 22, you can move west")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 21
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 23:
            monster("forest")
            time.sleep(3)
            print("your in room 23, you can move north")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 21
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
else:
    print("Very well, maybe another time")
    quit = True