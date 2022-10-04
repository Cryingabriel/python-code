import time #beings in files prewritten code
import random

def hello():

    slow = False #declaring and intializing variables
    count = 0
    while count < 5 and slow == False:
        nim = random.randint(0,20) #random number between 1-20
        TimeStart = time.perf_counter()#starts the timer
        print("quickly press the number", nim)
        usernumber = int(input())
        TimeEnd = time.perf_counter()
        if TimeEnd-TimeStart < 2 and usernumber == nim:
            count+=1
        else:
            if usernumber != nim:
                print("wrong number")
            else:
                print("very slow")
            slow = True
    if slow == False:
        print("you were so slow that a sloth could beat you")
        return False
    else:
        print("you were pretty fast")
        return True

#__________________________________________________
hello()

