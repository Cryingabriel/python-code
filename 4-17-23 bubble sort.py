import random

l = []

x = 11

for i in range(12):
    l.append(random.randint(1,11))

print(l)
for i in range(12):
    for j in range(x):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]


print(l)