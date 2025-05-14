import pandas as pd

data_dict = {
    "Names" : ["Ashok","Vijay","Ajay"],
    "Score" : [10,20,30]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("My_Scores.csv")