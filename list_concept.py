# list1 = [1,2,3,4,5]
# list2 = ['a', 'b', 'c']
# list3 = list1 + list2
# for x in list3:
#     print(x, end = ',')
#
# # print("**********")
# # names = ['Ram', 'Rani']
# # lname = ['Rane', 'Mane']
# # fname = names + lname
# # for name in fname:
# #     print(name, end = ',')
#
#
# '''Converting Two list in one dictionary'''
# names = ['Ram', 'Rani', 'Priya', 'Raj']
# lname = ['Pawar', 'Mane', 'Patil']
# # full_names = names + lname
# # for name in full_names:
# #     print(name, end = ',')
# full_name = zip(names, lname)
# print(dict(full_name))

try:
    num = float(input("Enter your number: "))
    count = 0
    for i in range(0, int(num + 1)):
        count += i
    print(count)

except:
    print("Please enter only integer number..... Try again")

# 1*1 = 1
# 2*1 =2
# 3*2 = 6
# 4*6 = 24
# 5*24 = 120
# friends = ["Raj", "Om"]
# # new_friends = ['Priya', 'sai']
# comma = ",".join(friends)
# print(comma)
