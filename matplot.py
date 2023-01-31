import matplotlib.pyplot as plt

y = []

for i in range(20):
    y.append(i*5-20)

l = []

for i in range(20):
    l.append(i*-3+10)

plt.plot(y)
plt.plot(l)
plt.show()