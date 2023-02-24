'''Arguments'''
"""1. positional arguments- positional must be required.- number of parameter = number of arguments.
2.keyword arguments - provides key value paires as actual arguments. no need to maintain positions, number of parameter = number of arguments.
3. Default arguments- 
4.Variable lenght arguments."""


# positional arguments
def power(a, b):
	print(a ** b)


power(2, 3)  # 8
power(3, 2)  # 9


# keyword arguments
def info(name, age):
	print(f"Name is {name} and age is {age}")


info(name='Ram', age=21)
info(age=30, name='Raj')


# Variable length arguments

def sum1(*num):
	count = 0
	for i in num:
		count += i
	print(count)


sum1(12, 12, 12, 13)
sum1(13, 40, 50)


# Variable length keyword arguments
def sum2(**num):
	count = 0
	for key in num:
		count = count + num[key]

	print(count)


sum2(a=10, b=20)
sum2(a=20, b=30, c=40)
# import keyword
# print(keyword.kwlist)
a = 2e3
print(a)
print(type(a))

a = {1,2,3,4,"Hello",4}
print(a)
print(10,20,30)

a = 5
b = 4
print(~ a)

print((2+1)*2**4/3+4)
print(-9//2)