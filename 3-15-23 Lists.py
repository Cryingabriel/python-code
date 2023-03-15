import random

mah = []

for i in range(12):
    y = random.randrange(1,13)
    mah.append(y)


mah.sort()
print(mah)
print("The biggest number is:", max(mah))
print("The smallest number is :", min(mah))
print(mah)
for i in range(10):
    if mah[i]+1 == mah[i+1]:
        if mah[i+1]+1 == mah[+2]:
            print("The list contains", mah[i], mah[i+1], mah[i+2], " so True")
    else:
        print("False")
mah.reverse()
print(mah)