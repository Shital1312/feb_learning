"""Higher order Function"""

numbers = [11, 13, 24, 35, 44, 48, 49]


def filter_even(val):
	if val % 2 == 0:
		return True


filter_obj = list(filter(filter_even, numbers))
print(filter_obj)  # even numbers
print(type(filter_obj))  # class 'list'
print(filter_obj)  # again print the even nubers list.
'''Two ways to use filter function but most useful is above because there you can print list many times but below you don't print again list.'''

# filter_obj = (filter(filter_even, numbers))
# print(list(filter_obj)) # even numbers
# print(type(filter_obj)) # class 'filter'
# print(list(filter_obj)) # if we print again then get empty list.

'lambda function: with filter function'
num = [12, 13, 24, 11, 15, 16]
filter_ob = list(filter(lambda n: n > 14, num))
print(filter_ob)

values = [True, False, True, 0, 12]
print(list(filter(None, values)))  # here is all True value is print.

phone = {'Redmi': 10000, 'Vivo': 20000, "iPhone": 100000, 'Realme': 30000, 'Nokia': 25000}
budget = int(input("Enter your price: "))


def filter_price(ele):
	if phone[ele] == budget:
		return True
	else:
		return False


obj = list(filter(filter_price, phone))
print("Your budget product is :", obj)
