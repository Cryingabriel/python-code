import random
myfile = open("score.txt", "a")
myfile.close()



four = random.randint(1,101)
gover = False
score1 = 0

while gover == False:
    too = int(input("what is the random number"))

    if too < four:
        print("number is too low")
        score1 += 1
    elif too > four:
        print("number is too high")
        score1 += 1
    else:
        print("you got it!")
        score1 += 1
        gover = True


myfile = open("score.txt", "r")
print("Current scores in the file:")
print(myfile.read())
lines = myfile.readlines()
myfile.close()

scores = [(int(line.split()[0]), line.split()[1].strip()) for line in lines] #split looks for spaces and puts things into different slots of a list based on that split
#strip gets rid of spaces

User_name = input("What is you're name")

scores.append((score1, User_name))
scores.sort(reverse=True)

while len(scores) > 10:
    scores.pop

myfile = open("score.txt", "a")

for score, name in scores:
    myfile.write(f"{score} {name}\n")
    myfile.close()