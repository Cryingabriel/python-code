a = int(input("type a number "))
b = int(input("type a second number "))
c = int(input("type a third number "))





def Biggest(a,b,c):
    
    if a > b and c:
        print(a)
    elif b > a and c:
        print(b)
    elif c > a and b:
        print(c)

Biggest(a,b,c)


l = []
f = []
for i in range(10):
    p = int(input("type a number ")) 
    l.append(p*2)


f.append(l)

print(f)
