''''Map function'''

# write a program for finding square each number.

num = [2, 3, 4, 5, 6, 8]


def square(n):
	return n * n


# obj = list(map(square, num))
# print(obj)
obj = map(square, num)
for ele in obj:
	print(ele)

# using lambda function with map
mapped = map(lambda n: n * n, num)
print(list(mapped))

# add two list using map function
list1 = [10, 20, 30]
list2 = [11, 12, 13]


# list3 = map(lambda x, y: x + y, list1, list2)
# print(list(list3))

def add(a, b):
	return a + b


obj = map(add, list1, list2)
# for i in obj:
# 	print(i)
print(list(obj))
