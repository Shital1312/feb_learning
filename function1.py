"""globals(), locals()"""

a = 10


def demo():
	print("Hello")
	b = 100
	print(locals())
	print(globals()['a'])


demo()
