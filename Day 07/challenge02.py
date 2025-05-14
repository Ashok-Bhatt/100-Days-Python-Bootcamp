word = "freecodecamp"
guess = "c"

word_collection = ["-"]*len(word)
for index,element in enumerate(word):
    if element==guess:
        word_collection[index] = guess

print(word_collection)