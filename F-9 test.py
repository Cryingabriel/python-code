for i in range(3, 38, 5):
    print(i)
    
for k in range(100,48,-2):
    print(k)

quit = False

while quit == False:
    num = int(input("type number"))
    print(num*2)
    hi = input("you're stuck here. If you want out then press 0")
    if hi == ("0"):
        quit = True