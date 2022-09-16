import math
import time 

quit = False

while quit == False:
    r = int(input("type number 1 to continue, type 2 to quit"))
    if r == 1:
        f = float(input("please type 1 number"))
        time.sleep(2)
        g = float(input("please type another number"))
        time.sleep(2)
        d = float(input("give 'nother num"))
        time.sleep(2)
        print(f+g+d/3)
        time.sleep(2)
        n = float(input("please type 1 number"))
        q = float(input("please input a number"))
        print(math.sqrt(n))
        print(math.sqrt(q))
        a = int(input("please type 1 number"))
        b = int(input("please type number"))
        print(a**b)
    elif r == 2:
        print("turning off...")
        quit = True
    