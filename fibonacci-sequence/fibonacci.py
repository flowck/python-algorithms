# Write a Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21, 34, ... (n)

# I found the solution on a book called Beginning Python.

def fibonacci(n): 
	fibs = [0, 1]
	for i in range(n):
		fibs.append(fibs[-2] + fibs[-1])

	return fibs

## print(fibonacci(40))