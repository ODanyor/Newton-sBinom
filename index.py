def main():
	# Here is the main Sigma function
	def sigma(n, to):
		sum_of_i = 0
		for i in range(n, to+1):
			# Put some different formulas here:
			sum_of_i += i

			# Here are some examples:
			# sum_of_i = i**2
			# sum_of_i = 2*i+1
			# sum_of_i = i*(i+1)
			# sum_of_i = i/(i+1)

		print(sum_of_i)

	# Put some values to 'n' and 'to'
	sigma(1, 5)

if __name__ == "__main__":
	main()