
hours = int(input("what is the hour you get up?"))
minutes = int(input("what is the minute you get up?"))

def yay(hours, minutes):
    minutes -= 40

    if minutes < 0:
        hours -= 1
        minutes = minutes + 60
    if hours <0:
        hours = 23
    print(hours,":", minutes)


print(yay(hours,minutes))
