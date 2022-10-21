choice = input("what color are you thinking about")

if choice == "blue":
  print("The sky is Blue!")
elif choice == "green":
  print("The grass is green!")
else:
  print("I don't know that color")

choice1 = int(input("how old are you?"))

if choice1 < 43:
  print("you are too young to play this game")
elif choice1 > 43:
  print("you are way too old to play this game")
elif choice1 == 43:
  print("you are our target audience so welcome aboard")

for i in range(50,27,3):
  print(i)

quit = False
while quit == False:
  for k in range(10,65,5):
    print(k)
    quit = True

quit1 = False 
while quit1 == False:
  choice2 = input("type a word, type q to stop")
  print(choice2)
  if choice2 == ("q"):
      quit1 = True



def add(x, y):
    return x/y

print(add(4,2))



def snore(hi):
    for i in range(13):
        print("snorfle")
        
snore("hi")