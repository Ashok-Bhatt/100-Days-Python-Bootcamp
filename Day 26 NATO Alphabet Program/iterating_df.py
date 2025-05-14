import pandas as pd

students = {
    "Name" : ["Ashok", "Irfan", "Ankit"],
    "Age" : [19, 19, 18]
}

student_dataframe = pd.DataFrame(students)

# Traversing whole columns
for key,value in student_dataframe.items():
    print(key, value)

# Traversing whole rows
print("\n\n")
for index,entry in student_dataframe.iterrows():
    print(index,entry["Name"])