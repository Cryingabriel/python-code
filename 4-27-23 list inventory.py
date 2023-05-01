quit = False
room = 1
door = False
inventory = []



#Game loop-------------------------------

while quit == False:
    if room == 1:
        print("You're in room 1, You can move South.")
        choice = input(": ")
        if choice == 'south' or choice == "South":
            room = 2
        elif choice == 'pickup' or choice == 'Pickup':
            if 'Map' in inventory:
                print("You have already picked up the Medkit.")
            else:
                inventory.append("Map")
                print("You have picked up a Map.")
        elif choice == 'inventory' or choice == 'Inventory':
            print(inventory)
        else:
            print("That is not an option.")
    if room == 2:
        if 'Key' in inventory:
            print("You're in room 2, you can move South or North.")
        else:
            print("You're in room 2, out of the corner of your eye you see a key shining on a desk you can move South or North.")
        choice = input(": ")
        if choice == 'south' or choice == 'South':
            room = 3
        elif choice == 'east' or choice == 'East':
            room = 1
        elif choice == 'pickup' or choice == 'Pickup':
            if 'Key' in inventory:
                print("You have already picked up the key.")
            else:
                inventory.append("Key")
                print("You have picked up a Key.")
        elif choice == 'inventory' or choice == 'Inventory':
            print(inventory)
        else:
            print("That is not an option.")
    if room == 3:
        print("You're in room 3, you see a weird rug in the middle of the room, you can move South or North.")
        choice = input(": ")
        if choice == 'south' or choice == "South":
            if door == True:
                room = 4
            else:
                print("You need a Key to open this.")
        elif choice == 'north' or choice == 'North':
            room = 3
        elif choice == 'use' or choice == 'Use':
            door = True
            print("when you open the door the key in your hand disappears before your eyes.")
            inventory.remove('Key')
        elif choice == 'find' or choice == 'Find':
            if 'Sword' in inventory:
                print("You already have the sword")
            else:
                inventory.append('Sword')
                print("You have picked up a Sword")
        elif choice == 'inventory' or choice == 'Inventory':
            print(inventory)
        else:
            print("That is not an option.")
    if room == 4:
        print("You're in room 4, You can move East or North.")
        choice = input(": ")
        if choice == 'east' or choice == 'East':
            room = 5
        elif choice == 'north' or choice == 'North':
            room = 3
        elif choice == 'pickup' or choice == 'Pickup':
            if 'Shield' in inventory:
                print("You have already picked up the Shield.")
            else:
                inventory.append("Shield")
                print("You have picked up a Shield.")
        elif choice == 'inventory' or choice == 'Inventory':
            print(inventory)
        else:
            print("That is not an option.")
    if room == 5:
        if 'Sword'and 'Shield' in inventory:
            print("You defeat the dragon after a epic duel.")
            print("You're in room 5, you find a medkit on a table near the door. you can move West.")
        else:
            print("You get eaten by a dragon.")
            quit = True
        choice = input(": ")
        if choice == 'west' or choice == 'West':
            room = 4
        elif choice == 'pickup' or choice == 'Pickup':
            if 'Medkit' in inventory:
                print("You have already picked up the Medkit.")
            else:
                inventory.append("Medkit")
                print("You have picked up a Medkit.")
        elif choice == 'inventory' or choice == 'Inventory':
            print(inventory)
        else:
            print("That is not an option")
