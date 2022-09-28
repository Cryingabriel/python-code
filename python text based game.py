import random
#function definition
def monster(biome):
  num = random.randrange(0, 100)
  if biome == "dungeon":
    if num <= 25:
      print("a zombie attacks you")
    elif num <= 45:#30% chance
      print("a skeleton fires at you")
    elif num <= 65:
      print("a spider is trying to trap you")
    elif num <= 100:
      print("you get stabbed by a goblin")
  elif biome == "mansion":
    if num <= 30:
      print("a scorpion attacks you")
    elif num <= 50:#30% chance
      print("a skeleton fires at you")
    elif num <= 79:
      print("a spider is trying to trap you")
    elif num <= 100:
      print("you get stabbed by a goblin")
  elif biome == "forest":
    if num <= 25:
      print("a mushroom monsters attacks you")
    elif num <= 75:#30% chance
      print("Fairies start biting at you")
    elif num <= 85:
      print("a Troll is trying to squash you")
    elif num <= 100:
      print("you get stabbed by a goblin")

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
        print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 7
        else:
            print("that's not an option")
    if room == 9:
        monster("mansion")
        print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west")
        choice = input()
        if choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 10
        elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 6
        else:
            print("that's not an option")
    if room == 10:
        monster("mansion")
        print("you climb up the ladder to find yourself in a some sort of storage with all sorts of tools inside it, you can move west")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 9
        else:
            print("that's not an option")