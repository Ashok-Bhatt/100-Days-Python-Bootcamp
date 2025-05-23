#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode="r") as filename:
    letter = filename.readlines()
    print(letter)

with open("./Input/Names/invited_names.txt",mode="r") as newfile:
    names = newfile.readlines()
    print(names)

"""
    for i in names:
        letter[0] = f"Dear {i},"
        with open(f"./Output/ReadyToSend/{i[:-1]}.txt", mode="w") as writing_file:
            writing_file.writelines(letter)
"""