import random

word_list = ["ashok","bhatt","goat"]
chosen_word = random.choice(word_list)

guess = input("Guess the character: ").lower()

for i in chosen_word:
    if i==guess:
        print("Correct Letter")
    else:
        print("Incorrect Letter")

