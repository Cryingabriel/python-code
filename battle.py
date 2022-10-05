import random
#___________________________________________________________
def monster(biome):
  num = random.randrange(0, 100)
  if biome == "dungeon":
    if num <= 25:
      battlesystem("Zombie",100)
    elif num <= 45:#30% chance
      battlesystem("Skeleton",100)
    elif num <= 65:
      battlesystem("Spider",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "mansion":
    if num <= 30:
      battlesystem("Scorpion",100)
    elif num <= 50:#30% chance
      battlesystem("Skeleton",100)
    elif num <= 79:
      battlesystem("Spider",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "forest":
    if num <= 25:
      battlesystem("Mushroom",100)
    elif num <= 75:#30% chance
      battlesystem("Fairy",100)
    elif num <= 85:
      battlesystem("Troll",100)
    elif num <= 100:
      battlesystem("Goblin",100)
  elif biome == "outside":
    if num <= 25:
      battlesystem("Skeleton",100)
    elif num <= 75:#30% chance
      battlesystem("Ghost",100)
    elif num <= 85:
      battlesystem("Zombie",100)
    elif num <= 100:
      battlesystem("Slime",100)
#____________________________________________

def battlesystem(monster, playerhealth):
    if monster == "Zombie":
        monsterhealth = 28
        print("a Zombie has spawned in")
    elif monster == "Skeleton":
        monsterhealth = 25
        print("a Skeleton has shot at you")
    elif monster == "Spider":
        monsterhealth = 27
        print("a Spider tried to trap you")
    elif monster == "Goblin":
        monsterhealth = 20
        print("a Goblin is trying to stab you")
    elif monster == "Scorpion":
        monsterhealth = 24
        print("A Scorpion is stinging you")
    elif monster == "Mushroom":
        monsterhealth =16
        print("a mushroom monster tries to poison you")
    elif monster == "Troll":
        monsterhealth =45
        print("a Troll is trying to squash you")
    elif monster == "Fairy":
        monsterhealth =19
        print("Fairies start biting at you")
    elif monster == "Ghost":
        monsterhealth =39
        print("Ghosts are trying take you away")
    elif monster == "Slime":
        monsterhealth =30
        print("slimes are trying to erode you")
        
    while monsterhealth>0 and playerhealth >0:
        if monster == "Zombie":
            monsterattack = random.randrange(9, 14)
        elif monster == "Skeleton":
            monsterattack = random.randrange(8,16)
        elif monster == "Spider":
            monsterattack = random.randrange(7,13)
        elif monster == "Goblin":
            monsterattack = random.randrange(9,17)
        elif monster == "Scorpion":
            monsterattack = random.randrange(7,19)
        elif monster == "Troll":
            monsterattack = random.randrange(16,26)
        elif monster == "Fairy":
            monsterattack = random.randrange(10,15)
        elif monster == "Mushroom":
            monsterattack = random.randrange(13,15)
        elif monster == "Ghost":
            monsterattack = random.randrange(17,18)
        elif monster == "Slime":
            monsterattack = random.randrange(19,24)
            
        print("The", monster, "attacks deal", monsterattack, "damage")
        playerhealth = playerhealth - monsterattack
        print("your HP is at", playerhealth)
        
        playerattack = random.randrange(10,15)
        print("you deal", playerattack, "damage")
        monsterhealth= monsterhealth - playerattack
        print("the monsters HP is at", monsterhealth)
    if monsterhealth<= 0:
        print("you have won")
    else:
        print("you have died")
    return playerhealth
#_________________________________________________________
monster("outside")