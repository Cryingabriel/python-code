import random
import time
#function definition
playerhealth=100
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
    if monster == "Zombie":
        monsterhealth = 38
        print("a Zombie has spawned in")
        time.sleep(4)
    elif monster == "Skeleton":
        monsterhealth = 35
        print("a Skeleton has shot at you")
        time.sleep(4)
    elif monster == "Spider":
        monsterhealth = 37
        print("a Spider tried to trap you")
        time.sleep(4)
    elif monster == "Goblin":
        monsterhealth = 30
        print("a Goblin is trying to stab you")
        time.sleep(4)
    elif monster == "Scorpion":
        monsterhealth = 34
        print("A Scorpion is stinging you")
        time.sleep(4)
    elif monster == "Mushroom":
        monsterhealth =28
        print("a mushroom monster tries to poison you")
        time.sleep(4)
    elif monster == "Troll":
        monsterhealth =45
        print("a Troll is trying to squash you")
        time.sleep(4)
    elif monster == "Fairy":
        monsterhealth =29
        print("Fairies start biting at you")
        time.sleep(4)
    elif monster == "Ghost":
        monsterhealth =39
        print("Ghosts are trying take you away")
        time.sleep(4)
    elif monster == "Slime":
        monsterhealth =30
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
        
        playerattack = random.randrange(13,17)
        time.sleep(4)
        print("you deal", playerattack, "damage.")
        time.sleep(3)
        monsterhealth= monsterhealth - playerattack
        time.sleep(3)
        print("the monsters HP is at", monsterhealth)
        time.sleep(3)
    if monsterhealth<= 0:
        print("you have won.")
        time.sleep(3)
        print("the", monster, "drops a red liqud. when you pick it up some of your wounds disapear.")
        time.sleep(4)
        num2 = random.randrange(0,100)
        if num2 <=70:
            print("the potion gives you", potion, "health.")
            playerhealth = playerhealth + potion
        elif num2 <=95:
            print("the potion gives you", highpotion, "health.")
            playerhealth = playerhealth + highpotion
        elif num2 <= 100:
            print("the potion gives you", fullpotion, "health.")
            playerhealth = playerhealth + fullpotion
        if playerhealth > 100:
            playerhealth = 100
        time.sleep(2)
        print("your HP is at", playerhealth)
    else:
        print("you have been slain.")
    return playerhealth

print("you slowly wake up with water driping down you're face, when you open your eyes your inside a cold, dark and damp room. You have no idea how you woke up in here, all you can recall is falling asleep in bed then waking here.through the darkness you can see a vague silhouette coming towards you.")
room = 1
time.sleep(8)
while True:
    if room == 1:
        monster("dungeon")
        time.sleep(3)
        print("your in a dull looking cell, it appears run down as parts of the iron bars look to be destroyed enough to squeez through, you can move (e)ast")
        choice = input()
        if choice == 'e' or choice == 'East' or choice == 'east' or choice == 'East':
            room = 2
        else:
            print("that's not an option")
    if room == 2:
        monster("dungeon")
        time.sleep(3)
        print("your in room 2, you can move west or south")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 1
        elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 3
        else:
            print("that's not an option")
    if room == 3:
        monster("dungeon")
        time.sleep(3)
        print("your in room 3, you can move north, south or east")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 4
        elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 5
        else:
            print("that's not an option")
    if room == 4:
        monster("dungeon")
        time.sleep(3)
        print("your in room 4, you can move north")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 3
        else:
            print("that's not an option")
    if room == 5:
        print("you enter the room, you find that it's a plain room with nothing in it exept a ladder which seems to lead up.")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 3
        elif choice == 'up' or choice == 'Up':
            room = 6
        else:
            print("that's not an option")
    if room == 6:
        monster("mansion")
        time.sleep(3)
        print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 7
        elif choice == 'd' or choice == 'D' or choice == 'down' or choice == 'Down':
            room = 5
        elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room == 9
        else:
            print("that's not an option")
    if room == 7:
        monster("mansion")
        time.sleep(3)
        print("your in room 7, you can move north or east")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 8
        elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 6
        else:
            print("that's not an option")
    if room == 8:
        monster("mansion")
        time.sleep(3)
        print("your in room 8, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 7
        else:
            print("that's not an option")
    if room == 9:
        monster("mansion")
        time.sleep(3)
        print("your in room 9, you can move east or north")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 10
        elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 6
        else:
            print("that's not an option")
    if room == 10:
        monster("mansion")
        time.sleep(3)
        print("your in room 10, you can move west or east")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 9
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 11
        else:
            print("that's not an option")
    if room == 11:
        monster("outside")
        time.sleep(3)
        print("when you look around you find yourself surrounded by greenery of a abandoned garden.It's filled with overgrown vines and weeds all over with countless spiderwebs everywhere, you can move west, south or east")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 12
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 18
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 15
        else:
            print("that's not an option")
    if room == 12:
        monster("outside")
        time.sleep(3)
        print("your in room 12, you can move west or east")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 13
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 11
        else:
            print("that's not an option")
    if room == 13:
        monster("outside")
        time.sleep(3)
        print("your in room 13, you can move north or east")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 14
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 12
        else:
            print("that's not an option")
    if room == 14:
        monster("outside")
        time.sleep(3)
        print("your in room 14, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 13
        else:
            print("that's not an option")
    if room == 15:
        monster("outside")
        time.sleep(3)
        print("your in room 15, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 16
        else:
            print("that's not an option")
    if room == 16:
        monster("outside")
        time.sleep(3)
        print("your in room 16, you can move north or west")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 17
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 15
        else:
            print("that's not an option")
    if room == 17:
        monster("outside")
        time.sleep(3)
        print("your in room 17, you can move east")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 16
        else:
            print("that's not an option")
    if room == 18:
        monster("forest")
        time.sleep(3)
        print("your in room 18, you can move west or east")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 11
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 19
        else:
            print("that's not an option")
    if room == 19:
        monster("forest")
        time.sleep(3)
        print("your in room 19, you can move west, south or north")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 18
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 20
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 21
        else:
            print("that's not an option")
    if room == 20:
        monster("forest")
        time.sleep(3)
        print("your in room 20, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 19
        else:
            print("that's not an option")
    if room == 21:
        monster("forest")
        time.sleep(3)
        print("your in room 21, you can move north, east or south")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 22
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 19
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 23
        else:
            print("that's not an option")
    if room == 22:
        monster("forest")
        time.sleep(3)
        print("your in room 22, you can move west")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 21
        else:
            print("that's not an option")
    if room == 23:
        monster("forest")
        time.sleep(3)
        print("your in room 23, you can move north")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 21
        else:
            print("that's not an option")