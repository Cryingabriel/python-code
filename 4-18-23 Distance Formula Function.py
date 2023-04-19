import math

def Distance(x,y,i,o,r):
    t = (math.sqrt((x-i)**2+(y-o)**2))

    if t < r:
        print("It's in the circle")
    else:
        print("It's not in the circle")

x = int(input("What is the first x value? "))
i = int(input("What is the second x vlaue? "))
y = int(input("What is the first y value? "))
o = int(input("What is the second y value?"))
r = int(input("What is the radius of the circle? "))

Distance(x,i,y,o,r)
