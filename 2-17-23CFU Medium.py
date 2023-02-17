
level = int(input("What is your level? 1 is bullseye, 2 is the white circle, 3 is the blue circle, etc ending at 5: "))

def targets(level):
    score = 0
    if level == 1:
        score = 50
    if level == 2:
        score = 40
    if level == 3:
        score = 30
    if level == 4:
        score = 20
    if level == 5:
        score = 10
    print("Your score is:", score)

targets(level)