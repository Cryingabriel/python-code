ringtoy = []

ringtoy.append("Red")
ringtoy.append("Blue")
ringtoy.append("Purple")

print(ringtoy)

def reverse(str):
    stack = []

    for ch in str:
        stack.append(ch)

    
    rev = " "

    while len(stack):
        rev = rev + stack.pop()
    
    return rev

print(reverse("martin"))

