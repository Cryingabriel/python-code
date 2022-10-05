import random
#function definition
def monster(biome):
  num = random.randrange(0, 100)
  if biome == "dungeon":
    if num <= 25:
      battlesystem("Zombie",100)
    elif num <= 45:#30% chance
      battlesystem("Skeleton",100)
    elif num <= 65:
      battlesystem("Spider",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "mansion":
    if num <= 30:
      battlesystem("Scorpion",100)
    elif num <= 50:#30% chance
      battlesystem("Skeleton",100)
    elif num <= 79:
      battlesystem("Spider",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "forest":
    if num <= 25:
      battlesystem("Mushroom",100)
    elif num <= 75:#30% chance
      battlesystem("Fairy",100)
    elif num <= 85:
      battlesystem("Troll",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "outside":
    if num <= 25:
      battlesystem("Skeleton",100)
    elif num <= 75:#30% chance
      battlesystem("Ghost",100)
    elif num <= 85:
      battlesystem("Zombie",100)
    elif num <= 100:
      battlesystem("Slime",100)
#____________________________________________

def battlesystem(monster, playerhealth):
    if monster == "Zombie":
        monsterhealth = 28
        print("a Zombie has spawned in")
    elif monster == "Skeleton":
        monsterhealth = 25
        print("a Skeleton has shot at you")
    elif monster == "Spider":
        monsterhealth = 27
        print("a Spider tried to trap you")
    elif monster == "Goblin":
        monsterhealth = 20
        print("a Goblin is trying to stab you")
    elif monster == "Scorpion":
        monsterhealth = 24
        print("A Scorpion is stinging you")
    elif monster == "Mushroom":
        monsterhealth =16
        print("a mushroom monster tries to poison you")
    elif monster == "Troll":
        monsterhealth =45
        print("a Troll is trying to squash you")
    elif monster == "Fairy":
        monsterhealth =19
        print("Fairies start biting at you")
    elif monster == "Ghost":
        monsterhealth =39
        print("Ghosts are trying take you away")
    elif monster == "Slime":
        monsterhealth =30
        print("slimes are trying to erode you")
        
    while monsterhealth>0 and playerhealth >0:
        if monster == "Zombie":
            monsterattack = random.randrange(9, 14)
        elif monster == "Skeleton":
            monsterattack = random.randrange(8,16)
        elif monster == "Spider":
            monsterattack = random.randrange(7,13)
        elif monster == "Goblin":
            monsterattack = random.randrange(9,17)
        elif monster == "Scorpion":
            monsterattack = random.randrange(7,19)
        elif monster == "Troll":
            monsterattack = random.randrange(16,26)
        elif monster == "Fairy":
            monsterattack = random.randrange(10,15)
        elif monster == "Mushroom":
            monsterattack = random.randrange(13,15)
        elif monster == "Ghost":
            monsterattack = random.randrange(17,18)
        elif monster == "Slime":
            monsterattack = random.randrange(19,24)
            
        print("The", monster, "attacks deal", monsterattack, "damage")
        playerhealth = playerhealth - monsterattack
        print("your HP is at", playerhealth)
        
        playerattack = random.randrange(10,15)
        print("you deal", playerattack, "damage")
        monsterhealth= monsterhealth - playerattack
        print("the monsters HP is at", monsterhealth)
    if monsterhealth<= 0:
        print("you have won")
    else:
        print("you have died")
    return playerhealth

print("you slowly wake up with water driping down you're face, when you open your eyes your inside a cold, dark and damp room. You have no idea how you woke up in here, all you can recall is falling asleep in bed then waking here.")
room = 1
while True:
    if room == 1:
        monster("dungeon")
        print("your in room 1, you can move (e)ast")
        choice = input()
        if choice == 'e' or choice == 'East' or choice == 'east' or choice == 'East':
            room = 2
        else:
            print("that's not an option")
    if room == 2:
        monster("dungeon")
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
        print("your in room 8, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 7
        else:
            print("that's not an option")
    if room == 9:
        monster("mansion")
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
        print("your in room 11, you can move west, south or east")
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
        print("your in room 14, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 13
        else:
            print("that's not an option")
    if room == 15:
        monster("outside")
        print("your in room 15, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 16
        else:
            print("that's not an option")
    if room == 16:
        monster("outside")
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
        print("your in room 17, you can move east")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 16
        else:
            print("that's not an option")
    if room == 18:
        monster("forest")
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
        print("your in room 20, you can move south")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 19
        else:
            print("that's not an option")
    if room == 21:
        monster("forest")
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
        print("your in room 22, you can move west")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 21
        else:
            print("that's not an option")
    if room == 23:
        monster("forest")
        print("your in room 23, you can move north")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 21
        else:
            print("that's not an option")