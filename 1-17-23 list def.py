num = []
def cup(num):
    average = sum(num) / len(num)
    print("the average is ", average)

for i in range(6):
        y = int(input("type a number"))
        num.append(y)

cup(num)