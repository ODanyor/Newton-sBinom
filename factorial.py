# Factorial for any usage
# Called by other functions

def factorial(number):
	facto = 1
	for n in range(1, number+1):
		facto = facto*n
	return facto