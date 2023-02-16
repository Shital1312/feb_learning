import json

# d = {'name': 'Shital', 'Age': 30, 'ismaried': True, 'insurance': None}
# Name= 'Shital'
# Age = '30'
# data = ['shital', 22, True, None]
# data1 = ('Shital', 22, True, None)
#
# var = None
#
# print(json.dumps(d))
# print(type(json.dumps(d))) # json.dumps() does not file create you can see output in your terminal. also trype is 'str' not dict.
# True is converted in true and None is converted in null. also tuple , list both are print in array format.

data = {
    'Age': 23,
    'Name': 'Raj',
    'Number': 345567788,
    'City': 'Pune',
    'Subject': [
        "Computer science",
        "Arts",
        "Commerce"
    ],
    'Is_married': False
}
# f = open('data.json', mode='w')
# json.dump(data, f, indent=4,
#           sort_keys=True)
# separators ko aap last mai kya use karna chahte ho aur key aur value ki beech mai kya vo mention kar skte ho. sort keys means aap alphabet ke anusar data laga skte ho.
# data_json = json.dump(data) # that way you can print all json data in one line.
# print(data_json)

'''json into python dict'''
# data_json = json.dumps(data)
#
# data1 = json.loads(data_json)
# print(data1)  ## you can read data in yout terminal as a python dict.
# print(type(data1))  # dict


f = open('data.json',mode = 'r')
my_data = json.load(f)
print(my_data)
f.close()
