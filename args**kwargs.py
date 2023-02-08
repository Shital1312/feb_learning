def ave(*numbers):
    print(type(numbers))
    count = 1
    for number in numbers:
        count += number
    print("all numbers avarage is ", count / len(numbers))


ave(2, 3, 4, 5, 3)
'''Args'''


def num(*names):
    for name in names:
        print(name)


har = ["shital", 'khaire', 'pawar', 'vidya', 'rani']
num(*har)

'''**kwargs'''


def job(**employee):
    for key, value in employee.items():
        print(f"Employee name is {key}, and work is {value}")


newemp = {'shital': 'cook', 'Rani': 'Admin', 'Sandip': 'HR', 'Ram': 'Marketing'}
job(**newemp)
