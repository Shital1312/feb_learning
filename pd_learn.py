import pandas as pd

# import numpy as np

# file = pd.read_csv("list_phone.csv")
# # print(d.head())
# # print(d['PRICE'])
# print(file)

dict1 = {"Name": ['Raj', 'Om', 'Priya', 'Ravi', 'Prem'],
		 "Marks": [80, 75, 66, 89, 94],
		 "City": ['Mumbai', 'Delhi', 'Pune', 'Nagar', 'Baner']
		 }

df = pd.DataFrame(dict1)
df.to_csv('Friends.csv', index=False)  # index= Flase means index delete ho jayegi
# print(df.describe()) # print interjer value coloum
var1 = pd.DataFrame(dict1)

var2 = pd.DataFrame(dict1, columns=['Marks'])  # you can find all marks and print marks coloum in terminal
print(var1)  # print all dic data
print(var2)
print(var1['Name'][4])  # you can find any value this way

"""Arithmetic **operation"""
obj = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [4, 5, 6, 7, 8]})
obj["C"] = obj["A"] + obj["B"]
obj.insert(3, "D", [21, 22, 23, 24, 25])  # insert
obj.pop("C")  # delete
# del obj["B"]


print(obj)
