import random

gover = False

class lightbulb():
    def __init__(self):

        self.on = False
        self.red = random.randint(0,255)
        self.green = random.randint(0,255)
        self.blue = random.randint(0,255)
        self.burn = False 
    def turnon(self, n):
        l = random.randint(1,101)
        if l <= 5 and n == 'yes':
            self.burn = True
            self.on = False
            print("the bulb flickers and slowly dies out")
        if n == "yes":
            self.on = True
        elif n == "no":
            self.on = False
    def condition(self):
        print("is the light on?", self.on)
        print("color in rgb is: ", self.red, self.green, self.blue)
        print("Light is burnt: ", self.burn)


bulb1 = lightbulb()
bulb2 = lightbulb()
bulb3 = lightbulb()

while not gover:
    f = input("what bulb do you want to check, bulb (1), (2), or (3)")
    if f == '1':
        bulb1.condition()
        h = input("do you wish to turn on the light? yes/no")
        if h == 'yes':
            bulb1.turnon(h)
    if f == '2':
        bulb2.condition()
        h = input("do you wish to turn on the light? yes/no")
        if h == 'yes':
            bulb2.turnon(h)
    if f == '3':
        bulb3.condition()
        h = input("do you wish to turn on the light? yes/no")
        if h == 'yes':
            bulb3.turnon(h)