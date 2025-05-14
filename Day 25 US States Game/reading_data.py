""" 
with open("Day 23/weather_data.csv", mode="r") as weather:
    data = weather.readlines()
    print(data)
 """

""" 
import csv
with open("Day 23/weather_data.csv", mode="r") as weather:
    data = csv.reader(weather)
    temperature = []
    for element in data:
        if element[1]!="temp":
            temperature.append(int(element[1]))
    print(temperature)
 """

import pandas as pd
data = pd.read_csv("weather_data.csv")
temperature = data["temp"]
print(data, "\n")

""" 
print(data)
print(type(data),end="\n\n")
print(tempearture)
print(type(temperature))
 """

data_dict = data.to_dict()
print(data_dict, "\n")

temperature_list = temperature.to_list()
print(temperature_list, "\n")

""" 
average_temperature = sum(temperature)/len(temperature)
print("The average of the given temperatures is:",average_temperature)
 """

""" 
# Apart from calculating the mean, we can also calculate the median and mode using it
print("The average of the given temperatures is:",data["temp"].mean())
print("The median of the given temperatures is:",data["temp"].median())
print("The maximum from the given tempeartures is:",data["temp"].max())
 """

""" 
print(data["condition"])        # Key
print(data.condition)           # Attribute
 """

""" 
print(data[data.day=="Monday"], end="\n\n")
print(data[data.temp==data.temp.max()])
 """

""" 
tuesday = data[data.day == "Tuesday"]
print(int(tuesday["temp"]))      # Here, int() function is must, for reference try without using the int() function
print(int(tuesday["temp"])*(9/5)+32)
 """