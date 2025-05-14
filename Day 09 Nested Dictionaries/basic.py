dict1 = {"Ashok":23, "Bhatt":34}
print(dict1)

dict2 = {}
print(dict2)

dict1["Ashok"] = 1
print(dict1["Ashok"])
print(dict1["Bhatt"])

for keys in dict1:
    print(f"{keys} -----> {dict1[keys]}")

for keys in dict1.keys():
    print(keys)

for values in dict1.values():
    print(values)