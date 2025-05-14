student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_df = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")
data_dict = {value["letter"]:value["code"] for (key,value) in data_df.iterrows()}

for key,value in data_dict.items():
    print(f"{key:<3}{value}")

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_correct = False
while not(is_correct):
    word = input("\nEnter the word: ").upper()
    try:
        phonotic_code = [data_dict[letter] for letter in word]
    except KeyError:
        print("Invalid Input!")
    else:
        is_correct = True

print(phonotic_code)