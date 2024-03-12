r = input("what's the secret word\n")
e = int(input("What's ur number of guesses?\n"))
didit = False
guesses = []
word = [_ for _ in r]
for i in range(e):
    ng = 0
    if not r in guesses and ng < e:
        pizza = "ee"
        while len(pizza) != 1:
            pizza = input("What's the ASCII character you're gonna guess?\n")
        guesses.append(pizza)
        ng += 1
        if pizza in word:
            print("Success! You got a character in da word!")
        else:
            print("You guessed a wrong character. You are one more guess away from perishing.")
        correct = 0
        for em in word:
            did = False
            for me in guesses:
                if me == em:
                    print(me, end = " ")
                    correct += 1
                    did = True
                    break
            if not did:
                print("_", end = " ")
            if correct == len(word):
                print("Yippee you did it!!!!!!!!!!!!!!!!")
                didit = True
                break
    if didit:
        break
if not didit:
    print("Y O U   F A I L E D ! ! !")