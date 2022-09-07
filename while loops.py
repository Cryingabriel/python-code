quit = False
while quit == False:
    num = int(input("please type a number"))
    if num == 3:
         print("You suck child")
         quit = True
    else:
        print("good job!")
        
print("Goodbye")
quit2 = False
while quit2 == False:
    quitinput = input("Type in what you want, type quit to stop")
    if quitinput == ("Quit"):
        quit2 = True
    