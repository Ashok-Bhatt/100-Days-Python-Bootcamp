dict1 = {"Ashok": ["Bhatt",18], "Irfan": ["Ansari",19]}
print(dict1)
print(dict1["Ashok"][0])

dict2 = {"Ashok":["Bhatt",18], "Person":{"Irfan":["Ansari",19]}}
print(dict2)
print(dict2["Person"]["Irfan"][1])

dict3 = [{"Ashok":"Bhatt","Irfan":"Ansari"},{"Lui":"Shirosagi"}]
print(dict3)
print(dict3[0])
print(dict3[0]["Ashok"])