import random
adj = ["Attractive", "Bald","Brave", "Calm", "Fit", "Grumpy", "Faithful", "Kind", "Lazy", "Zealous", "raving"]
noun = ["Adult", "Girl", "Boy", "Baby", "Dad", "Fish", "History", "Coffee", "Buisness", "Animal"]

game = False
while game == False:
    g = input("Want to generate a random stage name, Yes/No")
    n = random.randint(0,10)
    l = random.randint(0,9)
    if g == ('no'):
        game = True
    elif g == ('yes'):
        print("Your stage name is", adj[n], noun[l])