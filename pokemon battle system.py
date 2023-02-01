import random

level = int(input("what is the level of your pokemon "))
critical = random.randrange(1,10)
power = int(input("what is the power of the attack? "))
stab = input("is your attack the same type as the enemy? (y/n) ")
ran = random.randrange(217,255)
t1 = input("is the attack effective against the opponent. (e), (n), (ne)")
t2 = input("is the attack effevtive against the opponent, (e), (n), (ne). ")
A = int(input("enter the attack stat of the enemy "))
D = int(input("enter the defensive stat of the enemy "))
def poke(
    damage,
    critical,
    power,
    A,
    D,
    stab,
    level,
    t1,
    t2
    ):
    if stab == 'y':
        stab = 2
    elif stab == 'n':
        stab = 1
    if t1 == 'e':
        t1 = 2
    elif t1 == 'n':
        t1 = 1
    elif t1 == 'ne':
        t1 = .5
    if t2 == 'e':
        t2 = 2
    elif t2 == 'n':
        t2 = 1
    elif t2 == 'ne':
        t2 = .5
    if critical <= 2:
        critical = 2
    elif critical >2:
        critical = 1
    damage = (((2*level*critical)/5+2)*power*A/D/50+2)*stab*t1*t2*ran
    print(damage)
    return damage



print(poke(level, critical, power, A, D, stab, ran, t1, t2))
