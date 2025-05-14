word = "shazam"
word_list = ["-"]*len(word)

while ("-" in word_list):

    guess = input("Guess the letter:").lower()
    for index,element in enumerate(word):
        if element==guess and word_list[index]=="-":
            word_list[index] = guess
    
    print(word_list)