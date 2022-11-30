#Add gold into the game so that the player has to pay gold to enter the next area[Done.]
#Maybe make it so when the player dies they go back to the beginning without anything that they got[Done.]
#Add it so the players can quit the game when they want[Done.]
#Add doors for the gold to be used on[Done.]
#Make it so that players can see the amount of gold and health when they type g or h[Semi done, finish for all rooms. Too much work to fix this problem so just leave for now.]
#Make it so that all input is lowercase so it's easier on me[It doesn't work so some reason, ask eli for help.]
#Add an inventory so that player can hold things when added later[Done.]
#Add a sword that spawns in a room that boosts attack[Done.]
#See if I can add healthpotions/aidkits in some later rooms to make beating the game easier[Might add or not. Depends on how hard I want to make the game.]
#Tweek potions so that it's easier to die to monsters[Not done.]
#Add final boss for the game[Done.]
#Add a way to increase Max health for player[Done.]
#Add Doors or chests that can only be opened when other things are opened[Done.]
#Make it so players can see their inventory[Done.]
#Make it so that players have a certain chance to crit on attack[Done.]

import random
import time
import math
import os
#function definition
end = input("Do you wish to turn your text to light mode? yes/no")
if end == 'yes' or end =='y':
    os.system('color f0')#This makes it so the terminal for the game changes colors.
elif end == 'No' or end == 'no':
    end = input("Press any key to continue")
    os.system('color 55')

playerhealth=100
mplayerhealth = 100
gold=0
inventory = []
def help():
    print("press g to view the amount of gold that you have. type 'hp' in order to view your health. press p in order to pick up items. press q to quit the game.(your gameplay will not be saved). type pay in order to open doors and chests. ")
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
    elif biome == "BossRoom":
        battlesystem("Dragon")

#____________________________________________

def battlesystem(monster):#This makes it so that you can fight monsters and degeat them to get gold.
    global inventory
    potion = random.randrange(35,40)#These are the range of which these potions can heal you.
    highpotion = random.randrange(40,45)
    fullpotion = random.randrange(100,110)
    global playerhealth
    global gold
    monsterhealth = 0
    global quit
    global mplayerhealth
    global room
    global opendoor
    global opendoor1
    global opendoor2
    global opendoor3
    if monster == "Zombie":#This here controls the amount of health each monster has.
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
        monsterhealth = 48
        print("a mushroom monster tries to poison you")
        time.sleep(4)
    elif monster == "Troll":
        monsterhealth = 60
        print("a Troll is trying to squash you")
        time.sleep(4)
    elif monster == "Fairy":
        monsterhealth = 39
        print("Fairies start biting at you")
        time.sleep(4)
    elif monster == "Ghost":
        monsterhealth = 39
        print("Ghosts are trying take you away")
        time.sleep(4)
    elif monster == "Slime":
        monsterhealth = 40
        print("slimes are trying to erode you")
        time.sleep(4)
    elif monster == "Dragon":
        monsterhealth = 80
        print("the master of this place won't let you leave that easily")
        time.sleep(4)
        
    while monsterhealth > 0 and playerhealth > 0:
        monsterattack = 0
        nu = random.randrange(0,100)
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
        elif monster == "Dragon":
            if nu <= 99:
                monsterattack = random.randrange(15,37)
            elif nu <= 100:
                monsterattack = random.randrange(99,100)
            
        print("The", monster, "attacks deal", monsterattack, "damage.")
        playerhealth = playerhealth - monsterattack
        time.sleep(3)
        print("your HP is at", playerhealth)
        
        playerattack = random.randrange(10,20) #I had to add 3 damage cause of Eli then I won later and subtracted 3 again then I won again
        n = random.randrange(0,100)
        
        if n >= 90 and n <= 100: #this makes it so that there's a 10% chance to crit a monster
            playerattack = playerattack*2
        
        for i in range(len(inventory)): # this goes though all of the inventory makes sure that you have these items 
            if inventory[i] == 'esword':
                playerattack +=10
                print("the sword adds 10 damage to your attack")
                time.sleep(2)
            elif inventory[i] == 'sword':
                playerattack +=7
                print("the sword you wield adds 7 damage to your attack")
                time.sleep(2)
        
        time.sleep(2)
        print("you deal", playerattack, "damage.")
        time.sleep(2)
        monsterhealth= monsterhealth - playerattack
        time.sleep(2)
        print("the monsters HP is at", monsterhealth)
        time.sleep(2)
    if playerhealth <= 0:# this makes sure that when the player dies the game end
        print("you succumbed to your wounds as your vision slowly fades to black")
        room = 1
        playerhealth = 100
        gold = 0
        opendoor = False
        opendoor1 = False
        opendoor2 = False
        opendoor3 = False
        inventory = []
        time.sleep(3)
        print("you slowly regain consciousness propt up against a familiar looking room")
        time.sleep(3)
    elif monsterhealth <= 0: #makes sure that when you defeat the monster the monster drops gold for doors
        print("you have won.")
        time.sleep(3)
        print("the", monster, "drops a red liqud. when you pick it up some of your wounds disapear.")
        time.sleep(4)
        num2 = random.randrange(0,100)
        monsterdrop = random.randrange(30,65)#this randomly drops a certain amount of gold between those numbers
        if num2 <= 85:
            print("the potion gives you", potion, "health.")
            playerhealth = playerhealth + potion#this makes it so that the potion actually adds health
            print("the", monster, "also drops", monsterdrop, "gold that could be used later.")
            gold = gold + monsterdrop
            print("you now have", gold, "gold")
        elif num2 <= 95:
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
        for i in range(len(inventory)):#This makes it so that if you have the token in your inventory then it makes your MaxHp 150 instead of 100
            if inventory[i] == 'MaxHp':
                mplayerhealth = 150
                playerhealth = playerhealth + 1
                if playerhealth > 150:
                    playerhealth = 150
        if playerhealth > mplayerhealth:
            playerhealth = mplayerhealth
    
    time.sleep(2)
    print("your HP has been restored to", playerhealth, "/", mplayerhealth)

    return playerhealth
