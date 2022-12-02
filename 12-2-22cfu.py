import random
inventory = []
f = False
l = random.randrange(0,100)
money = l
def shop():
    global inventory
    global f
    global money
    print('Welcome to the shop, you have', money, 'coins.')
    print('Your items:', inventory)
    print("Shop items: Potions: $5, Food: $3, Keys: $10")
    i = input("Press P for a potion, f for food, k for a key, and q to quit:")
    if i == 'p':
        if money >= 5:
            print("You got a Potion.")
            inventory.append("Potion")
            money = money - 5
        elif money < 5:
            print("You don't have enough.")
    elif i == 'f':
        if money >= 3:
            print("You got food.")
            inventory.append("Food")
            money = money - 3
        elif money < 3:
            print("You don't have enough coins to buy this.")
    elif i == 'k':
        if money >= 10:
            print("You got a key.")
            inventory.append("Key")
            money = money - 10
        elif money < 10:
            print("You don't have enough for this.")
    elif i == 'q':
        print("bye")
        f = True
    
    return money

while f == False:
    shop()