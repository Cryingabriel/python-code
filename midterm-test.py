f = int(input("How many cookies do you have?"))
if f < 3:
    print("You don't have enough Cookies.")
elif f >= 3 and f <=10:
    print("You have an alright amount of Cookies.")
elif f > 10:
    print("You have too many Cookies and should share them.")

l = input("Are you a Jedi or a Sith?")
if l == 'jedi' or l == 'Jedi':
    print("Then you are eligible for a Green Lightsaber!.")
elif l == 'sith' or l == 'Sith':
    print("Then you shall rule the galaxy wit ha red saber in hand!")
else:
    print("you are worthy of the ultimate...BREADSTICK!")
    
for i in range(4,44,2):
    print(i)
num =100
while num != 40:
    print(num)
    num-=10
quit2 = False
while quit2 == False:
    print("Knock knock, who's there? ... BANANA!")
    i = input("if you wish for this torment to stop type Orange.")
    if i == 'Orange' or i == 'orange':
        print("Orange you glad I didn't say Banana")
        quit2 = True

def add(x,y,z):
    return x+y+z

print(add(23,5,7))

def bob(x):
    for i in range(x):
        print(x, "Bottles of Root Beers on the wall!...", x, "Bottles of Root Beer!, Take one down, pass it around,", x-1, "Bottle of Root Beer on the wall!")
        x-=1
p = int(input("type a number"))
bob(p)