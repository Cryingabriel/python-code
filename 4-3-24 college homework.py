f = True


def scooter(r,t):
    if r.lower() == "k" or r.lower() == "kilometer":
        print("Distance in Miles",t * .60934)
        e = t/24.1402
        e = e* 60
        print("Total time in minutes:", e)
        a = 1 + (.15 * (e))
        b = (.12 * (e-5)) + 2.50
        c = 5 + (.06 * (e))
        if a < b and a < c:
            print("You should use company A. It will cost $", a)
        elif b < a and b < c:
            print("You should use company A. It will cost $", b)
        elif c < a and c < b:
            print("You should use company A. It will cost $", c)
    elif r.lower() == "m" or r.lower() == "miles":
        print("Distance in Kilometers",t * 1.60934)
        e = t/15
        e = e* 60
        print("Total time in minutes:", e)
        a = 1 + (.15 * (e))
        b = (.12 * (e-5)) + 2.50
        c = 5 + (.06 * (e))
        if a < b and a < c:
            print("You should use company A. It will cost $", a)
        elif b < a and b < c:
            print("You should use company A. It will cost $", b)
        elif c < a and c < b:
            print("You should use company A. It will cost $", c)


while f == True:
    t = float(input("whats the distance you're going?"))
    r = input("do you wish for distance to be in kilometers or miles?")

    scooter(r,t)  