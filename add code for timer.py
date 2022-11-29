import time 

start = time.time()
room = 1
Timeleft = 2000

while Timeleft > 0:
    print()
    newtime = time.time()
    timee = start - newtime
    print(int(timee*-1), "seconds passed.")
    Timeleft += timee
    print("you have", int(Timeleft), "seconds left to complete thhe game!")