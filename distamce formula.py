import math
l = float(input("type the first x value"))
m = float(input("type the second x value"))
n = float(input("type the first y value"))
o = float(input("type the second y value"))
p = float(input("what is the radius of the circle"))
t = (math.sqrt((l-m)**2+(n-o)**2))

if t < p:
    print("it's in the circle")
else:
    print("it's not in the circle")

print(t)