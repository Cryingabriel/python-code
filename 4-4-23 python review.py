
#1 input 4
y = int(input("How much can you bench press?"))

if y <= 10:
    print("Keep practicing and you'll get SWOL.")
elif y > 10 and y <= 50:
    print("eh you're getting good.")
elif y > 50:
    print("Geez you're MEGA SWOL.")


#2 for loop 4

for i in range(20,52,2):
    print(i)


#3 while loop 4
quit = False

while quit == False:
    print("ribbit")
    l = input("Type frog if you want to stop ")
    if l == 'frog':
        quit = True

num = 100

while num != 50:
    num-=5
    print(num)

#4 function 4

def atn(x,y):
    r = (x+y)/2
    print(r)

atn(8,4)

def gc(name):
    print(name, "you look good today.")

quit2 = False

while quit2 == False:
    name = input("What is your name? else type no to stop")
    if name == "stop":
        quit2 = True
    else:
        gc(name)

#5 list 4

marbles = [4,6,2,9]

print(marbles[2])
marbles[0]*=5
marbles[1]*=5
marbles[2]*=5
marbles[3]*=5
print(marbles)

#6 class 3

class fruit:
    def __init__(self, t, w):
        self.type = t
        self.weight = w
        self.isf = True
    
    def printinfo(self):
        print("I am a", self.type, "and I weigh", self.weight)
        if self.isf == True:
            print("I am Fresh")
        else:
            print("I am Rotten")
    def trotten(self):
        self.isf = False

f1 = fruit("apple", 2)
f2 = fruit("orange", 4)

f1.printinfo()
f2.printinfo()
f1.trotten()
f2.trotten()
f1.printinfo()
f2.printinfo()