import random

items = []

game = True

def itemdrop():
    l = random.randint(0,100)
    if l < 25:
        print("You got a Potion!")
        items.append("Potion")
    elif l < 50:
        print("You got a Sock!")
        items.append("Sock")
    elif l < 60:
        print("You got a Coin!")
        items.append("Coin")
    else:
        print("You got Nothing!")



while game != False:
    f = input("Press enter to continue.")
    itemdrop()