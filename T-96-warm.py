a = int(input("what is you're age?"))

if a <= 13:
    print("you're too young for this game, you baby")
elif a <= 17:
    print("you need permission from gaurdian for this game")
elif a > 17 and a < 42:
    print("welcome and enjoy")
elif a == 42 :
    print("not allowed, you'll embaress the young people")
elif a > 42:
    print("welcome, do you wish to play the regular game, or and 8 bit game for nostalgia")