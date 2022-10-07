import random
import time
def a(Npc):
  n = random.randrange(0,100)
  if Npc == "n":
    if n <= 20:
      print("Hey, I like shorts!")
    elif n <=30:
      print("DO A BARREL ROLL!")
    elif n <=45:
      print("Science isn't about why, it's about why not!")
    elif n <=80:
      print("What is a man? A miserable little pile of secrets.")
    elif n <=100:
      print("I used to be an adventurer like you. Then I took an arrow in the knee")
    

for i in range(5):
  time.sleep(3)
  a("n")