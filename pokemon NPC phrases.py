import random


def poke():
    r = random.randrange(1,100)
    l = input("what is your name")
    if r < 25:
        print("Awww Uncle please? I want to chalenge this GYM!")
    if r < 60:
        print("UNCLE, I'll go back to verdanturf")
    if r < 80:
        print("oh wow a pokemon")
    else:
        print("oh", l, "it's me WALLY")


poke()