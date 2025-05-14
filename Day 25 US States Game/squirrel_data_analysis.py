import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"]

data_dict = {
    "Fur Color": ["Gray", "Cinammon", "Black"],
    "Count": [0,0,0]
             }

for entry in data:
    if entry=="Gray":
        data_dict["Count"][0] += 1
    elif entry=="Cinammon":
        data_dict["Count"][1] += 1
    else:
        data_dict["Count"][2] += 1

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")