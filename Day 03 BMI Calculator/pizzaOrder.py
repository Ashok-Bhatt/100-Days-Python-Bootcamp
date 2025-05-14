size = input("Enter your Pizza Size: 'L' for Large, 'M' for Medium and 'S' for Small \n")
addPepper = bool(int(input("Do you want to add pepper? '1' for Yes and '0' for No \n")))
addCheese = bool(int(input("Do you want to add extra cheese? '1' for Yes and '0' for No \n")))

amount = 0

if (size == 'L'):
    amount = 25
    if (addPepper == True):
        amount = amount + 3
elif (size == 'M'):
    amount = 20
    if (addPepper == True):
        amount = amount + 3
else:
    amount = 15
    if (addPepper == True):
        amount = amount + 2

if (addCheese):
    amount = amount + 1

print("\nCost for Pizza: ", amount)