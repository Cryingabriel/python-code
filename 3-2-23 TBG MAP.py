import random

def direction(x, y):
    t = random.randrange(0, 4)
    print(t)
    if t == 0 and y != 10:
        y += 1
        return x, y
    elif t == 1 and y != 0:
        y -= 1
        return x, y
    elif t == 2 and x != 10:
        x += 1
        return x, y
    elif t == 3 and x != 0:
        x -= 1
        return x, y

game = [[0 for i in range (10)] for j in range (10)]
r = random.randint(0, 10)
g = random.randint(0, 10)
game[r][g] = 1
ticker = 1

while ticker != 10:
    r, g = direction(r, g)
    print(r, g)
    if game[r][g] == 0:
        game[r][g] = random.randrange(2, 5)
        ticker += 1

for i in range(10):
    for j in range(10):
        if game[i][j] == 0:
            print("[ ]", end = "")
        else:
            print("[", end = "")
            print(game[i][j], end = "")
            print("]", end = "")
    print()
