import time

name = ["declan", "alfred", "eli", "sebastion", "landan"]

for i in range(10):
    time.sleep(4)
    l = input("choose who you want to learn about?,Declan, Alfred, Eli, Sebastion, Landan.").lower()

    if "declan" in l:
        print("he is too smart for our group.")
    
    if "alfred" in l:
        print("he is pay to lose in ssbu with all the amibos he's buying.")

    if "eli" in l:
        print("he likes BTD6 way too much that he has 20 hours.")

    if "sebastion" in l:
        print("he is a litteral sweat in ssbu, he needs to take a shower for a least 12 hours.")
    if "landan" in l:
        print("he is about the same level of skill as me in ssbu")
    else:
        print("I don't know that person")