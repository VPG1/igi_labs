def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def mult(x, y):
	return x * y

def div(x, y):
	return x / y

def foo(list):
	result = []
	for el in list:
		if el % 2 == 0:
			result.append(el)
	return result
	

print("Hello, world")

print(foo([1, 2, 3, 4]))
