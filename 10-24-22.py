friends = ('Eli', 'Alfred', 'Sebastion', 'Cai','Jake', 'Martin', 'Landen')
inventory = []
item = 6
print("what are the ages of your friends?")
for i in range(item):
    age = int(input("age?"))
    inventory.append(age)
for i in range(item):
    print(friends[i],':', inventory[i])# i is going through the 0-5 which is my list and tuple
average = sum(inventory) / len(inventory)
print("the average age is ", average)