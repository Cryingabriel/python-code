

print("you slowly wake up with water driping down you're face, when you open your eyes your inside a cold, dark and damp room. You have no idea how you woke up in here, all you can recall is falling asleep in bed then waking here.")
room = 1
while True:
    if room == 1:
        print("your in room 1, you can move (e)ast")
        choice = input()
        if choice == 'e' or choice == 'East' or choice == 'east' or choice == 'East':
            room = 2
    if room == 2:
        print("your in room 2, you can move west or south")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 1
        elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 3
    if room == 3:
        print("your in room 3, you can move north or south")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'North' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south' or choice == 'South':
            room = 4
        elif choice == 'e' or choice == 'E' or choice == 'east' or choice == 'East':
            room = 5
    if room == 4:
        print("your in room 4, you can move north")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 3
     if room == 5:
        print("your in room 5, you can move north")
        choice = input()
        if choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 3