#__________game below_______________________________________________________________ 
quit = False
opendoor = True
opendoor1 = True
opendoor2 = True
opendoor3 = True
opendoor4 = True
choice1 = input("do you want to play a game? Yes/No")
if choice1 == 'y' or choice1 == 'Y' or choice1 == 'yes' or choice1 == 'Yes' or choice1 == 'YES':
    time.sleep(3)
    print("you slowly wake up with water driping down you're face, when you open your eyes your inside a cold, dark and damp room. You have no idea how you woke up in here, all you can recall is falling asleep in bed then waking here.through the darkness you can see a vague silhouette coming towards you.")
    room = 16
    time.sleep(8)
    while quit == False:
        
        if room == 1:
            #monster("dungeon")#this is calling my monster and battle function to run
            time.sleep(3)
            print("Your in a dull looking cell, it appears run down as parts of the iron bars look to be destroyed enough to squeez through. Out of the corner of your eye something is shining, you can move (e)ast.")
            print("psst, if you need help press h for info if you need help.")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':  
                room = 2
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("Press any key to continue your journey.")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("Press any key to continue your journey.")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()#this is calling my help/info function to run
                i = input("Press any key to continue.")
            elif choice == 'pickup' or 'p':
                print("you have obtained a Rusted Key.")
                inventory.append("Rusted Key")#this adds an item into the inventory
            else:
                print("that's not an option.")
        if room == 2:
            #monster("dungeon")
            time.sleep(3)
            print("When you walk into the room you find a brick hallway that drips with some sort of fluid with a foul smell that makes you recoil with disgust. You can move (w)est or (s)outh.")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 1
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 3
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")#gives a break to the player so they have time to think.
            elif choice == 'i' or choice == 'I':
                print(inventory)#this prints out the entire inventory.
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option.")
        if room == 3:
            #monster("dungeon")
            time.sleep(3)
            n = random.randrange(100,300)
            if opendoor == False:
                print("Your in room 3, you can move North, South or pay to open door to the East.")
            if opendoor == True:
                print("Your in room 3, you can move North, South or East.")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'North' or choice == 'north' or choice == 'NORTH':
                room = 2
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 4
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST' and opendoor == True:
                room = 5
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'pay'and gold >= 200:
                gold -= 200
                opendoor = True
                time.sleep(3)
                print("Taking you're gold the door magically dissapears before your eyes.")
                time.sleep(2)
                print("You now have", gold, "gold")
            elif choice == 'pay' and gold != 200:
                print("You try to pay but realise too late that you don't have enough money and lost 100 gold.")
                gold -= n
                time.sleep(3)
                print("you now have", gold, "gold")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option.")
        if room == 4:
            #monster("dungeon")
            time.sleep(3)
            if opendoor2 == False:
                print("your in room 4, when you look around the room you find that it, like the previous rooms was mostly empty. but out of the corner of your eye you find that there was a small door leading to somewhere unknown. when you try to open it it doesn't budge and nothing you do seems to open it.")
            if opendoor2 == True:
                print("your in room 4 you can move (n)orth or (w)est")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North'  or choice == 'NORTH':
                room = 3
            elif choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West'  or choice == 'WEST':
                room = 24
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
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
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 6:
            #monster("mansion")
            time.sleep(3)
            print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west, south or go back down")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 7
            elif choice == 'd' or choice == 'D' or choice == 'down' or choice == 'Down' or choice == 'DOWN':
                room = 5
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 9
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 7:
            #monster("mansion")
            time.sleep(3)
            print("your in room 7, you can move north or east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 8
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 6
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 8:
            #monster("mansion")
            time.sleep(3)
            print("your in room 8 in the corrider you have found an old chest that seems to need a key, you can move south")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 7
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'open' or choice == 'Open':
                key = False
                for i in range(len(inventory)):
                    if inventory[i] == "Key":
                        key = True
                if key == True:
                    print("you have obtained a Key")
                    inventory.append("Key1")
                else:
                    print("you try everything to open the chest however the chest doesn't budge and afetr a while you give up")
            else:
                print("that's not an option")
        if room == 9:
            #monster("mansion")
            time.sleep(3)
            print("your in room 9, you can move north or east")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 10
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 6
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 10:
            #monster("mansion")
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
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'pay'and gold >= 700:
                gold -= 700
                opendoor1 = True
                time.sleep(3)
                print("taking you're gold the door magically dissapears before your eyes")
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
            #monster("outside")
            time.sleep(3)
            n = random.randrange(300,450)
            if opendoor3 == False:
                print("when you look around you find yourself surrounded by greenery of a abandoned garden.It's filled with overgrown vines and weeds all over with countless spiderwebs everywhere, you can move north, west, south or pay to open a door going east")
            if opendoor3 == True:
                print("your in room 11 you can move north, west, south or east")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 12
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST' and opendoor3 == True:
                room = 18
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH' and opendoor3 == True:
                room = 10
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'pay'and gold >= 1000:
                gold -= 1000
                opendoor3 = True
                time.sleep(3)
                print("taking you're gold the door magically dissapears before your eyes")
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
            #monster("outside")
            time.sleep(3)
            print("your in room 12, you can move west or east, you find a bloody sword stuck in the dirt")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 13
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 11
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'sword' or 'Sword':
                print("you got a sword")
                inventory.append('sword')
            else:
                print("that's not an option")
        if room == 13:
            #monster("outside")
            time.sleep(3)
            print("your in room 13, you can move north or east")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 14
            elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 12
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 14:
            #monster("outside")
            time.sleep(3)
            print("your in room 14, you can move south")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 13
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 15:
            #monster("outside")
            time.sleep(3)
            print("your in room 15, you can move south or north")
            choice = input()
            if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 16
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 11
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 16:
            #monster("outside")
            time.sleep(3)
            if opendoor4 == False:
                print("your in room 16, you can move North or have a key to open the door ")
            if opendoor4 == True:
                print("your in room 16, you can move north or west")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 17
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 15
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'open' or choice == 'Open':
                Key0 = False
                for i in range(len(inventory)):
                    if inventory[i] == "Rusted Key":
                        Key0 = True
                if Key0 == True:
                    print("taking you're key the door magically disapears before your eyes.")
                    opendoor4 = True
                else:
                    print("you try everything to open the door however the door doesn't budge and after a while you give up.")
            else:
                print("that's not an option")
        if room == 17:
            monster("outside")
            time.sleep(3)
            print("your in room 17 and find a glowing sword that gives off a sacred feeling besides it you find a weird token, you can move east")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 16
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH':
                room = 23
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'pickup' or choice == 'p':
                print("when you pick up the sword it starts to glow even brighter like it wants to be wielded by you.")
                time.sleep(3)
                print("when you pick up the token you for some reason feel like you become healthier")
                inventory.append("esword")
                inventory.append("MaxHp")
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
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
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
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
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
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 21:
            monster("forest")
            time.sleep(3)
            if opendoor2 == False:
                print("your in room 21, you can move west or pay to open the door leading east")
            if opendoor2 == True:
                print("your in room 21 you can move north or east")
            print("your in room 21, you can move north, east or open a door to the south")
            choice = input()
            if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East' or choice == 'EAST':
                room = 22
            elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 19
            elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South' or choice == 'SOUTH' and opendoor2 == True:
                room = 23
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'open' or choice == 'Open':
                Key1 = False
                for i in range(len(inventory)):
                    if inventory[i] == "Key1":
                        Key1 = True
                if Key1 == True:
                    print("taking you're key the door magically dissapears before your eyes.")
                    opendoor2 = True
                else:
                    print("you try everything to open the chest however the chest doesn't budge and afetr a while you give up.")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            else:
                print("that's not an option")
        if room == 22:
            monster("BossRoom")
            time.sleep(3)
            print("your in room 22, you can move west")
            choice = input()
            if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West' or choice == 'WEST':
                room = 21
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            else:
                print("that's not an option")
        if room == 23:
            monster("forest")
            time.sleep(3)
            print("your in room 23 and find a worn down chest that could be opened, you can move north")
            choice = input()
            if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 21
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'open' or choice == 'Open':
                print("when you open the chest you notice a shiny object and when you pick it up you find that it's a key.")
                inventory.append("Key")
            else:
                print("that's not an option")
        if room == 24:
            time.sleep(3)
            print("when you enter the small door you find that you have to crawl through in order to fit. after a few minutes of crawling you make your way into an emtpy room. looking around the only thing you find is a message written in stone next to a skeleton.")
            choice = input()
            if choice == 'e' or choice == 'N' or choice == 'north' or choice == 'North' or choice == 'NORTH':
                room = 21
            elif choice == 'g' or choice == 'G' or choice == 'gold' or choice == 'Gold' or choice == 'GOLD':
                print("You have", gold, "gold.")
                i = input("press any key to continue your journey")
            elif choice == 'hp' or choice == 'HP' or choice == 'health' or choice == 'Health' or choice == 'HEALTH':
                print("you have", playerhealth, "health.")
                i = input("press any key to continue your journey")
            elif choice == 'i' or choice == 'I':
                print(inventory)
                i = input("Press any key to continue your journey.")
            elif choice == 'h' or choice == 'help':
                help()
                i = input("Press any key to continue.")
            elif choice == 'q' or choice == 'Q' or choice == 'quit' or choice == 'Quit' or choice == 'QUIT':
                quit = True
            elif choice == 'ex' or choice == 'Ex' or choice == 'examine' or choice == 'Examine' or choice == 'EXAMINE':
                print("When you go examine the message on the stone wall it says. 'god this took forever to code and I wish I made it easier for myself and did just 10 rooms instead of 24, it took forever to code and when I was content I suddenly had more Ideas that I wanted to implement which took forever when those things caused bugs AHHHHHH. The skeleton here represents me after all of this is done.'")
                i = input("press any key to continue")
                print("When you finish reading the message you hear a clicking noise, turning around you find 5 monsters coming at you")
                monster("dungeon")
                monster("dungeon")
                monster("dungeon")
                monster("dungeon")
                monster("dungeon")
else:
    print("Very well, maybe another time.")
    quit = True