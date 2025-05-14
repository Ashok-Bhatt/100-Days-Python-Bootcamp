import random

def shuffleString(password):

    character = []
    ans = ""

    for i in password:
        character.append(i)
    
    random.shuffle(character)

    for i in character:
        ans = ans + i

    return ans

letters = [chr(65+i) for i in range(26)] + [chr(97+i) for i in range(26)]
numbers = [chr(48+i) for i in range(10)]
symbols = ['!','#','$','%','&','(',')','*','+']

passwordSize = int(input("Password Size: "))
totalNumbers = int(input("Total numbers: "))
totalSymbols = int(input("Total Symbols: "))

if (passwordSize==0 or (totalNumbers+totalSymbols)>passwordSize):
    print("Invalid")
else:
    password = ""

    for i in range(totalNumbers):
        password = password + random.choice(numbers)

    for i in range(totalSymbols):
        password = password + random.choice(symbols)

    for i in range(passwordSize-totalNumbers-totalSymbols):
        password = password + random.choice(letters)
    
    finalPassword = shuffleString(password)
    print("Password: " + finalPassword)