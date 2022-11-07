
f = [10,100,345,24]

def bob(f):
    print(max(f))

bob(f)


inventory = []

def ar(num):
    for x in num:
        print(x)

for i in range(6):
    p = int(input("Type a number"))
    inventory.append(p)

ar(inventory)