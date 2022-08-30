import time#you need to import this so time.sleep() function works

name = input("What is your name")

print("???: Welcome "+ name)
time.sleep(3)#makes the text wait a few to appear
print("???: You have been chosen because no one else was left.")
time.sleep(3)
print("???: Now then please, come with me "+name)

f = input("do you wish to follow this person?, yes/no").lower#.lower makes the users input lowercase

#_______________________________________________



if "yes" in f:
    time.sleep(3)
    print("You follow the mysterious man with many questions running through your head.")
    time.sleep(3)
    print("While you walk you pass by many people. They look at you with an anxious look on their faces.")
    time.sleep(5)
    print("You: why are they looking at me like that?")
    time.sleep(3)
    print("Mysterious man: a lot is riding on your decisions. They are worried that you don't have what it takes.")
    time.sleep(3)
    print("You stop infront of two huge doors.")
    time.sleep(3)
    print("Mysterious man: this is your last chance to walk away.")
    time.sleep(3)
    l = input("Do you wish to contiue to follow? yes/no").lower()
    time.sleep(3)
    if "yes" in l:
        print("You: too into it now.")
        time.sleep(3)
        print("You walk through the huge doors with the man. A new adventure starts here.")
    elif "no" in l:
        print("Your vision starts to go dark and you lose conscience.")
elif "no" in f:
    print("You run away flailing your arms at the situation.")
    time.sleep(3)
    print("The man behind you facepalms and murmurs, 'why did we choose this guy.")
    time.sleep(3)
    print("Your vision goes dark and you lose conscience.")