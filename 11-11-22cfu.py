import random
per = ('Butterfingers', "Hershey's", 'Peanutbutter cups', "M&M's", 'Sourpatch', 'Rocks')
candy = [0, 0, 0, 0, 0, 0]
y = int(input("how many houses do you go trick or treating at?"))

def cog():
    global candy
    for i in range(y):
        f = random.randint(1,100)
        g = random.randint(1,4)
        if f <=15:
            candy[0]+= g
            print("You got", g, "Butterfingers")
        elif f <=35:
            candy[1]+= g
            print("You got",g, "Hershey's")
        elif f <= 70:
            candy[2]+= g
            print("You got", g, "Peanutbutter cups")
        elif f <=80:
            candy[3]+= g
            print("You got", g, "M&M's")
        elif f <= 98:
            candy[4]+= g
            print("You got", g, "Sourpatch")
        elif f <= 100:
            candy[5]+= g
            print("You got", g, "Rocks")
    print(candy)

cog()
for i in range(6):
    print(per[i], ":", candy[i])