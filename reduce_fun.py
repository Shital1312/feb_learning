'''REduce function'''
import functools

num = [23, 24, 25, 12, 24]


def func(a, b):
	return a + b


sum1 = functools.reduce(func, num)
print(sum1)

print(functools.reduce(lambda x, y: x + y, num))

number = [11, 12, 13, 34, 45, 67, 89, 99]


def greater(a, b):
	if a > b:
		return a
	else:
		return b


obj = functools.reduce(greater, number)
print(obj)
