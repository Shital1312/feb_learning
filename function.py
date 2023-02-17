""" Local variable"""


# colan use for start of function body.
# arguments use for function call.
# parameter use for define the function.

def add2(b, c):  # parameter.
	a = b + c
	print(a)


add2(20, 40)  # arguments.
print('*************')

a = 100
'''Globle Variable'''


def add(b):
	c = a + b
	print(c)  # 105


add(5)
print('*************')

s = 10


def add1():
	global s
	s = s + 5
	print(s)  # 15


add1()
print(s)  # 15
'return statement must at last in funnction, return keyword is only used in funtion, datatype of return value can be anything'
'If you no return values it returns "None" by default. you can return multiply values.'


def abc(a, b):
	sum1 = a + b
	sub = a - b
	return sum1, sub


# sum1,sub = abc(9,3)
# print(sum1)
# print(sub)
# print(type(sum1) # int

total = abc(4, 5)
print(total)
print(type(total))  # tuple

print('*************')


def demo():
	print("Hello")


print(demo())
print('*************')


def outer():
	def inner():
		print("Hello World")
	inner()


outer() # Hello world
