import random
gameo = False
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

dave = chicken('dave')
sam = chicken('sam')
ah = chicken('ah')

while not gameo:
    dave.update()
    sam.update()
    ah.update()
    c = input("What chicken do you want to check up on? (d)ave, (s)am, (a)h?")
    if c == 'd':
        h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
        if h == 'f':
            dave.feed(15)
        if h == 'p':
            dave.pet()
        if h == 'i':
            dave.info()
    if c == 's':
        h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
        if h == 'f':
            sam.feed(15)
        if h == 'p':
            sam.pet()
        if h == 'i':
            sam.info()
    if c == 'a':
        h = input("what do you wish to do with the chicken? (f)eed, (p)et, or get it's (i)nfo")
        if h == 'f':
            ah.feed(15)
        if h == 'p':
            ah.pet()
        if h == 'i':
            ah.info()
