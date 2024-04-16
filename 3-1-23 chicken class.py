import random
from re import A
gameo = False
chickens = ['dave', 'sam', 'ah']


class chicken:
    def __init__(self, name):
        self.hunger = 10
        self.eggs = 0
        self.name = name
    def update(self):
        self.hunger += 5
        if self.hunger < 30:
            l = random.randint(1, 2)
            if l == 1:
                print("bok BOK!")
                print("The Chicken has layed an egg")
                self.eggs += 1
                return 1
            if l == 2:
                return 2
    def feed(self,num):
        self.hunger -= num
        print("peck peck")
    def pet(self):
        print("bock bock!")
        print("the chicken seems happy")
    def info(self):
        print("Chicken Name:", self.name)
        print("Hunger:", self.hunger, "%")
        print("Eggs Layed:", self.eggs)

pen = []

for i in range(3):
    f = random.choice(chickens)
    pen.append(chicken(f))
    chickens.remove(f)

dave = chicken('dave')
sam = chicken('sam')
ah = chicken('ah')

while not gameo:
    c = input("What chicken do you want to check up on? (d)ave, (s)am, (a)h?")
    if c == 'd':
        if len(pen) == 'dave':
            h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
            if h == 'f':
                pen[0].feed(15)
            if h == 'p':
                pen[0].pet()
            if h == 'i':
                pen[0].info()
            pen[0].update()
    if c == 's':
        if len(pen) == 'sam':
            h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
            if h == 'f':
                pen[1].feed(15)
            if h == 'p':
                pen[1].pet()
            if h == 'i':
                pen[1].info()
            pen[1].update()
    if c == 'a':
        if len(pen) == 'ah':
            h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
            if h == 'f':
                pen[2].feed(15)
            if h == 'p':
                pen[2].pet()
            if h == 'i':
                pen[2].info()
            pen[2].update()
