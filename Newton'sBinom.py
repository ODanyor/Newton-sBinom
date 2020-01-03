import time
def main():
	def factorial(number):
		facto = 1
		for n in range(1, number+1):
			facto = facto*n
		return int(facto)

	def permutation(n, k):
		perm = (factorial(n)/factorial(n-k))
		return int(perm)

	def combination(n, k):
		comb = factorial(n)/(factorial(k)*factorial(n-k))
		return int(comb)

	def sigma(n, k):
		start_time = time.time()
		Sum = 0
		for i in range(n, k+1):
			Sum += int(combination(k, i)*(x**(k-i))*y**i)
		print(Sum)
		final_time = time.time()
		print(f"Full time: {final_time - start_time}")
		#return int(Sum)

	# Newton's Binom
	# (x + y)^n
	x=2
	y=2
	return sigma(0, 2)

	# The goal was to implement Newton's binom within factorial, combination and sigma

if __name__ == "__main__":
	main()